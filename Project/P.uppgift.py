# Vilhelm Burevik Sandberg 1990-11-13-1654
# Puppgift Gruppdat
#import os

class Lag(): 

    def __init__(self, team, played,win,draw,loss,scored,conceded,point):
        self.team = team
        self.played = played   # De olika attributen
        self.win = win
        self.draw = draw
        self.loss = loss
        self.scored=scored
        self.conceded=conceded
        self.point=point
        
    def add_played(self):       # Metoder till atributen             
        self.played +=1
    def add_win(self):
        self.point +=3      
        self.win += 1
    def add_draw (self):
        self.point +=1
        self.draw += 1
    def add_loss(self):
        self.loss += 1
    def add_scored(self,value):
        self.scored += value
    def add_conceded(self,value):
        self.conceded += value



        

    def __str__(self): # returnerar text information om lag objektet i tabellen
        return "%15s %4i %4i %4i %4i %4i %4i %4i" % (self.team, self.played, self.win, self.draw, self.loss, self.scored, self.conceded, self.point) 

class Tabell(): # Tabellklass för alla lagen
    def __init__(self, filename):
        self.filename = filename
        self.teams = []                 
        self.read_teams_from_file(filename) 

    def addteam(self,team,played,win,draw,loss,scored,conceded,point):  
        for t in self.teams:
            if t.team == team:
                return False
        self.teams.append(Lag(team,played,win,draw,loss,scored,conceded,point))    # Lägger till lagobjektet i tabellen######
        return True

    
    def findteam(self,team):
        for t in self.teams:
           if team ==t.team[:len(team)]:
               return t                     # Returnerar ett lagobjekt med statesik
        return None
                
        
    def removeteam(self,team): 
        t = self.findteam(team) 
        if t != None:
            self.teams.remove(t)   # Tar bort lagobjektet ur listan

            
    def read_teams_from_file(self,filename):
        fil = open('tabell.txt')
        team_strings = list(map(str.split,fil.readlines())) # skapar en lista med listor för alla lag samt deras statestik
        for row in team_strings:
            if len(row) != 6: # Kollar så alla 6 rader har ett värde
                return False
            name = row[0]
            win=int(row[1])
            draw=int(row[2])
            loss=int(row[3])
            scored=int(row[4])
            conceded=int(row[5])
            played = win + draw + loss
            point = 3*win + draw
            self.addteam(name,played,win,draw,loss,scored,conceded,point)

    
    def add_match(self,team1,team2,goals1,goals2):
        t1 = self.findteam(team1) # Hittar sökta lag samt deras statesikt
        t2 = self.findteam(team2) 
        if t1 ==None or t2 ==None:
            return 
        t1.scored += goals1
        t2.scored += goals2
        t1.conceded += goals2
        t2.conceded += goals1
        if goals1 > goals2: # Hemma vinst
            t1.add_win()
            t2.add_loss()
            
        elif goals1 < goals2: # Borta vinst
            t2.add_win()
            t1.add_loss()
        else:                # Oavgjort
            t2.add_draw()
            t1.add_draw()

        t1.add_played()
        t2.add_played()
            
    def save(self):
        fil = open(self.filename,'w')
        for t in self.teams:          
            s = "%s %i %i %i %i %i\n" % (t.team, t.win, t.draw, t.loss,t.scored,t.conceded) # sparar all info för varje lag
            fil.write(s)

        
        
    def __str__(self): # returnerar text information om objektet efter sortering
        li = self.teams
        li = sorted(li, key = lambda x : (-x.point,-(x.scored - x.conceded),-x.scored,x.team))
        
        s = ''
        s += "%4s %15s %4s %4s %4s %4s %4s %4s %4s\n" % ('', 'Team','S','V','O','F','G','I','Po')
        for i in range(len(self.teams)):
            t = li[i]
            s += "%4i %s\n" % (i + 1, str(t))
        return s
    



def closest_team(tabell, teamname): # Jämför två lag, retuernerar laget som ska bort
    team_list = tabell.teams      #lista med lagobjekt  
    teams = []
    for t in team_list:
        if teamname ==t.team[:len(teamname)]: 
            teams.append(t)
            
    if len(teams) == 1:
        return teams[0].team
    elif len(teams) > 1:
        print('Choose team')
        for i in range(len(teams)):
            print(str(i) + ' ' + teams[i].team)
        n = int(input(">> "))
    return teams[int(n)].team
        

    

                
def main():
    tabell = Tabell('tabell.txt')

    while True:
     #   os.system('clear')
        try:
            a = int(input('välj, \n 1:Lägg till lag \n 2 Ta bort lag \n 3 se tabell \n 4:Lägg in resultat \n 5 Avsluta och spara \n>> '))
        except:
            continue
    
        if a == 1:
            team = input('Skriv in laget:')
            tabell.addteam(team,0,0,0,0,0,0,0)
        if a == 2:
            try:
                team = input('Skriv in laget:')
                team = closest_team(tabell,team)
                tabell.removeteam(team)
            except:
                print('inget lag')
                continue
        if a == 3:
            print(tabell)
            
        if a == 4:
            try:
                hometeam =input("Skriv in hemmalag:")
                hometeam = closest_team(tabell,hometeam)
                awayteam = input("Skriv in bortalag:")
                awayteam = closest_team(tabell,awayteam)
                score1 = int(input("Skriv in antaet mål för hemmalaget:")) #### try testar om det är ett error: ej error vidare
                score2 = int(input("Skriv in antalet mål för bortalaget"))
            except:
                print('Wrong, try agiain')
                continue
            tabell.add_match(hometeam,awayteam,score1,score2) 
                        
        if a == 5:
            tabell.save()
            exit(0)

        input('Press enter to continue...')


if __name__ == '__main__':
    main()
