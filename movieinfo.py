import movie
import fresh_tomatoes
Bajrangi_bhaijan=movie.Movie("Bajrangi Bhaijan","A story of an indian guy dropping a pakistani girl in her native place "
                                   ,"http://static.koimoi.com/wp-content/new-galleries/2015/07/bajrangi-bhaijaan-review.jpg"
                                   ,"https://www.youtube.com/watch?v=vyX4toD395U")

Kick=movie.Movie("Kick","A story of a guy who helps needy",
                       "http://static.koimoi.com/wp-content/new-galleries/2014/07/Kick-New-Poster2.jpg"
                       ,"https://www.youtube.com/watch?v=kNEpMpbmayU")
msdhoni=movie.Movie("Ms Dhoni- The untold story","A story of a guy who became a big cricketer",
                          "http://static.koimoi.com/wp-content/new-galleries/2016/07/m-s-dhoni-the-untold-story-poster-news.jpg",
                          "https://www.youtube.com/watch?v=6L6XqWoS8tw")
dangal=movie.Movie("Dangal","A fatehr who train her girls who become wrestler",
                         "http://media.glamsham.com/download/poster/images/dangal/04-Dangal.jpg",
                         "https://www.youtube.com/watch?v=x_7YlGv9u1g")
soty=movie.Movie("Student Of The Year","Story of college students",
                       "http://media.glamsham.com/download/poster/images/student-of-the-year/Student-of-the-year-11.jpg",
                       "https://www.youtube.com/watch?v=fivOhPjX9YM")
inception=movie.Movie("Inception","A story of dream",
                            "https://movieposters2.com/images/704089-b.jpg",
                            "https://www.youtube.com/watch?v=YoHD9XEInc0")
movies=[Bajrangi_bhaijan,Kick,dangal,msdhoni,soty,inception]

# opening movie webpage
fresh_tomatoes.open_movies_page(movies)
