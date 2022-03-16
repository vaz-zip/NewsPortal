Модуль D2. ИТОГОВОЕ ЗАДАНИЕ 2.9 (HW-03)
Группа FPW-57, Ширяев К.В.

         1.Создать двух пользователей. 
           Команды:
u1 = User.objects.create_user(username='Sanny')
u2 = User.objects.create_user(username='Vally')

          2.Создать два объекта модели Author, связанные с пользователями.
            Команды:
Author.objects.create(author_user=u1)
Author.objects.create(author_user=u2) 

          3.Добавить четыре категории в модель Category.
            Команды:
c1 = Category.objects.create(category_theme='В стране')
c2 = Category.objects.create(category_theme='В мире')
c3 = Category.objects.create(category_theme='Экономика')
c4 = Category.objects.create(category_theme='Технологии')
          
          4.Добавить две статьи и одну новость.
            Команды:
author = Author.objects.get(id=1)
Post.objects.create(post_author=author, position='CTA', title='Стихи', news_text='Сказать, что ты...')   
Post.objects.create(post_author=author, position='CTA', title='Проза', news_text='Правду говорить легко...') 
Post.objects.create(post_author=author, position='HOB', title='Новости', news_text='Сегодня в России...')      

          5.Присвоить статьям категории.
            Команды:
Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))    
Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3)) 
Post.objects.get(id=3).post_category.add(Category.objects.get(id=4))

          6.Создать min 4 комментария к объектам модели Post.
            Команды:
Comment.objects.create(comment_post=Post.objects.get(id=1), comment_user=Author.objects.get(id=1).author_user, comment_us='WOW')
Comment.objects.create(comment_post=Post.objects.get(id=2), comment_user=Author.objects.get(id=1).author_user, comment_us='Лучше всех!')
Comment.objects.create(comment_post=Post.objects.get(id=3), comment_user=Author.objects.get(id=2).author_user, comment_us='!!!')
Comment.objects.create(comment_post=Post.objects.get(id=3), comment_user=Author.objects.get(id=2).author_user, comment_us='YYYEEESSS')

          7.Применяя функции like(), dislike() к статьям/новостям и комментариям,  скорректировать рейтинги этих объектов.
            Команды:
Comment.objects.get(id=1).like()                                                                                                     
Comment.objects.get(id=2).like() 
Comment.objects.get(id=3).like() 
Comment.objects.get(id=4).dislike()
  
          8.Обновить рнйтинги пользователей.
            Команды:
a = Author.objects.get(id=1)
a.update_rating()
a.author_rating
b = Author.objects.get(id=2)
b.update_rating()
b.author_rating

          9.Вывести username и рейтинг лучшего пользователя.
            Команды:
a = Author.objects.order_by('-author_rating')[:1] 
a

          10.Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дизлайках к этой статье.
             Команды:
bestPost = Post.objects.all().order_by('-rating')[0]
comments = bestPost.comment_set.all()
    for c in comments:
...     c.time_comment
...     c.comment_user
...     c.rating


          11.Вывести все комментарии к этой статье.
             Команды:
bestPost = Post.objects.all().order_by('-rating')[0]
comments = bestPost.comment_set.all()
    for c in comments:
...     c.comment_us
