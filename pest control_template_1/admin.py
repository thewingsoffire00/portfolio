from flask import *
from database import *
import uuid
from datetime import date, datetime

admin=Blueprint('admin',__name__)

@admin.route('/adhome')
def adhome():

    return render_template('admin_home.html')



@admin.route('/adminmanagestaff',methods=['get','post'])
def adminmanagestaff():
    data={}
    if 'submit' in request.form:
        email=request.form['email']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        house=request.form['house']
        street=request.form['street']
        # city=request.form['city']
        district=request.form['district']
        state=request.form['state']
        pin=request.form['pin']
        phone=request.form['phone']
        Salary=request.form['salary']
        # gender=request.form['gender']
        # dob=request.form['dob']

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','staff','inactive')"%(email,password)
            insert(q)
            q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'inactive')"%(email,fname,lname,house,street,district,state,pin,phone,email,Salary )
            insert(q)
            return redirect(url_for("admin.adminmanagestaff"))

    data={}
    q="select * from staff"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        stid=request.args['stid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='active' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='inactive' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))

    if action == "update":
        q="select * from staff where staff_id='%s'"%(stid)
        val=select(q)
        data['staff']=val


        if 'update' in request.form:
            # email=request.form['email']
            # password=request.form['password']
            fname=request.form['fname']
            lname=request.form['lname']
            house=request.form['house']
            street=request.form['street']
            state=request.form['state']
            district=request.form['district']
            # state=request.form['state']
            pin=request.form['pin']
            phone=request.form['phone']
            # gender=request.form['gender']
            # dob=request.form['dob']

            q="update staff set staff_fname='%s', staff_lname='%s', staff_housename='%s', staff_street='%s',staff_district='%s', staff_pincode='%s', staff_phone='%s',staff_state='%s' where staff_id='%s' "%(fname,lname,house,street,district,pin,phone,state,stid)
            update(q)
            return redirect(url_for("admin.adminmanagestaff"))
    return render_template('admin_manage_staff.html',data=data) 




@admin.route('/adminmanagevendor',methods=['get','post'])
def adminmanagevendor():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
        name=request.form['vname']
       
     
        street=request.form['street']
        city=request.form['city']
        dist=request.form['dist']
        bname=request.form['bname']
       
  
        pin=request.form['pin']
        phone=request.form['phone']
    

       
        q="insert into vendor values (null,'0','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(name,email,bname,street,dist,city,pin,phone)
        insert(q)
        return redirect(url_for("admin.adminmanagevendor"))
    data={}
    q="select * from vendor"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update vendor set status='active' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagevendor"))
    if action == "inactive":
       
        q="update vendor set status='inactive' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagevendor"))

    if action == "update":
        q="select * from vendor where vendor_id='%s'"%(vid)
        val=select(q)
        data['vendor']=val

        if 'update' in request.form:
           
            email=request.form['email']
            name=request.form['vname']
        
        
            street=request.form['street']
            # city=request.form['city']

            dist=request.form['dist']
            bname=request.form['bname']
    
            pin=request.form['pin']
            phone=request.form['phone']

            q="update vendor set v_building_name='%s',v_district='%s', v_name='%s', v_street='%s', v_pincode='%s', v_phone='%s',v_email='%s' where vendor_id='%s' "%(bname,dist,name,street,pin,phone,email,vid)
            update(q)
            return redirect(url_for("admin.adminmanagevendor"))
    return render_template('admin_manage_vendor.html',data=data) 



@admin.route('/adminmanagecourier',methods=['get','post'])
def adminmanagecourier():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
        name=request.form['cname']
       
     
        street=request.form['street']
        dist=request.form['dist']
        bname=request.form['bname']
       
  
        pin=request.form['pin']
        phone=request.form['phone']
    
        uname=request.form['uname']
        passw=request.form['password']

        state=request.form['state']

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("username already exists")
        else:

            q="insert into login values('%s','%s','courier','inactive')"%(uname,passw)
            insert(q)

            q="insert into courier values (null,'0','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'inactive')"%(uname,name,bname,street,dist,state,pin,phone,email)
            insert(q)
        return redirect(url_for("admin.adminmanagecourier"))
    data={}
    q="select * from courier"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update courier set status='active' where courier_id='%s' "%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagecourier"))
    if action == "inactive":
       
        q="update courier set status='inactive' where courier_id='%s' "%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagecourier"))

    if action == "update":
        q="select * from courier where courier_id='%s'"%(vid)
        val=select(q)
        data['cour']=val

        if 'update' in request.form:
           
            email=request.form['email']
            name=request.form['cname']
        
        
            street=request.form['street']
            dist=request.form['dist']
        
    
            pin=request.form['pin']
            phone=request.form['phone']
        
          
            state=request.form['state']

            q="update courier set cour_name='%s', cour_street='%s', cour_district='%s', cour_pincode='%s', cour_phone='%s',cour_email='%s',cour_state='%s' where courier_id='%s' "%(name,street,dist,pin,phone,email,state,vid)
            update(q)
            return redirect(url_for("admin.adminmanagecourier"))
    return render_template('admin_manage_courier.html',data=data) 



@admin.route('/adminmanagecaterogy',methods=['get','post'])
def adminmanagecaterogy():
    data={}
    if 'submit' in request.form:
        img=request.files['img']
        path="static/uploads/"+str(uuid.uuid4())+img.filename
        img.save(path)
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','%s','active')"%(path,name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

    data={}
    q="select * from category"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        cat_id=request.args['cat_id']

      
    else:
        action=None

    if action == "active":
        q="update category set cat_status='active' where cat_id='%s' "%(cat_id)
        update(q) 
        return redirect(url_for("admin.adminmanagecaterogy"))
    if action == "inactive":
        q="update category set cat_status='inactive' where cat_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

    if action == "update":
        q="select * from category where cat_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']
            img=request.files['img']
            path="static/uploads/"+str(uuid.uuid4())+img.filename
            img.save(path)
            q="update category set cat_name='%s', cat_desc='%s',image='%s' where cat_id='%s' "%(name,desc,path,cat_id)
            update(q)
            return redirect(url_for("admin.adminmanagecaterogy"))
    return render_template('admin_manage_category.html',data=data) 



@admin.route('/adminmanagesubcategory',methods=['get','post'])
def adminmanagesubcategory():
    data={}
    p="select * from category"
    data['view']=select(p)
    q="select * from subcategory  "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['cat']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s','active')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagesubcategory"))


    q="select * from subcategory "
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        subid=request.args['subid']

      
    else:
        action=None

    if action == "active":
        q="update subcategory set status='active' where subcat_id='%s' "%(subid)
        update(q) 
        return redirect(url_for("admin.adminmanagesubcategory"))
    if action == "inactive":
        q="update subcategory set status='inactive' where subcat_id='%s' "%(subid)
        update(q)
        return redirect(url_for("admin.adminmanagesubcategory"))

    if action == "update":
        q="select * from subcategory  where subcat_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcat_name='%s', subcat_desc='%s' where subcat_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("admin.adminmanagesubcategory"))
    return render_template('admin_manage_subcategory.html',data=data) 



@admin.route('/adminmanageitems',methods=['get','post'])
def adminmanageitems():
    data={}

    q="select * from category "
    data['sub']=select(q)

    q="select * from subcategory"
    data['subcategory']=select(q)

    if 'submit' in request.form:
        # subid=request.form['subid']
        brid=request.form['brid']
        name=request.form['name']
        desc=request.form['desc']
        # price=request.form['price']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
    
        q="insert into product values (null,'%s','%s','%s','%s','0',0,'active')"%(brid,name,desc,path)
        insert(q)
        return redirect(url_for("admin.adminmanageitems"))


    q="select * from product inner join subcategory using(subcat_id)"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']

      
    else:
        action=None

    if action == "active":
        q="update product set status='active' where product_id='%s' "%(pid)
        update(q) 
        return redirect(url_for("admin.adminmanageitems"))
    if action == "inactive":
        q="update product set status='inactive' where product_id='%s' "%(pid)
        update(q)
        return redirect(url_for("admin.adminmanageitems"))

    if action == "update":
        q="select * from product inner join subcategory using(subcat_id) where product_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            brid=request.form['brid']
            name=request.form['name']
            desc=request.form['desc']
            # price=request.form['price']
            image=request.files['image']
            path="static/uploads/"+str(uuid.uuid4())+image.filename
            image.save(path)
            print(image.filename)
            if image.filename == "":
                q="update product set subcat_id='%s', product_name='%s', product_desc='%s'  where product_id='%s' "%(brid,name,desc,pid)
                update(q)
            else:
                q="update product set subcat_id='%s', product_name='%s', product_desc='%s' , product_img='%s' where product_id='%s' "%(brid,name,desc,path,pid)
                update(q)
            return redirect(url_for("admin.adminmanageitems"))
    return render_template('admin_manage_item.html',data=data) 

@admin.route('/adminmanagepurchase',methods=['get','post'])
def adminmanagepurchase():
    data={}
    q="select * from vendor"
    data['ven']=select(q)
    q="select * from product"
    data['pro']=select(q)
    if 'submit' in request.form:
        ven=request.form['vid']
        proid=request.form['pro']
        cprice=request.form['cprice']
        qty=request.form['qty']
        total=request.form['total']
        selling=request.form['selling']
        q="select * from purchase_master where pstatus='pending'"
        res=select(q)
        if res:
            pmmid=res[0]['pmaster_id']
            q="select * from purchase_details where pmaster_id='%s' and  product_id='%s'"%(pmmid,proid)
            resq=select(q)
            if resq:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="update purchase_details set quantity=quantity+'%s' where product_id='%s' and pmaster_id='%s'"%(qty,proid,pmmid)
                update(q)
            else:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(pmmid,proid,cprice,selling,qty)
                insert(q)
        else:
            q="insert into purchase_master values(null,'%s',0,'%s','pending',now())"%(ven,total)
            id=insert(q)
            q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(id,proid,cprice,selling,qty)
            insert(q)
            flash('Product Added to Purchase List...')
            return redirect(url_for('admin.adminmanagepurchase'))
    
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id and pstatus='pending'"
    res=select(q)
    data['res']=select(q)

    if 'btn' in request.form:
        q="update purchase_master set pstatus='paid' where pstatus='pending'"
        update(q)
        flash('Purchase Completed...')
        return redirect(url_for('admin.adminmanagepurchase'))
    return render_template('admin_manage_purchase.html',data=data)


@admin.route('/adminviewpur')
def adminviewpur():
    data={}
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id "
    res=select(q)
    data['res']=select(q)
    return render_template('admin_view_purchasedlist.html',data=data)



@admin.route('/adminvieworders')
def adminvieworders():
    data={}
    q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and ostatus<>'pending' group by om.order_master_id"
    res=select(q)
    data['res']=select(q)
    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
    else:
        action=None
    if action=='reassihn':
        gg="delete from delivery where order_master_id='%s'"%(omid)
        delete(gg)
        kl="update order_master set ostatus='paid' where order_master_id='%s'"%(omid)
        update(kl)
        flash("reassign.........!")
        return redirect(url_for('admin.admin_assign_to_courier',omid=omid))
    return render_template('admin_view_booking.html',data=data)

@admin.route('/adminviewdetails')
def adminviewdetails():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and ostatus<>'pending' and om.order_master_id='%s'"%(omid)
    res=select(q)
    data['res']=select(q)
    return render_template('admin_view_details.html',data=data)


@admin.route('/adminviewpayment')
def adminviewpayment():
    data={}
    omid=request.args['omid']
    # q="SELECT * FROM payment p,card c,order_master om WHERE p.card_id=c.card_id AND p.order_master_id=om.order_master_id AND p.order_master_id='%s'"%(omid)
    q="select * from payment inner join card using(card_id)"
    data['pay']=select(q)
    return render_template('admin_view_payments.html',data=data)



@admin.route("/adminviewcomplaints",methods=['get','post'])
def adminviewcomplaints():

    
    data={}
    q="select * from customer inner join complaint using (customer_id)"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "reply":
        data['replysec']=True

        if 'submit' in request.form:
            reply=request.form['reply']

            q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
            update(q)
            return redirect(url_for("admin.adminviewcomplaints"))
    return render_template("admin_view_complaints.html",data=data)

@admin.route('/admin_purchase_Report',methods=['get','post'])
def admin_purchase_Report():
    data={}
    now = datetime.now()
    data['current_time'] = now.strftime("%H:%M")
    data['current_date']=date.today()
    if 'sale' in request.form:
        daily=request.form['daily']
        dddaily=request.form['dddaily']
        q="SELECT *,`order_details`.`quantity` AS qty,`order_master`.`date`AS ddate FROM `purchased` INNER JOIN `purchase_details` USING (`pdetails_id`) INNER JOIN `order_details` USING (`order_details_id`) INNER JOIN `product` ON `product`.`product_id`=`order_details`.`product_id`INNER JOIN `order_master`USING(`order_master_id`)INNER JOIN `customer`USING(`customer_id`) where `order_master`.`ostatus`!='pending' and `order_master`.`date` between '%s' and '%s' "%(daily,dddaily)
        data['view']=select(q)
    else:
        q="SELECT *,`order_details`.`quantity` AS qty,`order_master`.`date`AS ddate FROM `purchased` INNER JOIN `purchase_details` USING (`pdetails_id`) INNER JOIN `order_details` USING (`order_details_id`) INNER JOIN `product` ON `product`.`product_id`=`order_details`.`product_id`INNER JOIN `order_master`USING(`order_master_id`)INNER JOIN `customer`USING(`customer_id`) where `order_master`.`ostatus`!='pending'"
        data['view']=select(q)
    return render_template('admin_purchace.html',data=data)


@admin.route('/admin_cust_Report')
def admin_cust_Report():
    data={}
    now = datetime.now()
    data['current_time'] = now.strftime("%H:%M")

    
    data['current_date']=date.today()
    q="SELECT *,CONCAT(c_fname,'',c_lname) AS NAME,CONCAT(c_street,',',c_district,',',c_state,c_pincode) AS address FROM `customer` "
    data['view']=select(q)
    return render_template('admin_cust_Report.html',data=data)

@admin.route('/admin_assign_to_courier',methods=['get','post'])
def admin_assign_to_courier():
    data={}
    omid=request.args['omid']
    ff="SELECT * FROM `courier`WHERE `status`='active'"
    data['view']=select(ff)
    if 'assign' in request.form:
        cor=request.form['cor']
        gg="insert into delivery values(null,'%s','%s',curdate(),DATE_ADD(CURDATE(), INTERVAL 7 DAY),'pending')"%(omid,cor)
        insert(gg)
        kl="update order_master set ostatus='assigned' where order_master_id='%s'"%(omid)
        update(kl)
        flash("ASSIGNED.............!")
        return redirect(url_for('admin.adminvieworders'))
    return render_template('admin_assign_to_courier.html',data=data)
