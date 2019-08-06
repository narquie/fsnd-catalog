from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, BoardGame, User

engine = create_engine('sqlite:///boardgameswithcategorieswithuser.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

picturehtml = 'https://avatars2.githubusercontent.com/u/24280198?s=460&v=4'
# Create dummy user
User1 = User(name="Nicolas Arquie", email="@gmail.com",
             picture=picturehtml)
session.add(User1)
session.commit()

# The rest of the code is split into sections. I'm a large board game
# afficionado and I put together this list of real games for fun.

categoryCommit = Category(user_id=1, name="Worker Placement")

session.add(categoryCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Agricola",
    description="Farming and family.",
    price="$47.99", difficulty="Medium-Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Lords of Waterdeep",
    description="Recruiting adventurers and finishing quests.",
    price="$39.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Viticulture",
    description="Maintaining a vineyard.",
    price="$45.99", difficulty="Medium-Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Tzolk'in",
    description="Building and offering skulls to the Gods.",
    price="$48.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Caylus",
    description="Construction during the Middle Ages.",
    price="$45.99", difficulty="Medium-Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Dominant Species",
    description="Animals fighting the first Ice Age.",
    price="$62.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Teotihuacan: City of Gods",
    description="Creating temples and houses for the dead.",
    price="$46.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Raiders of the North Sea",
    description="Creating armies and pillaging villagers.",
    price="$38.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Stone Age",
    description="Surviving the Stone Age.",
    price="$45.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Roll and Write")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Railroad Ink (Red)",
    description="Building railroads (meteor and lava expansions).",
    price="$19.99", difficulty="Light-Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Railroad Ink (Blue)",
    description="Building railroads (river and lake expansions)",
    price="$19.99", difficulty="Light-Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Welcome To...",
    description="Building the most attractive suburb.",
    price="$32.99", difficulty="Light-Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Ganz Schon Clever",
    description="Roll dice and place them right!",
    price="$12.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Doppelt So Clever",
    description="Roll dice and place them twice as right!",
    price="$17.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Qwinto",
    description="Managing sums of dice.",
    price="$13.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Area Control")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Scythe",
    description="Combat in an Eastern European steampunk world.",
    price="$69.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Terra Mystica",
    description="Fantasy region claiming.",
    price="$63.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Root",
    description="Woodland animals fight for supremacy.",
    price="$79.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="El Grande",
    description="Allocation of soldiers with changing restrictions",
    price="$50.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Tigris and Euphrates",
    description="Abstract about connecting (or not connecting) regions.",
    price="$54.99", difficulty="Medium-Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Deck / Pool Building ")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Dominion",
    description="The original deckbuilder.",
    price="$31.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Great Western Trail",
    description="Building collections of and selling cattle.",
    price="$54.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Concordia",
    description="Worship the Gods and dominate the market.",
    price="$69.99", difficulty="Medium", category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Orleans",
    description="Dominate feudal France.",
    price="$41.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Mombasa",
    description="Profit the most from colonial Africa",
    price="$46.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Aoens End",
    description="Defend the main city in this dark fantasy world.",
    price="$49.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Push Your Luck")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Quacks of Quedlinburg",
    description="Mix together potions and don't explode!",
    price="$30.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="King of Tokyo",
    description="Become the greatest Kaiju in Tokyo!",
    price="$36.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Port Royal",
    description="Plunder ships and assemble your own crew.",
    price="$16.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Coloretto",
    description="Pick up as many of the same color as you can.",
    price="$8.99", difficulty="Light", category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Deep Sea Adventure",
    description="Gather enough treasure without ANYONE running out of air!",
    price="$19.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Auction / Bidding")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Castles of Mad King Ludwig",
    description="Combine rooms to complete a mad king's castle.",
    price="$44.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Ra",
    description="Bid for power in Ancient Egypt",
    price="$55.99", difficulty="Light-Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Sidereal Confluence",
    description="Share your findings and accumulate the most wealth.",
    price="$52.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Modern Art",
    description="Sell and buy art that isn't worthless!",
    price="$26.99", difficulty="Light-Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Biblios",
    description="Bidding on scrolls to make the best library.",
    price="$19.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

categoryCommit = Category(user_id=1, name="Card Drafting")

session.add(categoryCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Terraforming Mars",
    description="Colonize Mars, and earn prestige along the way.",
    price="$48.99", difficulty="Heavy", category=categoryCommit
)

session.add(boardGameCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="7 Wonders",
    description="Create the best of the ancient empires.",
    price="$28.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Sushi Go Party!",
    description="Draft the tastiest sushi.",
    price="$19.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Seasons",
    description="Grow your magic and control the elements!",
    price="$38.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Kingdomino",
    description="Create a kingdom of similar tiles.",
    price="$15.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Queendomino",
    description="Kingdomino with more features!",
    price="$21.99", difficulty="Light",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit0 = BoardGame(
    user_id=1, name="Millenium Blades",
    description="A card game within a card game.",
    price="$59.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit0)
session.commit()

categoryCommit = Category(user_id=1, name="Variable Player Powers")

session.add(categoryCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="Gloomhaven",
    description="Dark fantasy RPG", price="$118.99",
    difficulty="Heavy", category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Mage Knight",
    description="Fantasy exploration and deckbuilding.",
    price="$61.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()


categoryCommit = Category(user_id=1, name="Cooperative")
session.add(categoryCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Spirit Island",
    description="Protect the natives from invaders.",
    price="$51.99", difficulty="Heavy",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()

boardGameCommit = BoardGame(
    user_id=1, name="Arkham Horror Card Game",
    description="Eldritch horror in expansive campaigns.",
    price="$37.99", difficulty="Medium",
    category=categoryCommit
)

session.add(boardGameCommit)
session.commit()


boardGameCommit = BoardGame(
    user_id=1, name="T.I.M.E. Stories",
    description="Travel through time to prevent catastrophes from happening.",
    price="$32.99", difficulty="Light-Medium", category=categoryCommit
)

session.add(boardGameCommit)
session.commit()


print "Cleared"
