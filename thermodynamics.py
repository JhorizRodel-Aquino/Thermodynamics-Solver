def ENTHALPY():
    enthalpy=((Hmol_p1*Hproduct1)+(Hmol_p2*Hproduct2))-((Hmol_r1*Hreactant1)+(Hmol_r2*Hreactant2))
    return enthalpy

def ENTROPY_of_sys():
    entropy=((Smol_p1*Sproduct1)+(Smol_p2*Sproduct2))-((Smol_r1*Sreactant1)+(Smol_r2*Sreactant2))
    return entropy

def ENTROPY_of_surr():
    entropy=(-(enthalpy_of_reaction)/(temperature))*1000
    return entropy

def ENTROPY_of_univ():
    entropy=entropy_of_system + entropy_of_surrounding
    return entropy

def FREE_ENERGY():
    free_energy=((mol_p1*product1)+(mol_p2*product2))-((mol_r1*reactant1)+(mol_r2*reactant2))
    return free_energy

print("""
CHEMISTRY FOR ENGINEER
THERMODYNAMICS

[1] ENTHALPY OF THE REACTION
[2.a] ENTROPY OF THE REACTION
2.b] ENTROPY OF THE SURROUNDING
[2.c] ENTROPY OF THE UNIVERSE
[3] Gibbs Free Energy of the Reaction

Which do you want to solve?""")

Choice=str(input("Enter your choice: "))

if Choice=="1":
    print("\nENTHALPY OF THE REACTION")
    print("------------------------------------------")

    print("\nREACTANT A")
    Hmol_r1 = float(input("Number of Moles: "))
    Hreactant1 = float(input("Enthalpy of Formation: "))

    print("\nREACTANT B")
    Hmol_r2 = float(input("Number of Moles: "))
    Hreactant2 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT C")
    Hmol_p1 = float(input("Number of Moles: "))
    Hproduct1 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT D")
    Hmol_p2 = float(input("Number of Moles: "))
    Hproduct2 = float(input("Enthalpy of Formation: "))

    print("------------------------------------------\n")
    if ENTHALPY()<0:
        print("ΔH⊖rxn =", ENTHALPY(), "- Exothermic Reaction")
    else:
        print("ΔH⊖rxn =", ENTHALPY(), "- Endothermic Reaction")

elif Choice=="2.a":
    print("\nENTROPY OF THE REACTION")
    print("------------------------------------------")

    print("\nREACTANT A")
    Smol_r1 = float(input("Number of Moles: "))
    Sreactant1 = float(input("Entropy of Formation: "))

    print("\nREACTANT B")
    Smol_r2 = float(input("Number of Moles: "))
    Sreactant2 = float(input("Entropy of Formation: "))

    print("\nPRODUCT C")
    Smol_p1 = float(input("Number of Moles: "))
    Sproduct1 = float(input("Entropy of Formation: "))

    print("\nPRODUCT D")
    Smol_p2 = float(input("Number of Moles: "))
    Sproduct2 = float(input("Entropy of Formation: "))

    print("------------------------------------------\n")
    print("ΔS⊖rxn=", ENTROPY_of_sys(), "J/K·mol")

elif Choice=="2.b":
    print("\nENTROPY OF THE SURROUNDING")
    print("------------------------------------------")

    print("\nEnthalpy of the Reaction")
    print("\nREACTANT A")
    Hmol_r1 = float(input("Number of Moles: "))
    Hreactant1 = float(input("Enthalpy of Formation: "))

    print("\nREACTANT B")
    Hmol_r2 = float(input("Number of Moles: "))
    Hreactant2 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT C")
    Hmol_p1 = float(input("Number of Moles: "))
    Hproduct1 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT D")
    Hmol_p2 = float(input("Number of Moles: "))
    Hproduct2 = float(input("Enthalpy of Formation: "))

    print("\nEnthalpy of the Reaction: ", ENTHALPY())
    print("------------------------------------------\n")

    enthalpy_of_reaction = ENTHALPY()
    temperature = 298
    print("ΔS⊖surr =", ENTROPY_of_surr(), "J/K·mol")

elif Choice=="2.c":
    print("\nENTROPY OF THE UNIVERSE")
    print("------------------------------------------")

    print("\nEntropy of the System")
    print("\nREACTANT A")
    Smol_r1 = float(input("Number of Moles: "))
    Sreactant1 = float(input("Entropy of Formation: "))

    print("\nREACTANT B")
    Smol_r2 = float(input("Number of Moles: "))
    Sreactant2 = float(input("Entropy of Formation: "))

    print("\nPRODUCT C")
    Smol_p1 = float(input("Number of Moles: "))
    Sproduct1 = float(input("Entropy of Formation: "))

    print("\nPRODUCT D")
    Smol_p2 = float(input("Number of Moles: "))
    Sproduct2 = float(input("Entropy of Formation: "))

    print("\nΔS⊖sys =", ENTROPY_of_sys(), "J/K·mol")
    print("------------------------------------------")

    print("\nEnthalpy of the Reaction")
    print("\nREACTANT A")
    Hmol_r1 = float(input("Number of Moles: "))
    Hreactant1 = float(input("Enthalpy of Formation: "))

    print("\nREACTANT B")
    Hmol_r2 = float(input("Number of Moles: "))
    Hreactant2 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT C")
    Hmol_p1 = float(input("Number of Moles: "))
    Hproduct1 = float(input("Enthalpy of Formation: "))

    print("\nPRODUCT D")
    Hmol_p2 = float(input("Number of Moles: "))
    Hproduct2 = float(input("Enthalpy of Formation: "))

    print("\nEnthalpy of the Reaction: ", ENTHALPY())
    print("------------------------------------------\n")
    enthalpy_of_reaction = ENTHALPY()
    temperature = 298

    print("ΔS⊖surr =", ENTROPY_of_surr(), "J/K·mol")
    print("------------------------------------------\n")

    entropy_of_system = ENTROPY_of_sys()
    entropy_of_surrounding = ENTROPY_of_surr()
    print("ΔS⊖univ =", ENTROPY_of_univ(), "J/K·mol")
    if ENTROPY_of_univ()>=0:
        print("The reaction is Spontaneous at 25°C")
    else:
        print("The reaction is Non-spontaneous at 25°C")

elif Choice=="3":
    print("\nGibbs Free Energy of the Reaction")
    print("------------------------------------------")

    print("\nREACTANT A")
    mol_r1 = float(input("Number of Moles: "))
    reactant1 = float(input("Gibbs Free Energy of Formation: "))

    print("\nREACTANT B")
    mol_r2 = float(input("Number of Moles: "))
    reactant2 = float(input("Gibbs Free Energy of Formation: "))

    print("\nPRODUCT C")
    mol_p1 = float(input("Number of Moles: "))
    product1 = float(input("Gibbs Free Energy of Formation: "))

    print("\nPRODUCT D")
    mol_p2 = float(input("Number of Moles: "))
    product2 = float(input("Gibbs Free Energy of Formation: "))

    print("\nΔG⊖rxn =", FREE_ENERGY(), "kJ/mol")
    if FREE_ENERGY()<0:
        print("Spontaneous Reaction - favours Forward Reaction (more products are present at equilibrium)")
    elif FREE_ENERGY()>0:
        print("Non-spontaneous Reaction - favours Reverse Reaction (more reactants are present at equilibrium)")
    else:
        print("The reaction is at Equilibrium")
