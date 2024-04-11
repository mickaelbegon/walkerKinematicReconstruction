from walker import BiomechanicsTools

# --- Options --- #
data_path = "data/sujet15/"
kinematic_model_file_path = "temporary.bioMod"
static_trial = f"{data_path}/New Patient Cal 01.c3d"
trials = (
    f"{data_path}/Sujet15_PAS_TS4.c3d",
    f"{data_path}/Sujet15_CAS_GAS1.c3d",
    f"{data_path}/Sujet15_CSS_GAS1.c3d",
    f"{data_path}/Sujet15_PAS_GAS1.c3d",
)




print(kinematic_model_file_path)
print('****')

# --------------- #


def main():
    print(kinematic_model_file_path)
    # Generate the personalized kinematic model
    tools = BiomechanicsTools(
        body_mass=70.4,
        include_upper_body=True,
        shoulder_offset={'R': .135, 'L': .135},
        elbow_width={'R': .095, 'L': .095},
        wrist_width={'R': .060, 'L': .060},
        hand_thickness={'R': .025, 'L': .025},
        leg_length={'R': .99, 'L': .99},
        ankle_width={'R': .065, 'L': .065},
    )
    tools.personalize_model(static_trial, kinematic_model_file_path)

    # Perform some biomechanical computation
    for trial in trials:
        print(trial)
        tools.process_trial(trial, compute_automatic_events=False)

    # TODO: Bioviz vizual bug with the end of the trial when resizing the window
    # TODO: Record a tutorial

if __name__ == "__main__":
    main()