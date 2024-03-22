import streamlit as st
import pyperclip
import time
from st_copy_to_clipboard import st_copy_to_clipboard


# List of categories
categories = [
    "Acoustic", "Adult", "Adult Contemporary", "Ambient", "Americana", "Archive", "Atmospheres/Drones/Beds", "Big Band", "Blues", "Children/Kids", "Choral/Chant", "Christmas", "Classical/Opera", "Comedy/Cartoon", "Corporate", "Country/Western", "Dance/Electronic", "Documentary", "Drama", "Drums/Percussion", "Easy Listening", "Film/TV Styles", "Folk", "Funk", "Hip-Hop/Rap", "Jazz", "Kitsch/Retro", "Latin", "Marches/Ceremonial/Fanfares", "National Anthem", "Orchestral/Symphonic", "Pop", "Pop Rock", "R&B/Soul", "Reggae", "Religious/Gospel", "Rock", "Solo/Featured Instrument", "Sound Design/FX", "Special Occasions", "Sports", "Traditional Dances", "Trailers", "Underscore", "Well Known Themes", "World Music"
]

# List of subcategories
subcategories = [
    "4th of July/Independence Day", "A Capella", "Acid", "Acoustic", "Action", "Adult", "Adult Contemporary", "Adventure", "Africa", "Africa > Central Africa", "Africa > Central Africa > Angola", "Africa > Central Africa > Central African Republic", "Africa > Central Africa > Chad", "Africa > Central Africa > Democratic Republic of the Congo/DCR (Zaire)", "Africa > Central Africa > Equatorial Guinea", "Africa > Central Africa > Guinea Bissau", "Africa > Central Africa > Republic of the Congo", "Africa > Eastern Africa", "Africa > Eastern Africa > Burundi", "Africa > Eastern Africa > Eritrea", "Africa > Eastern Africa > Ethiopia", "Africa > Eastern Africa > Islands", "Africa > Eastern Africa > Kenya", "Africa > Eastern Africa > Madagascar", "Africa > Eastern Africa > Malawi", "Africa > Eastern Africa > Mauritius", "Africa > Eastern Africa > Mozambique", "Africa > Eastern Africa > Rwanda", "Africa > Eastern Africa > Seychelles", "Africa > Eastern Africa > Somalia", "Africa > Eastern Africa > Tanzania", "Africa > Eastern Africa > Uganda", "Africa > Eastern Africa > Zambia", "Africa > Eastern Africa > Zimbabwe", "Africa > Northern Africa", "Africa > Northern Africa > Algeria", "Africa > Northern Africa > Libya", "Africa > Northern Africa > Morocco", "Africa > Northern Africa > Sudan", "Africa > Northern Africa > Tunisia", "Africa > Southern Africa", "Africa > Southern Africa > Botswana", "Africa > Southern Africa > Lesotho", "Africa > Southern Africa > Namibia", "Africa > Southern Africa > South Africa", "Africa > Southern Africa > Swaziland", "Africa > Southern Africa > Zambia", "Africa > Western Africa", "Africa > Western Africa > Benin", "Africa > Western Africa > Burkina Faso", "Africa > Western Africa > Cameroon", "Africa > Western Africa > Cape Verde", "Africa > Western Africa > Gabon", "Africa > Western Africa > Gambia", "Africa > Western Africa > Ghana", "Africa > Western Africa > Guinea", "Africa > Western Africa > Ivory Coast", "Africa > Western Africa > Liberia", "Africa > Western Africa > Mali", "Africa > Western Africa > Mauritania", "Africa > Western Africa > Niger", "Africa > Western Africa > Nigeria", "Africa > Western Africa > Senegal", "Africa > Western Africa > Sierra Leone", "Africa > Western Africa > Togo", "Afro-Punk/AfroPunk", "AfroBeat", "Airy", "Alternative", "Ambient", "Americana", "Anthem", "Archive", "Artsy", "Asia", "Asia > Central Asia", "Asia > Central Asia > Afghanistan", "Asia > Central Asia > Armenia", "Asia > Central Asia > Azerbaijan", "Asia > Central Asia > Georgia", "Asia > Central Asia > Kazakhstan", "Asia > Central Asia > Kyrgyzstan", "Asia > Central Asia > Tajikistan", "Asia > Central Asia > Turkmenistan", "Asia > Central Asia > Uzbekistan", "Asia > East Asia", "Asia > East Asia > China (Peoples Republic of China)", "Asia > East Asia > Hong Kong", "Asia > East Asia > Japan", "Asia > East Asia > Korea", "Asia > East Asia > Korea > Korea, North", "Asia > East Asia > Korea > Korea, South", "Asia > East Asia > Macao", "Asia > East Asia > Mongolia", "Asia > East Asia > Taiwan (Republic of China)", "Asia > East Asia > Tibet", "Asia > South Asia", "Asia > South Asia > Bangladesh", "Asia > South Asia > India", "Asia > South Asia > Nepal", "Asia > South Asia > Pakistan", "Asia > Southeastern Asia", "Asia > Southeastern Asia > Bali", "Asia > Southeastern Asia > Brunei", "Asia > Southeastern Asia > Cambodia", "Asia > Southeastern Asia > Indonesia", "Asia > Southeastern Asia > Java", "Asia > Southeastern Asia > Laos", "Asia > Southeastern Asia > Malaysia", "Asia > Southeastern Asia > Myanmar / Burma", "Asia > Southeastern Asia > Philippines", "Asia > Southeastern Asia > Singapore", "Asia > Southeastern Asia > Thailand", "Asia > Southeastern Asia > Vietnam", "Asia > Southeastern Asia > Vietnam > Vietnam, North", "Asia > Southeastern Asia > Vietnam > Vietnam, South", "Atmospheric", "Avant Garde", "Bachata", "Background/Elevator", "Baion", "Ballad", "Ballroom Dance", "Ballroom Dance > Beguine", "Ballroom Dance > Blackbottom", "Ballroom Dance > Bolero", "Ballroom Dance > Bossa Nova", "Ballroom Dance > Cha Cha", "Ballroom Dance > Charleston", "Ballroom Dance > Conga Line", "Ballroom Dance > Foxtrot", "Ballroom Dance > Habanera", "Ballroom Dance > Lambada", "Ballroom Dance > Mambo", "Ballroom Dance > Merengue", "Ballroom Dance > Military Two Step", "Ballroom Dance > Paso Doble", "Ballroom Dance > Polka", "Ballroom Dance > Quickstep", "Ballroom Dance > Rhumba", "Ballroom Dance > Salsa", "Ballroom Dance > Samba", "Ballroom Dance > Swing/Jitterbug/Jive", "Ballroom Dance > Tango", "Ballroom Dance > Two Step", "Ballroom Dance > Waltz", "Banda", "Baroque", "Baroque Pop", "Baseball", "Basketball", "Batucada", "Beats", "Bebop", "Birthday", "Bluegrass", "Blues", "Bohemian", "Bomba", "Boogie Woogie", "Bossa Nova", "Bounce", "Boxing/UFC/Wrestling", "Brass", "Brazilian", "Brazilian > Afoxé", "Brazilian > Arrocha", "Brazilian > Axé", "Brazilian > Baião", "Brazilian > Baile Funk", "Brazilian > Boi", "Brazilian > Brega", "Brazilian > Brega funk", "Brazilian > Carimbó", "Brazilian > Chamamé", "Brazilian > Chorinho/Choro", "Brazilian > Ciranda", "Brazilian > Coco", "Brazilian > Eletrobrega", "Brazilian > Embolada", "Brazilian > Forró", "Brazilian > Frevo", "Brazilian > Guitarrada", "Brazilian > Ijexá", "Brazilian > Jongo", "Brazilian > Lundu", "Brazilian > Maculele", "Brazilian > Manguebeat", "Brazilian > Maracatu", "Brazilian > Marchinha", "Brazilian > Maxixe", "Brazilian > Modinha", "Brazilian > MPB", "Brazilian > Pagode", "Brazilian > Pagode Baiano", "Brazilian > Partido Alto", "Brazilian > Piseiro", "Brazilian > Rastapé", "Brazilian > Repente", "Brazilian > Samba de Roda", "Brazilian > Samba Jazz", "Brazilian > Samba Rock", "Brazilian > Sertanejo", "Brazilian > Tropicália", "Brazilian > Vaneira/Vaneirão", "Brazilian > Xaxado", "Brazilian > Xote", "Breakbeat", "Breakdance", "Bright/Optimistic", "Brit", "Britpop", "Buddhism", "Bumpers", "Cabaret", "Cajun", "Carols", "Cartoon", "Celtic", "Cha Cha", "Chamber Pop", "Champeta", "Charanga", "Chase", "Chase/Detective/Mystery", "Cheesy", "Chicago", "Children", "Chillout", "Chillwave", "Chiptune", "Choral", "Christian", "Christmas", "Cinematic", "Classic", "Classic Rock", "Classic/Orchestral", "Classical", "Classical Dance", "Classical Dance > Ballet", "Classical Dance > Bouree", "Classical Dance > Gavotte", "Classical Dance > Gigue", "Classical Dance > Mazurka", "Classical Dance > Minuet", "Classical Dance > Pavane", "Classical Dance > Polonaise", "Classical Dance > Waltz, Classical", "Classical Form", "Classical Form > Adagio", "Classical Form > Aria", "Classical Form > Cadenza", "Classical Form > Cantata", "Classical Form > Concerto", "Classical Form > Concerto Grosso", "Classical Form > Etude", "Classical Form > Fugue", "Classical Form > Gregorian Chant", "Classical Form > Madrigal", "Classical Form > Mass", "Classical Form > Opera", "Classical Form > Operetta", "Classical Form > Oratorio", "Classical Form > Overture", "Classical Form > Prelude", "Classical Form > Rondo", "Classical Form > Sonata", "Classical Form > Symphony", "Classical Form > Theme and Variation", "Classical/Opera Fusion/Remix", "Club", "Cocktail", "College", "Colombian", "Comedy", "Communication/News", "Conga", "Conscious Hip-Hop", "Contemporary", "Contemporary R & B", "Cool", "Corrido", "Countries/English", "Countries/French", "Countries/German", "Countries/Italian", "Countries/Russian", "Countries/Spanish", "Country", "Cowboy", "Cricket", "Crime", "Crooner", "Cuban", "Cumbia", "Dance", "Dancehall", "Danza", "Death Metal", "Deep Funk", "Delta", "Dembow", "Detective/Mystery", "Detective/Spy", "Detroit Soul", "Dirge", "Dirty South/Crunk", "Disco", "Distorted", "Ditty", "Diva", "Dixieland", "DIY", "Documentary", "Doo Wop", "Downtempo", "Drama", "Dramedy", "Dream Pop", "Drinking Song", "Drone", "Drum & Bass", "Drum Corps", "Drumkit", "Drumline", "Drums", "Dub", "Dubstep", "Duet", "Easter", "Easy Listening", "Eclectic", "EDM", "Electric", "Electro", "Electro Jazz", "Electro Swing", "Electronic", "Electronica", "Emo", "Epic", "Ethereal", "Etherpop", "Ethnic", "Europe", "Europe > Eastern Europe", "Europe > Eastern Europe > Belarus", "Europe > Eastern Europe > Bulgaria", "Europe > Eastern Europe > Czech Republic", "Europe > Eastern Europe > Hungary", "Europe > Eastern Europe > Moldavia", "Europe > Eastern Europe > Poland", "Europe > Eastern Europe > Romania", "Europe > Eastern Europe > Russia / Former USSR", "Europe > Eastern Europe > Slovakia", "Europe > Eastern Europe > Ukraine", "Europe > Northern Europe", "Europe > Northern Europe > Denmark", "Europe > Northern Europe > England", "Europe > Northern Europe > Estonia", "Europe > Northern Europe > Finland", "Europe > Northern Europe > Iceland", "Europe > Northern Europe > Ireland", "Europe > Northern Europe > Ireland > Northern Ireland", "Europe > Northern Europe > Ireland > Republic of Ireland", "Europe > Northern Europe > Isle Of Man", "Europe > Northern Europe > Latvia", "Europe > Northern Europe > Lithuania", "Europe > Northern Europe > Northern Ireland", "Europe > Northern Europe > Norway", "Europe > Northern Europe > Scandinavia", "Europe > Northern Europe > Scotland", "Europe > Northern Europe > Sweden", "Europe > Northern Europe > United Kingdom", "Europe > Northern Europe > Wales", "Europe > Southern Europe", "Europe > Southern Europe > Albania", "Europe > Southern Europe > Bosnia Herzegovina", "Europe > Southern Europe > Croatia", "Europe > Southern Europe > Greece", "Europe > Southern Europe > Italy", "Europe > Southern Europe > Italy > Vatican City", "Europe > Southern Europe > Macedonia", "Europe > Southern Europe > Malta", "Europe > Southern Europe > Montenegro", "Europe > Southern Europe > Portugal", "Europe > Southern Europe > San Marino", "Europe > Southern Europe > Serbia", "Europe > Southern Europe > Slovenia", "Europe > Southern Europe > Spain", "Europe > Western Europe", "Europe > Western Europe > Andorra", "Europe > Western Europe > Austria", "Europe > Western Europe > Belgium", "Europe > Western Europe > France", "Europe > Western Europe > Germany", "Europe > Western Europe > Germany > Bavaria", "Europe > Western Europe > Luxembourg", "Europe > Western Europe > Monaco", "Europe > Western Europe > Netherlands", "Europe > Western Europe > Switzerland", "Exercise/Fitness/Recreational", "Exotic", "Expansive", "Experimental", "Extreme", "Factual", "Fairytale", "Family", "Fandango", "Fanfare/Charge", "Fanfares", "Fantasy", "Film/Porn", "Flamenco", "Folk", "Folk > Calypso", "Folk > Celtic", "Folk > Gypsy Style", "Folk > Klezmer", "Folk > Native American", "Food/Cooking", "Football > American", "Football > Soccer/Futbol/Rugby", "Found Sounds", "Free Jazz", "French", "Fun", "Funeral/Elegy", "Funk", "Fusion/Hybrid", "Future Bass", "Future Garage", "Future RnB", "G-Funk", "Gambling", "Game Show", "Gangsta", "Garage", "General", "German", "Glam", "Glitch", "Golf", "Gospel", "Gothic", "Graduation", "Grass Roots", "Grime", "Gritty", "Groove", "Groovy", "Grunge", "Grupero", "Guaguanco", "Guajira", "Guaracha", "Guitar", "Gypsy", "Halloween", "Hanukkah", "Hard", "Hard Rock", "Hardcore", "Heartland", "Heavy Metal", "Hick-Hop", "Hillbilly", "Hindu", "Hip Hop", "Honky Tonk", "Horror", "Horse/Racing/Equestrian", "House", "Hyperpop", "Ice Hockey", "IDM", "Indie", "Indietronica", "Industrial", "Investigative", "Islamic", "Island", "Jazz", "Jewish", "Jig", "Jungle", "K-Pop", "Keys/Piano", "Kiddie", "Kitschy", "Klezmer", "Kuduro", "Large Ensemble", "Late Night", "Latin", "Latin America", "Latin America > Caribbean/West Indies", "Latin America > Caribbean/West Indies > Bahamas", "Latin America > Caribbean/West Indies > Barbados", "Latin America > Caribbean/West Indies > Bermuda", "Latin America > Caribbean/West Indies > Cuba", "Latin America > Caribbean/West Indies > Dominican Republic", "Latin America > Caribbean/West Indies > Haiti", "Latin America > Caribbean/West Indies > Jamaica", "Latin America > Caribbean/West Indies > Puerto Rico", "Latin America > Central America", "Latin America > Central America > Belize", "Latin America > Central America > Costa Rica", "Latin America > Central America > El Salvador", "Latin America > Central America > Guatemala", "Latin America > Central America > Honduras", "Latin America > Central America > Mexico", "Latin America > Central America > Nicaragua", "Latin America > Central America > Panama", "Latin America > South America", "Latin America > South America > Argentina", "Latin America > South America > Bolivia", "Latin America > South America > Brazil", "Latin America > South America > Chile", "Latin America > South America > Colombia", "Latin America > South America > Ecuador", "Latin America > South America > French Guyana", "Latin America > South America > Guyana", "Latin America > South America > Paraguay", "Latin America > South America > Peru", "Latin America > South America > Suriname", "Latin America > South America > Uruguay", "Latin America > South America > Venezuela", "LGBTQ", "Lifestyle", "Light", "Live", "LoFi", "Lounge", "Love Song", "Lovers Rock", "Lullaby", "Mambo", "Mandopop", "March", "Marching Band", "Mariachi", "Martial Arts", "Medieval", "Mediterranean", "Merengue", "Metal", "Mexican Banda", "Miami Sound", "Middle East", "Middle East > Bahrain", "Middle East > Cyprus", "Middle East > Egypt", "Middle East > Iran", "Middle East > Iraq", "Middle East > Israel", "Middle East > Jordan", "Middle East > Kuwait", "Middle East > Lebanon", "Middle East > Oman", "Middle East > Qatar", "Middle East > Saudi Arabia", "Middle East > Syria", "Middle East > Turkey", "Middle East > United Arab Emirates", "Middle East > Yemen", "Midwest", "Military/War", "Minimal Techno", "Minimalist Style", "Modern", "Modern Blues", "Modern Classical/Neo Classical", "Motivational", "Motor Sports", "Motown", "Mythical", "Nature/Science", "Nautical", "Neo-Classical", "Neo-Soul", "New Age", "New Orleans", "New Wave", "New Year's Day", "News", "Newsreel", "Noir", "Norteño", "North America", "North America > Canada", "North America > USA", "North America > USA > Alaska/Pacific Northwest", "North America > USA > East Coast", "North America > USA > Hawaii", "North America > USA > South", "North America > USA > Southwest", "Nu Disco", "Nu-Folk/Pop", "Nu-Metal", "Nursery Rhymes/Well Known Themes", "Oceania/South Pacific", "Oceania/South Pacific > Australia", "Oceania/South Pacific > Cook Islands", "Oceania/South Pacific > Fiji", "Oceania/South Pacific > New Zealand", "Oceania/South Pacific > Samoa", "Oceania/South Pacific > Tahiti", "Oceania/South Pacific > Tonga", "Old School", "Old World", "Orchestral", "Orchestral/Symphonic", "Other", "Other Dance", "Other Dance > Can Can", "Other Dance > Go Go", "Other Dance > Jerk", "Other Dance > Soft Shoe", "Other Dance > Tap", "Other Dance > Twist", "Other Forms", "Other Forms > Arrangement", "Other Forms > Drone", "Other Forms > Fanfare", "Other Forms > Hymn", "Other Forms > Logo", "Other Forms > Loop/Riff", "Other Forms > Lullaby", "Other Forms > Remix", "Other Forms > Rhythm Track", "Pacific Northwest", "Pastoral", "Percolating", "Percussion", "Podcast", "Pop", "Pop Punk", "Pop Rock", "Porro", "Post", "Post Rock", "Power Ballad", "Power/Energetic", "Prestige/Luxury", "Prog Rock", "Progressive", "Promo", "Psychedelic", "Public Domain", "Pulsing", "Punk", "Quiet Storm", "Quirky", "R&B", "Ragtime", "Raï", "Ranchera", "Rap", "Rare Grooves", "Rave", "Raw", "Reggae", "Reggaeton", "Religious", "Remix", "Retro", "Rhythm & Blues", "Rhythm Bed", "Riser", "Rises", "Roadhouse", "Rock", "Rock n Roll", "Rockabilly", "Rocksteady", "Romantic", "Romantic Comedy", "Roots", "Royal", "Rural", "Salsa", "Samba", "Schlager", "Sci-Fi", "Science/Technology", "Score", "Second Line", "Shoegaze", "Shuffle", "Silent", "Singer Songwriter", "Sitcom", "Ska", "Skating/Figure Skating/Ice Skating", "Skating/Speed Skating", "Skiing", "Slapstick", "Small Ensemble", "Small Group", "Smooth", "Soap Opera/Telenovela", "Soca", "Soft", "Soft Rock", "Solea", "Son", "Song", "Soul", "Sound FX", "Soundscape", "Southern", "Spaghetti Western", "Spanish", "Speed Metal", "Spiritual", "Spoof", "Sports", "St Patrick's Day", "Stadium", "Stage Musical", "Stately", "Stings", "Stomp & Clap", "Storytelling", "String", "Striptease", "Surf", "Swamp", "Sweeping", "Swimming", "Swing", "Swooshes", "Synth", "Synthwave", "Talk Show", "Tango", "Techno", "Tejano", "Tennis", "Tex Mex", "Textural", "Thanksgiving", "Thrash Metal", "Thriller/Suspense", "Track & Field", "Traditional", "Traditional Folk/Ethnic Dance", "Traditional Folk/Ethnic Dance > Hora", "Traditional Folk/Ethnic Dance > Line Dance", "Traditional Folk/Ethnic Dance > Square Dance / Hoe Down", "Trailers /Score", "Training", "Trance", "Transition", "Trap", "Travel/Vacation", "Tribal", "Trio", "Trip Hop", "Tropical", "Tumba", "Turkish", "Tween", "Underground", "Underscore", "Valentine's Day", "Vallenato", "Vaudeville/Vintage", "Venezuelan > Gaita", "Venezuelan > Joropo", "Venezuelan > Llanera", "Vocal", "Waltz", "Weather", "Wedding", "Wellness/Relaxation", "West Coast", "Western", "Wind", "World", "World Games", "World Games/Sport", "Youthful", "Zydeco"
]




def filter_options(options, filter_text):
    return [option for option in options if filter_text.lower() in option.lower()]

st.markdown("<h1 style='text-align: center;'>SUGGESTER</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Categories')
    category_filter = st.text_input('Filter categories', key='category_filter')
    filtered_categories = filter_options(categories, category_filter)
    for cat in filtered_categories:
        if st.button(f'{cat}'):
            st_copy_to_clipboard(cat)
            st.success(f'Copied "{cat}" to clipboard!', icon="✨")

with col2:
    st.subheader('Subcategories')
    subcategory_filter = st.text_input('Filter subcategories', key='subcategory_filter')
    filtered_subcategories = filter_options(subcategories, subcategory_filter)
    for subcat in filtered_subcategories:
        if st.button(f'{subcat}'):
            st_copy_to_clipboard(subcat)
            st.success(f'Copied "{subcat}" to clipboard!', icon="✨")
