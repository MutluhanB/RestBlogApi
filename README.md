# RestBlogApi

---CRUD REST BLOG API---


->API python dilinde flask frameworkü ile kodlanmıştır. 
->Veri tabanı olarak SQLite seçilmiştir.
->Veri tabanı tek tablodan meydana gelmektedir. id,title ve text olmak üzere tablonun 3 kolonu bulunmaktadır, id bilgisi otomatik olarak üretilmektedir api'a sadece json formatında
title ve text bilgisi gönderilmesi yeterlidir
->Veri tabanı ile daha kolay etkileşebilmek için Python kütüphanelerinden SQLAlchemy ve ORM tool olarak da Marshmallow kullanılmıştır.
->Uygulama default olarak 5000 portunda çalışmaktadır localhost:5000/blog adresinden aşşağıda detayları verilen istekleri kullanarak api ile etkileşebilirsiniz.
->Uygulama Ubuntu işletim sisteminde Postman üzerinde test edilmiştir. Json içeriği postman arayüzünden Headers kısmında Key bilgisi "Content-Type" Value Bilgisi "application/json" seçildikten sonra 
body kısmına eklenerek api'a istek atılabilmektedir.

-GEREKSİNİMLER-
*Eksik olan gereksinimleri "python3 -m pip install [libraryname]" komutu ile yükleyebilirsiniz.
->Flask
->flask_sqlalchemy
->flask_marshmallow (sqlalchemy ile beraber çalışmak için ek yükleme istemesi halinde python3 -m pip install marshmallow-sqlalchemy komutu ile sorun çözülebilir)

-UYGULAMAYI ÇALIŞTIRMAK-
->Zip dosyasından uygulamayı çıkardıktan sonra çıkardığınız dizinde bir terminal ekranı açın.
->"python3 blogAPi.py" komutu ile uygulamayı çalıştırın
	->Uygulamanın çalışması halinde uygulamanın 5000 portunda çalıştığı ile ilgili bilgiler göreceksinizdir.
	->Eksik kütüphaneler ile ilgili hatalar için yukarıdaki gereksinimler kısmını inceleyebilirsiniz. 

-ENDPOINTLER-

1-)POST /blog
*Bu endpoint üzerinden yeni bir blog post yayınlanabilmektedir. Gönderilen post uygulama dizinindeki blog_db.sqlite veritabanına eklenecektir. İsteğe eklenebilecek örnek bir json:

{
	"title" : "This post is solely for testing purposes",
	"text"	: "This is a test post"
}


2-)GET /blog
*Bu endpoint üzerine boş bir GET request gönderildiğinde var olan tüm blog postları json formatında döndermektedir.

3)GET /blog/<id>
*Bu endpoint üzerine boş bir GET request gönderildiğinde verilen id ile eşleşen blog post json formatında dönderilmektedir.

4-)PUT /blog/<id>
*Bu endpoint üzerine boş bir PUT request gönderildiğinde verilen id ile eşleşen blog post isteğe eklenen json bilgisine göre güncellenmektedir.

örneğin localhost:5000/blog/1 adresine bir PUT isteğinin aşşağıdaki örnek json header'ı ile gönderilmesi halinde 1 numaralı postun içeriği ilgili json ile güncellenecektir
örnek json:

{
	"title" : "Title updated via PUT method",
	"text"	: "Content updated via PUT method"
}


5-)DELETE /blog/<id>
*Bu endpoint üzerine boş bir DELETE request gönderildiğinde verilen id ile eşleşen blog post silinecektir.



-MUTLUHAN BOZ 03/19
