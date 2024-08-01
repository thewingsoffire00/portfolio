from flask import *
from database import *

courier=Blueprint('courier',__name__)

@courier.route('/courierhome')
def courierhome():

    return render_template('courier_home.html')


@courier.route("/courierviewallreq")
def courierviewallreq():
    data={}
    q="SELECT * FROM `order_master`, `order_details`, `customer`, `product` WHERE `order_master`.`order_master_id`=`order_details`.`order_master_id` AND `order_master`.`customer_id`=`customer`.`customer_id` AND `order_details`.`product_id`=`product`.`product_id` and ostatus='paid'"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
    else:
        action=None

    if action == "accept":
        q="insert into delivery values(null, '%s','%s',curdate(),'Accepted by Courier')"%(omid,session['cor_id'])
        insert(q)
        q="update order_master set ostatus='Accepted by Courier' where order_master_id='%s'"%(omid)
        update(q)
        flash("Couier Accepted")
        # sweetAlert("Hello")
        return redirect(url_for("courier.courierhome"))
    return render_template("courierviewallreq.html",data=data)


@courier.route("/courierviewmyreq")
def courierviewmyreq():
    data={}
    q="SELECT * FROM `order_master`INNER JOIN `delivery`USING(`order_master_id`)INNER JOIN `customer`USING(`customer_id`)WHERE `courier_id`='%s' "%(session['cor_id'])

    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
        did=request.args['did']
    else:
        action=None
    if action=="view_product":
        ggh="SELECT * FROM `order_details`INNER JOIN `product`USING(`product_id`)WHERE `order_master_id`='%s'"%(omid)
        data['view']=select(ggh)
    if action=='pickup':
        q="update delivery set status='0' where delivery_id='%s' "%(did)
        insert(q)
        q="update order_master set ostatus='Pickuped' where order_master_id='%s'"%(omid)
        update(q)
        flash("Order Pickuped.............!")
        return redirect(url_for("courier.courierviewmyreq"))
    if action == "accept":
        q="update delivery set status='Delivery Completed' where delivery_id='%s' "%(did)
        insert(q)
        q="update order_master set ostatus='Delivery Completed' where order_master_id='%s'"%(omid)
        update(q)
        flash("Delivered Successfully")
        return redirect(url_for("courier.courierhome"))
    if action == "unreach":
        gg = "select * from delivery where order_master_id='%s'" % (omid)
        res = select(gg)
        if res[0]['status'] != '3':
            q = "update delivery set status=status + 1 where order_master_id='%s'" % (omid)
            update(q)
            return redirect(url_for("courier.courierviewmyreq"))
        else:
            q = "update delivery set status='Unreachable' where delivery_id='%s'" % (did)
            insert(q)
            q = "update order_master set ostatus='Unreachable' where order_master_id='%s'" % (omid)
            update(q)
            flash("Customer unreachable..........!")
            return redirect(url_for("courier.courierviewmyreq"))
    return render_template("courierviewmyreq.html",data=data)


