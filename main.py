import views.Menu
import database.criarTabela as database

database.create()
views.Menu.main()
