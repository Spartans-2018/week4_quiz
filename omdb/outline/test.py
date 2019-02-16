
import sqlite3
#from omdb_controller import Controller
conn=sqlite3.connect("omdb1.db")
c=conn.cursor()

# # sql="SELECT * FROM movies WHERE title=?"
# # my_cur= c.execute(sql, ("Steam",))
# # my_result=my_cur.fetchone()
# #print (my_result)

# #print (Controller().search_db('Steam'))

# #strin="Robert Downey Jr., Terrence Howard, Jeff Bridges, Gwyneth Paltrow"
# # lst=strin.split(',')
# # for name in lst:
# #     first_name=name.split()[0]
# #     last_name=name.split()[1]
# #     suffix=name.split()[2]
# # #print(lst)

# # sql = """SELECT movies.movie_id, actors.actor_id
# #         FROM movies, actors
# #         WHERE movies.title=? AND actors.first_name=?
# #         AND actors.last_name=?"""

# # sql1="""SELECT * FROM movies WHERE title LIKE ?;"""

# # m='top'

# # t=c.execute(sql1, ('%'+m+'%',))

# # p=c.execute(sql, ('Friends', "Lisa", 'Kudrow'))

# sql2="SELECT * FROM movies_actors WHERE movie_id='1';"
# p=c.execute(sql2)
# row=p.fetchall()
# actors_list=[]
# for pair in row:
#     actors_list.append(str(pair[0]))

# sql3="SELECT * FROM actors WHERE actor_id=(?);"
# actors_names=[]
# for actor in actors_list:
#     v=c.execute(sql3, actor)
#     row1=v.fetchone()[1:]
#     actors_names.append(row1)

# sql3="SELECT * FROM movies_directors WHERE movie_id=?;"
# direct_cur=c.execute(sql3, '5')
# dd=direct_cur.fetchone()
# dir_id=str (dd[0])
# sql4="SELECT * FROM directors WHERE director_id=(?);"
# dir_id_cur=c.execute(sql4, (dir_id,))
# direct_names=dir_id_cur.fetchone()[1:]


# print(actors_names)
sql="SELECT * FROM movies WHERE title LIKE  (?)"
movie_cur=c.execute(sql, ('%'+"eleven"+'%',))
md=movie_cur.fetchall()
movie_id=[]
for i in md:
    movie_id.append(i[0])

c.close()

# name = 'robert downy jr. III'
# print(name.split())
# fn=name.split()[1:]

# print(fn[0]+' '+fn[1])
# last_name=''

# for n in range(1, len(name.split())):
#     last_name=last_name+ name.split()[n]+' '

# print (last_name)

