BEGIN TRANSACTION;

-- DROP TABLE IF EXISTS alembic_version CASCADE;
-- DROP TABLE IF EXISTS book_categories CASCADE;
-- DROP TABLE IF EXISTS reviews CASCADE;
-- DROP TABLE IF EXISTS books CASCADE;
-- DROP TABLE IF EXISTS categories CASCADE;
-- DROP TABLE IF EXISTS contact_messages CASCADE;
-- DROP TABLE IF EXISTS users CASCADE;


-- CREATE TABLE alembic_version (
-- 	version_num VARCHAR(32) NOT NULL, 
-- 	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
-- );
INSERT INTO alembic_version VALUES('fc73138130dd');

-- CREATE TABLE "users" (
-- 	user_id INTEGER NOT NULL, 
-- 	username VARCHAR(50) NOT NULL, 
-- 	email VARCHAR(100) NOT NULL, 
-- 	password_hash VARCHAR(255) NOT NULL, 
-- 	profile_picture_url VARCHAR(255), 
-- 	created_at TIMESTAMP, 
-- 	role VARCHAR(50) DEFAULT 'user' NOT NULL
-- );
INSERT INTO users VALUES(2,'Bill','willjsaunders@icloud.com','scrypt:32768:8:1$pMthLituo1jQrZ7l$34cd907c1cb4d8d329b5947a4b2946849a50c13d42108fcabb368457e18a6d080ff73a72783d7d89f36ff753efb6ca4169a20ad8ec467c81d2ffefb26a73292b','https://www.swansea.ac.uk','2024-08-10 11:40:44.000000','admin');
INSERT INTO users VALUES(3,'Eliza','eliza@icloud.com','scrypt:32768:8:1$mjIlTOKT5eOksANH$d445865b269957ae2a03a0f986513c97ba3c0d1bac796736bb3e8c176f518ed45de46bc781f38efc19e667aed2fa69fc5f234a601084e41a74a20bfc4491b48a','https://www.google.com','2024-08-15 18:57:54.729584','regular');

-- CREATE TABLE books (
-- 	book_id INTEGER NOT NULL, 
-- 	title VARCHAR(255) NOT NULL, 
-- 	author VARCHAR(255) NOT NULL, 
-- 	published_date DATE, 
-- 	isbn VARCHAR(13), 
-- 	summary TEXT, 
-- 	cover_image_url VARCHAR(255), 
-- 	created_at TIMESTAMP, cover_image_data BYTEA, 
-- 	PRIMARY KEY (book_id)
-- );
INSERT INTO books VALUES(1,'To Kill a Mockingbird','Harper Lee','1960-07-11','9780061120084','A novel about the serious issues of rape and racial inequality.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/to_kill_a_mockingbird.jpeg',NULL);
INSERT INTO books VALUES(2,'1984','George Orwell','1949-06-08','9780451524935','A dystopian novel set in a totalitarian society ruled by Big Brother.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/1984.jpeg',NULL);
INSERT INTO books VALUES(3,'Pride and Prejudice','Jane Austen','1813-01-28','9781503290563','A romantic novel that also offers a biting critique of the British class system.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/pride_and_prejudice.jpeg',NULL);
INSERT INTO books VALUES(4,'The Great Gatsby','F. Scott Fitzgerald','1925-04-10','9780743273565','A novel set in the Jazz Age that tells the tragic story of Jay Gatsby.\r\nMy friend''s dog is called Gatsby.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_great_gatsby.jpeg',NULL);
INSERT INTO books VALUES(5,'Moby-Dick','Herman Melville','1851-10-18','9781503280786','A whaling voyage that explores complex themes such as revenge, fate, and the human condition.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/moby_dick.jpeg',NULL);
INSERT INTO books VALUES(6,'War and Peace','Leo Tolstoy','1869-01-01','9780199232765','A sweeping historical epic about the Napoleonic Wars and the impact on Russian society.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/war_and_peace.jpeg',NULL);
INSERT INTO books VALUES(7,'The Catcher in the Rye','J.D. Salinger','1951-07-16','9780316769488','A story about teenage rebellion and alienation narrated by the iconic Holden Caulfield.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_catcher_in_the_rye.jpeg',NULL);
INSERT INTO books VALUES(8,'The Hobbit','J.R.R. Tolkien','1937-09-21','9780547928227','A fantasy novel that serves as a prelude to The Lord of the Rings.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_hobbit.jpeg',NULL);
INSERT INTO books VALUES(9,'Crime and Punishment','Fyodor Dostoevsky','1866-01-01','9780486415871','A psychological drama about crime, guilt, and redemption.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/crime_and_punishment.jpeg',NULL);
INSERT INTO books VALUES(10,'The Brothers Karamazov','Fyodor Dostoevsky','1880-01-01','9780374528379','A philosophical and theological novel exploring faith, doubt, and morality.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_brothers_karamazov.jpeg',NULL);
INSERT INTO books VALUES(11,'Ulysses','James Joyce','1922-02-02','9781840226355','A modernist masterpiece that explores the inner thoughts of its characters.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/ulysses.jpeg',NULL);
INSERT INTO books VALUES(14,'Brave New World','Aldous Huxley','1932-01-01','9780060850524','A dystopian novel exploring a future world where the government controls every aspect of life.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/brave_new_world.jpeg',NULL);
INSERT INTO books VALUES(15,'Jane Eyre','Charlotte Brontë','1847-10-16','9780141441146','A gothic novel that delves into issues of class, sexuality, religion, and feminism.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/jane_eyre.jpeg',NULL);
INSERT INTO books VALUES(16,'Wuthering Heights','Emily Brontë','1847-12-01','9780141439556','A story of intense passion and hatred set on the Yorkshire moors.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/wuthering_heights.jpeg',NULL);
INSERT INTO books VALUES(17,'Frankenstein','Mary Shelley','1818-01-01','9780141439471','A novel that tells the story of Victor Frankenstein and the monster he creates.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/frankenstein.jpeg',NULL);
INSERT INTO books VALUES(18,'Anna Karenina','Leo Tolstoy','1878-01-01','9780199536061','A tragic story of love and infidelity set in Russian society.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/anna_karenina.jpeg',NULL);
INSERT INTO books VALUES(19,'Madame Bovary','Gustave Flaubert','1857-01-01','9780140449129','A novel about a doctor''s wife who seeks to escape her provincial life.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/madame_bovary.jpeg',NULL);
INSERT INTO books VALUES(20,'The Divine Comedy','Dante Alighieri','1320-01-01','9780142437223','An epic poem that represents the journey of the soul toward God.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_divine_comedy.jpeg',NULL);
INSERT INTO books VALUES(21,'One Hundred Years of Solitude','Gabriel Garcia Marquez','1967-05-30','9780060883287','A multi-generational story of the Buendía family in the fictional town of Macondo.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/one_hundred_years_of_solitude.jpeg',NULL);
INSERT INTO books VALUES(22,'The Sound and the Fury','William Faulkner','1929-01-01','9780679732242','A novel that captures the destruction of the Southern aristocracy after the Civil War.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_sound_and_the_fury.jpeg',NULL);
INSERT INTO books VALUES(23,'Don Quixote','Miguel de Cervantes','1605-01-16','9780142437230','A Spanish novel about a nobleman who becomes a knight-errant.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/don_quixote.jpeg',NULL);
INSERT INTO books VALUES(24,'In Search of Lost Time','Marcel Proust','1913-11-14','9780141180341','A novel that explores the themes of time, memory, and the search for meaning.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/in_search_of_lost_time.jpeg',NULL);
INSERT INTO books VALUES(25,'Great Expectations','Charles Dickens','1861-08-01','9780141439563','A coming-of-age story that follows the life of Pip, an orphan in Victorian England.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/great_expectations.jpeg',NULL);
INSERT INTO books VALUES(26,'Catch-22','Joseph Heller','1961-11-10','9781451626650','A satirical novel set during World War II, exploring the absurdities of war.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/catch_22.jpeg',NULL);
INSERT INTO books VALUES(27,'Lolita','Vladimir Nabokov','1955-09-15','9780679723165','A controversial novel about an older man''s obsession with a young girl.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/lolita.jpeg',NULL);
INSERT INTO books VALUES(28,'Beloved','Toni Morrison','1987-09-16','9781400033416','A novel about the haunting legacy of slavery in post-Civil War America.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/beloved.jpeg',NULL);
INSERT INTO books VALUES(29,'Mrs Dalloway','Virginia Woolf','1925-05-14','9780156628709','A modernist novel that captures a single day in the life of Clarissa Dalloway.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/mrs_dalloway.jpeg',NULL);
INSERT INTO books VALUES(30,'Middlemarch','George Eliot','1871-12-01','9780141439549','A novel that explores life in a provincial town and the reform movement of the 1830s.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/middlemarch.jpeg',NULL);
INSERT INTO books VALUES(31,'The Count of Monte Cristo','Alexandre Dumas','1844-01-01','9780140449266','A historical novel about a wrongfully imprisoned man who seeks revenge.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_count_of_monte_cristo.jpeg',NULL);
INSERT INTO books VALUES(32,'The Picture of Dorian Gray','Oscar Wilde','1890-06-20','9780141439570','A philosophical novel about a man who remains young while his portrait ages.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_picture_of_dorian_gray.jpeg',NULL);
INSERT INTO books VALUES(33,'The Stranger','Albert Camus','1942-01-01','9780679720201','A novel about an indifferent French Algerian who is drawn into a murder.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_stranger.jpeg',NULL);
INSERT INTO books VALUES(34,'Fahrenheit 451','Ray Bradbury','1953-10-19','9781451673319','A novel about a future society where books are banned and ''firemen'' burn them.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/fahrenheit_451.jpeg',NULL);
INSERT INTO books VALUES(35,'Dracula','Bram Stoker','1897-05-26','9780141439518','A gothic horror novel about a vampire count who travels to England.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/dracula.jpeg',NULL);
INSERT INTO books VALUES(36,'The Adventures of Huckleberry Finn','Mark Twain','1884-12-10','9780486280615','A novel about the adventures of a boy and a runaway slave on the Mississippi River.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/huckleberry_finn.jpeg',NULL);
INSERT INTO books VALUES(37,'The Sun Also Rises','Ernest Hemingway','1926-10-22','9780743297332','A novel about a group of American and British expatriates in Paris in the 1920s.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_sun_also_rises.jpeg',NULL);
INSERT INTO books VALUES(38,'Heart of Darkness','Joseph Conrad','1899-01-01','9780486264646','A novella that explores the dark side of European colonialism in Africa.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/heart_of_darkness.jpeg',NULL);
INSERT INTO books VALUES(39,'The Grapes of Wrath','John Steinbeck','1939-04-14','9780143039433','A novel about the hardships faced by American farmers during the Great Depression.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_grapes_of_wrath.jpeg',NULL);
INSERT INTO books VALUES(40,'The Old Man and the Sea','Ernest Hemingway','1952-09-01','9780684801223','A novella about an aging fisherman''s struggle to catch a giant marlin.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_old_man_and_the_sea.jpeg',NULL);
INSERT INTO books VALUES(41,'A Tale of Two Cities','Charles Dickens','1859-04-30','9780141439600','A historical novel set during the French Revolution.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/a_tale_of_two_cities.jpeg',NULL);
INSERT INTO books VALUES(42,'Les Misérables','Victor Hugo','1862-01-01','9780140444308','A novel about the lives of several characters, including the ex-convict Jean Valjean, in 19th-century France.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/les_miserables.jpeg',NULL);
INSERT INTO books VALUES(43,'Gulliver’s Travels','Jonathan Swift','1726-01-01','5134987331354','The travels of Gulliver','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/gullivers_travels.jpeg',NULL);
INSERT INTO books VALUES(44,'The Scarlet Letter','Nathaniel Hawthorne','1850-03-16','9780142437261','A novel about the consequences of sin in a rigid Puritan society.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_scarlet_letter.jpeg',NULL);
INSERT INTO books VALUES(45,'Alice''s Adventures in Wonderland','Lewis Carroll','1865-11-26','9780141439761','A whimsical tale of a young girl''s adventures in a strange and magical world.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/alices_adventures_in_wonderland.jpeg',NULL);
INSERT INTO books VALUES(46,'To the Lighthouse','Virginia Woolf','1927-05-05','9780156907392','A modernist novel about the Ramsay family and their visits to the Isle of Skye.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/to_the_lighthouse.jpeg',NULL);
INSERT INTO books VALUES(47,'Of Mice and Men','John Steinbeck','1937-11-23','9780142000670','A novella that explores the American dream and the burden of friendship.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/of_mice_and_men.jpeg',NULL);
INSERT INTO books VALUES(48,'The Lord of the Rings','J.R.R. Tolkien','1954-07-29','9780544003415','An epic high-fantasy novel that continues the story of The Hobbit.','https://raw.githubusercontent.com/bizboz1981/CI3-flask-books/main/static/assets/img/the_lord_of_the_rings.jpeg',NULL);
INSERT INTO books VALUES(49,'Emma','Jane Austen','1810-01-01',NULL,'Comedy of manners','https://m.media-amazon.com/images/I/61JkX0mbbyL._AC_UF894,1000_QL80_.jpg',NULL);
INSERT INTO books VALUES(50,'Love in the Time of Cholera','Gabriel Garcia Marquez','1990-01-01','554313','Magical realism in South America','https://m.media-amazon.com/images/I/61OBwknuKsL._AC_UF894,1000_QL80_.jpg',NULL);
INSERT INTO books VALUES(51,'Persuasion','Jane Austen','1815-01-01','9780192833617','A classic piece of literature ','https://m.media-amazon.com/images/I/81mUs+3qcfL._AC_UF894,1000_QL80_.jpg',NULL);
INSERT INTO books VALUES(52,'The Mill on the Floss','George Eliot',NULL,'1265432875435','Explores big themes of death','https://m.media-amazon.com/images/I/61lPnFKLJ8L._AC_UF894,1000_QL80_.jpg',NULL);
-- CREATE TABLE categories (
-- 	category_id INTEGER NOT NULL, 
-- 	category_name VARCHAR(50) NOT NULL, 
-- 	PRIMARY KEY (category_id), 
-- 	UNIQUE (category_name)
-- );
INSERT INTO categories VALUES(1,'Fiction');
INSERT INTO categories VALUES(2,'Non-Fiction');
INSERT INTO categories VALUES(3,'Science Fiction');
INSERT INTO categories VALUES(4,'Fantasy');
INSERT INTO categories VALUES(5,'Biography');
INSERT INTO categories VALUES(6,'History');
INSERT INTO categories VALUES(7,'Children');
INSERT INTO categories VALUES(8,'Mystery');
INSERT INTO categories VALUES(9,'Romance');
INSERT INTO categories VALUES(10,'Horror');
INSERT INTO categories VALUES(11,'Classics');
INSERT INTO categories VALUES(12,'Historical');
INSERT INTO categories VALUES(13,'Dystopian');
INSERT INTO categories VALUES(14,'Adventure');
INSERT INTO categories VALUES(15,'Young Adult');
INSERT INTO categories VALUES(16,'Psychological');
INSERT INTO categories VALUES(17,'Philosophical');
INSERT INTO categories VALUES(18,'Modernist');
INSERT INTO categories VALUES(19,'Epic');
INSERT INTO categories VALUES(20,'Tragedy');
INSERT INTO categories VALUES(21,'Poetry');
INSERT INTO categories VALUES(22,'Magical Realism');
INSERT INTO categories VALUES(23,'Satire');
INSERT INTO categories VALUES(24,'War');
INSERT INTO categories VALUES(25,'Gothic');
-- CREATE TABLE book_categories (
-- 	book_id INTEGER NOT NULL, 
-- 	category_id INTEGER NOT NULL, 
-- 	PRIMARY KEY (book_id, category_id), 
-- 	FOREIGN KEY(book_id) REFERENCES books (book_id), 
-- 	FOREIGN KEY(category_id) REFERENCES categories (category_id)
-- );
INSERT INTO book_categories VALUES(1,1);
INSERT INTO book_categories VALUES(1,11);
INSERT INTO book_categories VALUES(1,12);
INSERT INTO book_categories VALUES(2,1);
INSERT INTO book_categories VALUES(2,13);
INSERT INTO book_categories VALUES(2,11);
INSERT INTO book_categories VALUES(3,1);
INSERT INTO book_categories VALUES(3,9);
INSERT INTO book_categories VALUES(3,11);
INSERT INTO book_categories VALUES(4,1);
INSERT INTO book_categories VALUES(4,11);
INSERT INTO book_categories VALUES(4,12);
INSERT INTO book_categories VALUES(5,1);
INSERT INTO book_categories VALUES(5,11);
INSERT INTO book_categories VALUES(5,14);
INSERT INTO book_categories VALUES(6,1);
INSERT INTO book_categories VALUES(6,11);
INSERT INTO book_categories VALUES(6,12);
INSERT INTO book_categories VALUES(7,1);
INSERT INTO book_categories VALUES(7,11);
INSERT INTO book_categories VALUES(7,15);
INSERT INTO book_categories VALUES(8,1);
INSERT INTO book_categories VALUES(8,4);
INSERT INTO book_categories VALUES(8,14);
INSERT INTO book_categories VALUES(9,1);
INSERT INTO book_categories VALUES(9,11);
INSERT INTO book_categories VALUES(9,16);
INSERT INTO book_categories VALUES(10,1);
INSERT INTO book_categories VALUES(10,11);
INSERT INTO book_categories VALUES(10,17);
INSERT INTO book_categories VALUES(11,1);
INSERT INTO book_categories VALUES(11,11);
INSERT INTO book_categories VALUES(11,18);
INSERT INTO book_categories VALUES(14,1);
INSERT INTO book_categories VALUES(14,13);
INSERT INTO book_categories VALUES(14,11);
INSERT INTO book_categories VALUES(15,1);
INSERT INTO book_categories VALUES(15,9);
INSERT INTO book_categories VALUES(15,11);
INSERT INTO book_categories VALUES(16,1);
INSERT INTO book_categories VALUES(16,9);
INSERT INTO book_categories VALUES(16,11);
INSERT INTO book_categories VALUES(17,1);
INSERT INTO book_categories VALUES(17,10);
INSERT INTO book_categories VALUES(17,11);
INSERT INTO book_categories VALUES(18,1);
INSERT INTO book_categories VALUES(18,11);
INSERT INTO book_categories VALUES(18,9);
INSERT INTO book_categories VALUES(19,1);
INSERT INTO book_categories VALUES(19,11);
INSERT INTO book_categories VALUES(19,20);
INSERT INTO book_categories VALUES(20,1);
INSERT INTO book_categories VALUES(20,11);
INSERT INTO book_categories VALUES(20,19);
INSERT INTO book_categories VALUES(20,21);
INSERT INTO book_categories VALUES(21,1);
INSERT INTO book_categories VALUES(21,11);
INSERT INTO book_categories VALUES(21,22);
INSERT INTO book_categories VALUES(22,1);
INSERT INTO book_categories VALUES(22,11);
INSERT INTO book_categories VALUES(22,18);
INSERT INTO book_categories VALUES(23,1);
INSERT INTO book_categories VALUES(23,11);
INSERT INTO book_categories VALUES(23,14);
INSERT INTO book_categories VALUES(24,1);
INSERT INTO book_categories VALUES(24,11);
INSERT INTO book_categories VALUES(24,18);
INSERT INTO book_categories VALUES(25,1);
INSERT INTO book_categories VALUES(25,11);
INSERT INTO book_categories VALUES(26,1);
INSERT INTO book_categories VALUES(26,11);
INSERT INTO book_categories VALUES(26,23);
INSERT INTO book_categories VALUES(26,24);
INSERT INTO book_categories VALUES(27,1);
INSERT INTO book_categories VALUES(27,11);
INSERT INTO book_categories VALUES(27,16);
INSERT INTO book_categories VALUES(28,1);
INSERT INTO book_categories VALUES(28,11);
INSERT INTO book_categories VALUES(28,12);
INSERT INTO book_categories VALUES(29,1);
INSERT INTO book_categories VALUES(29,11);
INSERT INTO book_categories VALUES(29,18);
INSERT INTO book_categories VALUES(30,1);
INSERT INTO book_categories VALUES(30,11);
INSERT INTO book_categories VALUES(30,12);
INSERT INTO book_categories VALUES(31,1);
INSERT INTO book_categories VALUES(31,11);
INSERT INTO book_categories VALUES(31,14);
INSERT INTO book_categories VALUES(32,1);
INSERT INTO book_categories VALUES(32,11);
INSERT INTO book_categories VALUES(32,25);
INSERT INTO book_categories VALUES(33,1);
INSERT INTO book_categories VALUES(33,11);
INSERT INTO book_categories VALUES(33,17);
INSERT INTO book_categories VALUES(34,1);
INSERT INTO book_categories VALUES(34,13);
INSERT INTO book_categories VALUES(34,11);
INSERT INTO book_categories VALUES(35,1);
INSERT INTO book_categories VALUES(35,10);
INSERT INTO book_categories VALUES(35,11);
INSERT INTO book_categories VALUES(36,1);
INSERT INTO book_categories VALUES(36,11);
INSERT INTO book_categories VALUES(36,14);
INSERT INTO book_categories VALUES(37,1);
INSERT INTO book_categories VALUES(37,11);
INSERT INTO book_categories VALUES(37,12);
INSERT INTO book_categories VALUES(38,1);
INSERT INTO book_categories VALUES(38,11);
INSERT INTO book_categories VALUES(38,14);
INSERT INTO book_categories VALUES(39,1);
INSERT INTO book_categories VALUES(39,11);
INSERT INTO book_categories VALUES(39,12);
INSERT INTO book_categories VALUES(40,1);
INSERT INTO book_categories VALUES(40,11);
INSERT INTO book_categories VALUES(40,14);
INSERT INTO book_categories VALUES(41,1);
INSERT INTO book_categories VALUES(41,11);
INSERT INTO book_categories VALUES(41,12);
INSERT INTO book_categories VALUES(42,1);
INSERT INTO book_categories VALUES(42,11);
INSERT INTO book_categories VALUES(42,12);
INSERT INTO book_categories VALUES(43,1);
INSERT INTO book_categories VALUES(43,11);
INSERT INTO book_categories VALUES(43,4);
INSERT INTO book_categories VALUES(43,23);
INSERT INTO book_categories VALUES(44,1);
INSERT INTO book_categories VALUES(44,11);
INSERT INTO book_categories VALUES(44,9);
INSERT INTO book_categories VALUES(45,1);
INSERT INTO book_categories VALUES(45,11);
INSERT INTO book_categories VALUES(45,4);
INSERT INTO book_categories VALUES(45,7);
INSERT INTO book_categories VALUES(46,1);
INSERT INTO book_categories VALUES(46,11);
INSERT INTO book_categories VALUES(46,18);
INSERT INTO book_categories VALUES(47,1);
INSERT INTO book_categories VALUES(47,11);
INSERT INTO book_categories VALUES(47,12);
INSERT INTO book_categories VALUES(48,1);
INSERT INTO book_categories VALUES(48,4);
INSERT INTO book_categories VALUES(48,19);
INSERT INTO book_categories VALUES(50,18);
INSERT INTO book_categories VALUES(50,22);
INSERT INTO book_categories VALUES(51,9);
INSERT INTO book_categories VALUES(51,11);
-- CREATE TABLE reviews (
-- 	review_id INTEGER NOT NULL, 
-- 	book_id INTEGER NOT NULL, 
-- 	user_id INTEGER NOT NULL, 
-- 	rating INTEGER NOT NULL, 
-- 	review_text TEXT, 
-- 	created_at TIMESTAMP, 
-- 	PRIMARY KEY (review_id), 
-- 	FOREIGN KEY(book_id) REFERENCES books (book_id), 
-- 	FOREIGN KEY(user_id) REFERENCES users (user_id)
-- );
INSERT INTO reviews VALUES(1,49,2,5,'Absolutely glorious book!','2024-08-10 20:43:20.449826');
INSERT INTO reviews VALUES(2,49,2,5,'Absolutely glorious book!','2024-08-10 20:43:40.768364');
INSERT INTO reviews VALUES(3,5,2,3,'Not read this one','2024-08-10 20:46:13.448584');
INSERT INTO reviews VALUES(4,16,2,5,'Looking forward to reading this one','2024-08-12 19:40:27.853710');
INSERT INTO reviews VALUES(5,3,2,5,'Daddy is the best in the world','2024-08-15 18:16:06.592772');
INSERT INTO reviews VALUES(6,3,2,5,'Flossie is the best in the world 💗🌎🗺️','2024-08-15 18:21:38.237901');
INSERT INTO reviews VALUES(7,3,2,4,'Mummy  is good','2024-08-15 18:23:26.908639');
INSERT INTO reviews VALUES(8,3,3,5,'Eliza is the best in the world 🗺️','2024-08-15 19:00:50.240486');
INSERT INTO reviews VALUES(9,50,2,5,'cool book','2024-08-21 18:18:38.967055');
INSERT INTO reviews VALUES(10,16,2,5,'Enjoying this so far','2024-08-24 10:32:10.099167');
INSERT INTO reviews VALUES(11,51,2,5,'Review','2024-08-24 11:49:39.115728');
INSERT INTO reviews VALUES(12,51,2,5,'I Love Flossie♥️💖','2024-08-24 11:52:35.558534');
INSERT INTO reviews VALUES(13,1,2,3,'I found this a tad depressing. I prefer Jane Austen','2024-09-11 16:00:41.347624');
INSERT INTO reviews VALUES(14,1,2,5,'Beautiful cover. I haven''t read the book, but judging by its cover, it''s 5 stars all the way.','2024-09-11 16:03:29.444418');
INSERT INTO reviews VALUES(15,2,2,4,'testing','2024-09-11 17:14:28.497358');
INSERT INTO reviews VALUES(16,2,2,3,'Does this review persist?','2024-09-11 17:14:49.028379');
INSERT INTO reviews VALUES(17,2,2,2,'Clever but dreary','2024-09-11 17:22:31.214236');


-- CREATE TABLE _alembic_tmp_users (
-- 	user_id INTEGER NOT NULL, 
-- 	username VARCHAR(50) NOT NULL, 
-- 	email VARCHAR(100) NOT NULL, 
-- 	password_hash VARCHAR(128), 
-- 	profile_picture_url VARCHAR(255), 
-- 	created_at TIMESTAMP, 
-- 	role VARCHAR(50) DEFAULT 'user' NOT NULL, 
-- 	PRIMARY KEY (user_id), 
-- 	UNIQUE (username), 
-- 	UNIQUE (email)
-- );
-- CREATE TABLE contact_messages (
--     id SERIAL PRIMARY KEY,
--     name TEXT NOT NULL,
--     email TEXT NOT NULL,
--     message TEXT NOT NULL,
--     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );
INSERT INTO contact_messages VALUES(1,'Bill','willjsaunders@icloud.com','Testing','2024-09-07 07:40:34');
COMMIT;
