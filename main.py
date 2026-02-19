from pyscript import document
import asyncio


students = [
    "nathan", "thea", "maiah", "anxela", "gabbie", "joo", "caiomey",
    "athena", "nikolo", "chelsea", "jercey", "sittie", "jarett", "jakob E",
    "chloe", "urielle", "gelo", "ezra", "jakob L", "anika", "kaila",
    "xander", "samie", "pio", "katelyn", "andrei", "hans", "aaron"
]

async def display_players():

    await asyncio.sleep(0.5)
    
  
    container = document.getElementById("player-container")
    
    if container:
   
        container.innerHTML = ""
        
      
        for name in students:
            div = document.createElement("div")
            div.className = "player-card"
            div.innerText = name
            container.appendChild(div)
        
       
        total = document.getElementById("total-players")
        if total:
            total.innerText = "Total players: " + str(len(students))


asyncio.ensure_future(display_players())