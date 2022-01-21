#Status not working


#name of leaders
nominee_1=input("enter the nominee 1 name: ")
nominee_2=input("enter the nominee 2 name: ")

 # votes for nom1,nom2 respectively.
nom_1_votes=0
nom_2_votes=0

#voter id
votes_id=[1,2,3,4,5,6,7,8,9,10]

#no of voter paticipating in election dynamically
num_of_voter=len(votes_id)

while True:
    if votes_id==[]:
        print("voting session over")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/num_of_voter)*100
            print(nominee_1,"has won","with",percent,"% votes")

        elif nom_2_votes>nom_1_votes:
            percent=(nom_2_votes/num_of_voter)*100
            print(nominee_2,"has won","with",percent,"% votes")

    
    else:
      voter=int(input("enter your voter id no : "))
      if voter in votes_id:
        print("you are a voter")
        votes_id.remove(voter)
        vote = int(input("enter your vote 1 or 2:"))
        if vote==1:
            nom_1_votes+=1
            print("Thankyou for casting your vote")

        elif vote==2:
            nom_2_votes+=1
            print("Thankyou for casting your vote")

      else:
        print("you are not a voter here or you have already voted")