import trailer
import fresh_tomatoes
kerintha=trailer.Favouritemovies("Kerintha","A story about colle"
                                 "ge students","https://www.chitramal"
                                 "a.in/wp-content/uploads/2015/05/Kerint"
                                 "ha-Poster-300x300.jpg","https://www.youtube.co"
                                 "m/watch?v=zdjqWHj65Uk")
lifeisbeautiful=trailer.Favouritemovies("life is beautiful","a story about students","http://www.totalmovieinfo.com/w"
                                        "p-content/uploads/2018/05/1-16.jpg","https://youtu.be/Zh7Bfviqn30")

happydays=trailer.Favouritemovies("Happy days","a story about college students","https://c.saavncdn.com/361"
                                  "/Happy-Days-2007-500x500.jpg","https://youtu.be/BYy7gkao5cw")
kalasala=trailer.Favouritemovies("kalasala","a story about college students","http://www.myindiclub.com/music/2"
                                 "/KALASALA/KALASALA.JPG","https://youtu.be/fg5QALirV-I")
snehitudu=trailer.Favouritemovies("snehitudu","A story about college students","http"
                                  "s://i.pinimg.com/236"
                                  "x/a8/12/8f/a8128f07b20bc9c6852177b68def7feb.jpg","https://"
                                  
                                  "youtu.be/eYZ_bP9xGpQ")
robo=trailer.Favouritemovies("robo2","a movie about cellphones","https://i.ytimg.com/vi/0eMQl_quDV8/maxresdefault.jpg","https://youtu.be/RWNrgxgqbdc")
movies=[kerintha,lifeisbeautiful,happydays,kalasala,snehitudu,robo]
fresh_tomatoes.open_movies_page(movies)

