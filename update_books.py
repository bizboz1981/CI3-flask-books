import os
from app import app
from models import Book
from extensions import db

# Ensure the instance path is set correctly
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'books.db')

# data to update the books
book_details = [
    {
        "title": "To Kill a Mockingbird",
        "isbn": "9780061120084",
        "summary": "A novel about the serious issues of rape and racial inequality.",
        "cover_image_url": "https://example.com/to_kill_a_mockingbird.jpg"
    },
    {
        "title": "1984",
        "isbn": "9780451524935",
        "summary": "A dystopian novel set in a totalitarian society ruled by Big Brother.",
        "cover_image_url": "https://example.com/1984.jpg"
    },
    {
        "title": "Pride and Prejudice",
        "isbn": "9781503290563",
        "summary": "A romantic novel that also offers a biting critique of the British class system.",
        "cover_image_url": "https://example.com/pride_and_prejudice.jpg"
    },
    {
        "title": "The Great Gatsby",
        "isbn": "9780743273565",
        "summary": "A novel set in the Jazz Age that tells the tragic story of Jay Gatsby.",
        "cover_image_url": "https://example.com/the_great_gatsby.jpg"
    },
    {
        "title": "Moby-Dick",
        "isbn": "9781503280786",
        "summary": "A whaling voyage that explores complex themes such as revenge, fate, and the human condition.",
        "cover_image_url": "https://example.com/moby_dick.jpg"
    },
    {
        "title": "War and Peace",
        "isbn": "9780199232765",
        "summary": "A sweeping historical epic about the Napoleonic Wars and the impact on Russian society.",
        "cover_image_url": "https://example.com/war_and_peace.jpg"
    },
    {
        "title": "The Catcher in the Rye",
        "isbn": "9780316769488",
        "summary": "A story about teenage rebellion and alienation narrated by the iconic Holden Caulfield.",
        "cover_image_url": "https://example.com/the_catcher_in_the_rye.jpg"
    },
    {
        "title": "The Hobbit",
        "isbn": "9780547928227",
        "summary": "A fantasy novel that serves as a prelude to The Lord of the Rings.",
        "cover_image_url": "https://example.com/the_hobbit.jpg"
    },
    {
        "title": "Crime and Punishment",
        "isbn": "9780486415871",
        "summary": "A psychological drama about crime, guilt, and redemption.",
        "cover_image_url": "https://example.com/crime_and_punishment.jpg"
    },
    {
        "title": "The Brothers Karamazov",
        "isbn": "9780374528379",
        "summary": "A philosophical and theological novel exploring faith, doubt, and morality.",
        "cover_image_url": "https://example.com/the_brothers_karamazov.jpg"
    },
    {
        "title": "Ulysses",
        "isbn": "9781840226355",
        "summary": "A modernist masterpiece that explores the inner thoughts of its characters.",
        "cover_image_url": "https://example.com/ulysses.jpg"
    },
    {
        "title": "The Odyssey",
        "isbn": "9780140268867",
        "summary": "An epic Greek poem attributed to Homer, telling the story of Odysseus' journey home.",
        "cover_image_url": "https://example.com/the_odyssey.jpg"
    },
    {
        "title": "The Iliad",
        "isbn": "9780140445923",
        "summary": "An ancient Greek epic poem about the Trojan War.",
        "cover_image_url": "https://example.com/the_iliad.jpg"
    },
    {
        "title": "Brave New World",
        "isbn": "9780060850524",
        "summary": "A dystopian novel exploring a future world where the government controls every aspect of life.",
        "cover_image_url": "https://example.com/brave_new_world.jpg"
    },
    {
        "title": "Jane Eyre",
        "isbn": "9780141441146",
        "summary": "A gothic novel that delves into issues of class, sexuality, religion, and feminism.",
        "cover_image_url": "https://example.com/jane_eyre.jpg"
    },
    {
        "title": "Wuthering Heights",
        "isbn": "9780141439556",
        "summary": "A story of intense passion and hatred set on the Yorkshire moors.",
        "cover_image_url": "https://example.com/wuthering_heights.jpg"
    },
    {
        "title": "Frankenstein",
        "isbn": "9780141439471",
        "summary": "A novel that tells the story of Victor Frankenstein and the monster he creates.",
        "cover_image_url": "https://example.com/frankenstein.jpg"
    },
    {
        "title": "Anna Karenina",
        "isbn": "9780199536061",
        "summary": "A tragic story of love and infidelity set in Russian society.",
        "cover_image_url": "https://example.com/anna_karenina.jpg"
    },
    {
        "title": "Madame Bovary",
        "isbn": "9780140449129",
        "summary": "A novel about a doctor's wife who seeks to escape her provincial life.",
        "cover_image_url": "https://example.com/madame_bovary.jpg"
    },
    {
        "title": "The Divine Comedy",
        "isbn": "9780142437223",
        "summary": "An epic poem that represents the journey of the soul toward God.",
        "cover_image_url": "https://example.com/the_divine_comedy.jpg"
    },
    {
        "title": "One Hundred Years of Solitude",
        "isbn": "9780060883287",
        "summary": "A multi-generational story of the Buendía family in the fictional town of Macondo.",
        "cover_image_url": "https://example.com/one_hundred_years_of_solitude.jpg"
    },
    {
        "title": "The Sound and the Fury",
        "isbn": "9780679732242",
        "summary": "A novel that captures the destruction of the Southern aristocracy after the Civil War.",
        "cover_image_url": "https://example.com/the_sound_and_the_fury.jpg"
    },
    {
        "title": "Don Quixote",
        "isbn": "9780142437230",
        "summary": "A Spanish novel about a nobleman who becomes a knight-errant.",
        "cover_image_url": "https://example.com/don_quixote.jpg"
    },
    {
        "title": "In Search of Lost Time",
        "isbn": "9780141180341",
        "summary": "A novel that explores the themes of time, memory, and the search for meaning.",
        "cover_image_url": "https://example.com/in_search_of_lost_time.jpg"
    },
    {
        "title": "Great Expectations",
        "isbn": "9780141439563",
        "summary": "A coming-of-age story that follows the life of Pip, an orphan in Victorian England.",
        "cover_image_url": "https://example.com/great_expectations.jpg"
    },
    {
        "title": "Catch-22",
        "isbn": "9781451626650",
        "summary": "A satirical novel set during World War II, exploring the absurdities of war.",
        "cover_image_url": "https://example.com/catch_22.jpg"
    },
    {
        "title": "Lolita",
        "isbn": "9780679723165",
        "summary": "A controversial novel about an older man's obsession with a young girl.",
        "cover_image_url": "https://example.com/lolita.jpg"
    },
    {
        "title": "Beloved",
        "isbn": "9781400033416",
        "summary": "A novel about the haunting legacy of slavery in post-Civil War America.",
        "cover_image_url": "https://example.com/beloved.jpg"
    },
    {
        "title": "Mrs Dalloway",
        "isbn": "9780156628709",
        "summary": "A modernist novel that captures a single day in the life of Clarissa Dalloway.",
        "cover_image_url": "https://example.com/mrs_dalloway.jpg"
    },
    {
        "title": "Middlemarch",
        "isbn": "9780141439549",
        "summary": "A novel that explores life in a provincial town and the reform movement of the 1830s.",
        "cover_image_url": "https://example.com/middlemarch.jpg"
    },
    {
        "title": "The Count of Monte Cristo",
        "isbn": "9780140449266",
        "summary": "A historical novel about a wrongfully imprisoned man who seeks revenge.",
        "cover_image_url": "https://example.com/the_count_of_monte_cristo.jpg"
    },
    {
        "title": "The Picture of Dorian Gray",
        "isbn": "9780141439570",
        "summary": "A philosophical novel about a man who remains young while his portrait ages.",
        "cover_image_url": "https://example.com/the_picture_of_dorian_gray.jpg"
    },
    {
        "title": "The Stranger",
        "isbn": "9780679720201",
        "summary": "A novel about an indifferent French Algerian who is drawn into a murder.",
        "cover_image_url": "https://example.com/the_stranger.jpg"
    },
    {
        "title": "Fahrenheit 451",
        "isbn": "9781451673319",
        "summary": "A novel about a future society where books are banned and 'firemen' burn them.",
        "cover_image_url": "https://example.com/fahrenheit_451.jpg"
    },
    {
        "title": "Dracula",
        "isbn": "9780141439518",
        "summary": "A gothic horror novel about a vampire count who travels to England.",
        "cover_image_url": "https://example.com/dracula.jpg"
    },
    {
        "title": "The Adventures of Huckleberry Finn",
        "isbn": "9780486280615",
        "summary": "A novel about the adventures of a boy and a runaway slave on the Mississippi River.",
        "cover_image_url": "https://example.com/huckleberry_finn.jpg"
    },
    {
        "title": "The Sun Also Rises",
        "isbn": "9780743297332",
        "summary": "A novel about a group of American and British expatriates in Paris in the 1920s.",
        "cover_image_url": "https://example.com/the_sun_also_rises.jpg"
    },
    {
        "title": "Heart of Darkness",
        "isbn": "9780486264646",
        "summary": "A novella that explores the dark side of European colonialism in Africa.",
        "cover_image_url": "https://example.com/heart_of_darkness.jpg"
    },
    {
        "title": "The Grapes of Wrath",
        "isbn": "9780143039433",
        "summary": "A novel about the hardships faced by American farmers during the Great Depression.",
        "cover_image_url": "https://example.com/the_grapes_of_wrath.jpg"
    },
    {
        "title": "The Old Man and the Sea",
        "isbn": "9780684801223",
        "summary": "A novella about an aging fisherman's struggle to catch a giant marlin.",
        "cover_image_url": "https://example.com/the_old_man_and_the_sea.jpg"
    },
    {
        "title": "A Tale of Two Cities",
        "isbn": "9780141439600",
        "summary": "A historical novel set during the French Revolution.",
        "cover_image_url": "https://example.com/a_tale_of_two_cities.jpg"
    },
    {
        "title": "Les Misérables",
        "isbn": "9780140444308",
        "summary": "A novel about the lives of several characters, including the ex-convict Jean Valjean, in 19th-century France.",
        "cover_image_url": "https://example.com/les_miserables.jpg"
    },
    {
        "title": "Gulliver's Travels",
        "isbn": "9780141439495",
        "summary": "A satire on human nature, recounting the adventures of Lemuel Gulliver.",
        "cover_image_url": "https://example.com/gullivers_travels.jpg"
    },
    {
        "title": "The Scarlet Letter",
        "isbn": "9780142437261",
        "summary": "A novel about the consequences of sin in a rigid Puritan society.",
        "cover_image_url": "https://example.com/the_scarlet_letter.jpg"
    },
    {
        "title": "Alice's Adventures in Wonderland",
        "isbn": "9780141439761",
        "summary": "A whimsical tale of a young girl's adventures in a strange and magical world.",
        "cover_image_url": "https://example.com/alices_adventures_in_wonderland.jpg"
    },
    {
        "title": "To the Lighthouse",
        "isbn": "9780156907392",
        "summary": "A modernist novel about the Ramsay family and their visits to the Isle of Skye.",
        "cover_image_url": "https://example.com/to_the_lighthouse.jpg"
    },
    {
        "title": "Of Mice and Men",
        "isbn": "9780142000670",
        "summary": "A novella that explores the American dream and the burden of friendship.",
        "cover_image_url": "https://example.com/of_mice_and_men.jpg"
    },
    {
        "title": "The Lord of the Rings",
        "isbn": "9780544003415",
        "summary": "An epic high-fantasy novel that continues the story of The Hobbit.",
        "cover_image_url": "https://example.com/the_lord_of_the_rings.jpg"
    }
]

# Use the Flask app context
with app.app_context():
    for details in book_details:
        # Query the book by title
        book = Book.query.filter_by(title=details["title"]).first()
        
        if book:
            # Update the book's details
            book.isbn = details["isbn"]
            book.summary = details["summary"]
            book.cover_image_url = details["cover_image_url"]
            db.session.add(book)  # Mark the book object for update
    
    db.session.commit()  # Commit the changes

print("Books updated successfully!")