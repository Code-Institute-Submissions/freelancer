function quote(){
    document.getElementById("total").innerHTML = "";

    categoryValue = document.getElementById("category").value;
    countValue = document.getElementById("count").value;

    if (countValue > 1000) 
         { price = countValue / 100}
    else 
         {price = 10}
    if (categoryValue != "general") {price = price * 1.1}
    price = Math.round(price).toFixed(2);
    discount = (price / 100 * 80).toFixed(2);


  
  
    category = document.getElementById("category")
 

    count = document.getElementById("count")
    
  

    /*form validation */
    if (countValue <= 0)
         {count.style.borderColor= "red"; count.classList.add('fill-error');}
    else
         {count.style.borderColor = "rgb(59, 55, 55)"; }
    
    if (categoryValue == "choose")
         {category.style.borderColor= "red"; category.classList.add('fill-error');}
    else
         {category.style.borderColor = "rgb(59, 55, 55)"};

    setTimeout(function() {
              count.classList.remove('fill-error');
              category.classList.remove('fill-error')
          }, 400);
      if (countValue != 0 && categoryValue != "choose")  
         {document.getElementById("total").innerHTML = "Was" + "<span id=\"crossed\"> €" + price + "</span>"+"<span class=\"handwrite\"> Now only €" + discount + "</span>";}
        
  }
  function quote2(){
       category = document.getElementById("category");
       description = document.getElementById("id_description");
       count = document.getElementById("id_number");

       categoryValue = document.getElementById("category").value;
       descriptionValue = document.getElementById("id_description").value;
       countValue = document.getElementById("id_number").value;

       if (categoryValue == "choose")
       {category.style.borderColor= "red"; category.classList.add('fill-error');}
       else
       {category.style.borderColor = "rgb(59, 55, 55)"};

       if (descriptionValue == "")
       {description.style.borderColor= "red"; description.classList.add('fill-error');}
       else
       {description.style.borderColor = "rgb(59, 55, 55)"};
     
       if (countValue <= 0)
       {count.style.borderColor= "red"; count.classList.add('fill-error');}
       else
       {count.style.borderColor = "rgb(59, 55, 55)"};


       setTimeout(function() {
          description.classList.remove('fill-error');
          category.classList.remove('fill-error')
          count.classList.remove('fill-error')
      }, 400);
  }