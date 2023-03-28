REGION
Rail

"DbMSAI00LV03".Parameters.StartPositionX := 1; // ERM
0; // 1; // 1;
"DbMSAI00LV03".Parameters.PositionsConfiguredX := UINT_TO_INT("MSAI00LV03_BIN_POSITION_COUNT");
"DbMSAI00LV03".Parameters.OffsetPositionsX := 0; // -1; // 0; // 3;
# tempOffsetPositionX := "DbMSAI00LV03".Parameters.OffsetPositionsX; //1;
IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".Parameters.LimitUpperX_mm := 100000; // 64890;
(Before changing the bay size)
ELSE
"DbMSAI00LV03".Parameters.LimitUpperX_mm := 100000;
END_IF;
"DbMSAI00LV03".Parameters.LimitLowerX_mm := 0;

END_REGION

REGION
Left
Racks

"DbMSAI00LV03".Port1RackConveyors[1].Name := "instMSAI00LL03RI10".outParameters.Group.Name;
"DbMSAI00LV03".Port1RackConveyors[1].NameHash := "instMSAI00LL03RI10".outParameters.Group.NameHash;
"DbMSAI00LV03".Port1RackConveyors[1].InnerEdgeAlign := FALSE;
"DbMSAI00LV03".Port1RackConveyors[1].RackType :=  # enumRackType.Inbound;
"DbMSAI00LV03".Port1RackConveyors[1].Side := USINT_TO_SINT(  # enumSide.Left);
    "DbMSAI00LV03".Port1RackConveyors[1].TemplateId := 1;
"DbMSAI00LV03".Port1RackConveyors[1].RackConveyorOnLiftSide1 := FALSE;
"DbMSAI00LV03".Port1RackConveyors[1].OffsetZExtraDepth_mm := 1;
"DbMSAI00LV03".Port1RackConveyors[1].PositionX := 1; // ERM
0; // 1; // -1;

END_REGION

REGION
Left
Bays

"DbMSAI00LV03".Port1Bays[1].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[1].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[1].FirstPositionX := 2; // ERM
1;
"DbMSAI00LV03".Port1Bays[1].FirstPositionXToUpright_mm := 295; // mayesbd - TODO
verify
at
site

"DbMSAI00LV03".Port1Bays[2].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[2].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[2].FirstPositionX := 6; // ERM
5;
"DbMSAI00LV03".Port1Bays[2].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[3].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[3].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[3].FirstPositionX := 10; // ERM
9;
"DbMSAI00LV03".Port1Bays[3].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[4].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[4].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[4].FirstPositionX := 14; // ERM
13;
"DbMSAI00LV03".Port1Bays[4].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[5].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[5].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[5].FirstPositionX := 18; // ERM
17;
"DbMSAI00LV03".Port1Bays[5].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[6].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[6].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[6].FirstPositionX := 22; // ERM
21;
"DbMSAI00LV03".Port1Bays[6].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[7].TemplateId := 6;
"DbMSAI00LV03".Port1Bays[7].BayBlockageTemplateId := 6;
"DbMSAI00LV03".Port1Bays[7].FirstPositionX := 26; // ERM
25;
"DbMSAI00LV03".Port1Bays[7].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[8].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[8].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[8].FirstPositionX := 29; // ERM
28;
"DbMSAI00LV03".Port1Bays[8].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[9].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[9].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[9].FirstPositionX := 33; // ERM
32;
"DbMSAI00LV03".Port1Bays[9].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[10].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[10].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[10].FirstPositionX := 37; // ERM
36;
"DbMSAI00LV03".Port1Bays[10].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[11].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[11].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[11].FirstPositionX := 41; // ERM
40;
"DbMSAI00LV03".Port1Bays[11].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[12].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[12].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[12].FirstPositionX := 45; // ERM
44;
"DbMSAI00LV03".Port1Bays[12].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[13].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[13].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[13].FirstPositionX := 49; // ERM
48;
"DbMSAI00LV03".Port1Bays[13].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[14].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[14].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[14].FirstPositionX := 53; // ERM
52;
"DbMSAI00LV03".Port1Bays[14].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[15].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[15].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[15].FirstPositionX := 57; // ERM
56;
"DbMSAI00LV03".Port1Bays[15].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[16].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[16].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[16].FirstPositionX := 61; // ERM
60;
"DbMSAI00LV03".Port1Bays[16].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[17].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[17].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[17].FirstPositionX := 65; // ERM
64;
"DbMSAI00LV03".Port1Bays[17].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[18].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[18].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[18].FirstPositionX := 69; // ERM
68;
"DbMSAI00LV03".Port1Bays[18].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[19].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[19].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[19].FirstPositionX := 73; // ERM
72;
"DbMSAI00LV03".Port1Bays[19].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[20].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[20].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[20].FirstPositionX := 77; // ERM
76;
"DbMSAI00LV03".Port1Bays[20].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[21].TemplateId := 6;
"DbMSAI00LV03".Port1Bays[21].BayBlockageTemplateId := 6;
"DbMSAI00LV03".Port1Bays[21].FirstPositionX := 81; // ERM
80;
"DbMSAI00LV03".Port1Bays[21].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[22].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[22].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[22].FirstPositionX := 84; // ERM
83;
"DbMSAI00LV03".Port1Bays[22].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[23].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[23].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[23].FirstPositionX := 88; // ERM
87;
"DbMSAI00LV03".Port1Bays[23].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port1Bays[24].TemplateId := 5;
"DbMSAI00LV03".Port1Bays[24].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port1Bays[24].FirstPositionX := 92; // ERM
91;
"DbMSAI00LV03".Port1Bays[24].FirstPositionXToUpright_mm := 295;

END_REGION

REGION
Right
Racks

"DbMSAI00LV03".Port2RackConveyors[1].Name := "instMSAI00LL03RO10".outParameters.Group.Name;
"DbMSAI00LV03".Port2RackConveyors[1].NameHash := "instMSAI00LL03RO10".outParameters.Group.NameHash;
"DbMSAI00LV03".Port2RackConveyors[1].InnerEdgeAlign := FALSE;
"DbMSAI00LV03".Port2RackConveyors[1].RackType :=  # enumRackType.Outbound;
"DbMSAI00LV03".Port2RackConveyors[1].Side := USINT_TO_SINT(  # enumSide.Right);
    "DbMSAI00LV03".Port2RackConveyors[1].TemplateId := 2;
"DbMSAI00LV03".Port2RackConveyors[1].RackConveyorOnLiftSide1 := FALSE;
"DbMSAI00LV03".Port2RackConveyors[1].OffsetZExtraDepth_mm := 1;
"DbMSAI00LV03".Port2RackConveyors[1].PositionX := 1; // ERM
0; // 1; // -1;

END_REGION

REGION
Right
Bays

"DbMSAI00LV03".Port2Bays[1].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[1].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[1].FirstPositionX := 2; // ERM
1;
"DbMSAI00LV03".Port2Bays[1].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[2].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[2].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[2].FirstPositionX := 6; // ERM
5;
"DbMSAI00LV03".Port2Bays[2].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[3].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[3].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[3].FirstPositionX := 10; // ERM
9;
"DbMSAI00LV03".Port2Bays[3].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[4].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[4].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[4].FirstPositionX := 14; // ERM
13;
"DbMSAI00LV03".Port2Bays[4].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[5].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[5].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[5].FirstPositionX := 18; // ERM
17;
"DbMSAI00LV03".Port2Bays[5].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[6].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[6].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[6].FirstPositionX := 22; // ERM
21;
"DbMSAI00LV03".Port2Bays[6].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[7].TemplateId := 6;
"DbMSAI00LV03".Port2Bays[7].BayBlockageTemplateId := 6;
"DbMSAI00LV03".Port2Bays[7].FirstPositionX := 26; // ERM
25;
"DbMSAI00LV03".Port2Bays[7].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[8].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[8].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[8].FirstPositionX := 29; // ERM
28;
"DbMSAI00LV03".Port2Bays[8].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[9].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[9].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[9].FirstPositionX := 33; // ERM
32;
"DbMSAI00LV03".Port2Bays[9].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[10].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[10].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[10].FirstPositionX := 37; // ERM
36;
"DbMSAI00LV03".Port2Bays[10].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[11].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[11].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[11].FirstPositionX := 41; // ERM
40;
"DbMSAI00LV03".Port2Bays[11].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[12].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[12].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[12].FirstPositionX := 45; // ERM
44;
"DbMSAI00LV03".Port2Bays[12].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[13].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[13].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[13].FirstPositionX := 49; // ERM
48;
"DbMSAI00LV03".Port2Bays[13].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[14].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[14].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[14].FirstPositionX := 53; // ERM
52;
"DbMSAI00LV03".Port2Bays[14].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[15].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[15].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[15].FirstPositionX := 57; // ERM
56;
"DbMSAI00LV03".Port2Bays[15].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[16].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[16].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[16].FirstPositionX := 61; // ERM
60;
"DbMSAI00LV03".Port2Bays[16].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[17].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[17].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[17].FirstPositionX := 65; // ERM
64;
"DbMSAI00LV03".Port2Bays[17].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[18].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[18].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[18].FirstPositionX := 69; // ERM
68;
"DbMSAI00LV03".Port2Bays[18].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[19].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[19].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[19].FirstPositionX := 73; // ERM
72;
"DbMSAI00LV03".Port2Bays[19].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[20].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[20].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[20].FirstPositionX := 77; // ERM
76;
"DbMSAI00LV03".Port2Bays[20].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[21].TemplateId := 6;
"DbMSAI00LV03".Port2Bays[21].BayBlockageTemplateId := 6;
"DbMSAI00LV03".Port2Bays[21].FirstPositionX := 81; // ERM
80;
"DbMSAI00LV03".Port2Bays[21].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[22].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[22].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[22].FirstPositionX := 84; // ERM
83;
"DbMSAI00LV03".Port2Bays[22].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[23].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[23].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[23].FirstPositionX := 88; // ERM
87;
"DbMSAI00LV03".Port2Bays[23].FirstPositionXToUpright_mm := 295;

"DbMSAI00LV03".Port2Bays[24].TemplateId := 5;
"DbMSAI00LV03".Port2Bays[24].BayBlockageTemplateId := 5;
"DbMSAI00LV03".Port2Bays[24].FirstPositionX := 92; // ERM
91;
"DbMSAI00LV03".Port2Bays[24].FirstPositionXToUpright_mm := 295;

END_REGION

REGION
Teaching
positions

(* // ERM | TODO: Double
check, this
logic
block
could
be
deleted | position
"0"
isn
't reacheable for shuttles over VER2_1 | RackIn & Out movet to Pos 1
IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Left.Offset_mm := 1367;
                         "DbMSAI00LV03".PositionX[
                             0 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.RackIn;
                             "DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Right.Offset_mm := 1367;
                                                      "DbMSAI00LV03".PositionX[
                                                          0 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.RackOut;
                                                          ELSE
"DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             0 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.RackIn;
                             "DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          0 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.RackOut; 
                                                          END_IF;
"DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Left.BelongsToBay := 0;
                         "DbMSAI00LV03".PositionX[0 +  # tempOffsetPositionX].Right.BelongsToBay := 0; *)

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             1 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.RackIn; //ERM #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          1 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.RackOut; //ERM #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             1 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.RackIn; //ERM #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          1 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.RackOut; //ERM #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Left.BelongsToBay := 0; //ERM 1;
                         "DbMSAI00LV03".PositionX[1 +  # tempOffsetPositionX].Right.BelongsToBay := 0; //ERM 1;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             2 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          2 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             2 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          2 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Left.BelongsToBay := 1;
                         "DbMSAI00LV03".PositionX[2 +  # tempOffsetPositionX].Right.BelongsToBay := 1;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             3 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          3 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             3 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          3 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Left.BelongsToBay := 1;
                         "DbMSAI00LV03".PositionX[3 +  # tempOffsetPositionX].Right.BelongsToBay := 1;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             4 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          4 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             4 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          4 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Left.BelongsToBay := 1;
                         "DbMSAI00LV03".PositionX[4 +  # tempOffsetPositionX].Right.BelongsToBay := 1;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             5 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          5 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             5 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          5 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Left.BelongsToBay := 1; //ERM 2;
                         "DbMSAI00LV03".PositionX[5 +  # tempOffsetPositionX].Right.BelongsToBay := 1; //ERM 2;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             6 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          6 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             6 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          6 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Left.BelongsToBay := 2;
                         "DbMSAI00LV03".PositionX[6 +  # tempOffsetPositionX].Right.BelongsToBay := 2;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             7 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          7 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             7 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          7 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Left.BelongsToBay := 2;
                         "DbMSAI00LV03".PositionX[7 +  # tempOffsetPositionX].Right.BelongsToBay := 2;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             8 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          8 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             8 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          8 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Left.BelongsToBay := 2;
                         "DbMSAI00LV03".PositionX[8 +  # tempOffsetPositionX].Right.BelongsToBay := 2;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             9 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          9 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             9 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          9 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Left.BelongsToBay := 2; //ERM 3;
                         "DbMSAI00LV03".PositionX[9 +  # tempOffsetPositionX].Right.BelongsToBay := 2; //ERM 3;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             10 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          10 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             10 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          10 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Left.BelongsToBay := 3;
                         "DbMSAI00LV03".PositionX[10 +  # tempOffsetPositionX].Right.BelongsToBay := 3;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             11 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          11 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             11 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          11 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Left.BelongsToBay := 3;
                         "DbMSAI00LV03".PositionX[11 +  # tempOffsetPositionX].Right.BelongsToBay := 3;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             12 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          12 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             12 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          12 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Left.BelongsToBay := 3;
                         "DbMSAI00LV03".PositionX[12 +  # tempOffsetPositionX].Right.BelongsToBay := 3;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             13 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          13 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             13 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          13 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Left.BelongsToBay := 3; //ERM 4;
                         "DbMSAI00LV03".PositionX[13 +  # tempOffsetPositionX].Right.BelongsToBay := 3; //ERM 4;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             14 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          14 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             14 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          14 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Left.BelongsToBay := 4;
                         "DbMSAI00LV03".PositionX[14 +  # tempOffsetPositionX].Right.BelongsToBay := 4;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             15 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          15 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             15 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          15 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Left.BelongsToBay := 4;
                         "DbMSAI00LV03".PositionX[15 +  # tempOffsetPositionX].Right.BelongsToBay := 4;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             16 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          16 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             16 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          16 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Left.BelongsToBay := 4;
                         "DbMSAI00LV03".PositionX[16 +  # tempOffsetPositionX].Right.BelongsToBay := 4;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             17 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          17 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             17 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          17 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Left.BelongsToBay := 4; //ERM 5;
                         "DbMSAI00LV03".PositionX[17 +  # tempOffsetPositionX].Right.BelongsToBay := 4; //ERM 5;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             18 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          18 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             18 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          18 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Left.BelongsToBay := 5;
                         "DbMSAI00LV03".PositionX[18 +  # tempOffsetPositionX].Right.BelongsToBay := 5;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             19 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          19 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             19 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          19 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Left.BelongsToBay := 5;
                         "DbMSAI00LV03".PositionX[19 +  # tempOffsetPositionX].Right.BelongsToBay := 5;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             20 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          20 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             20 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          20 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Left.BelongsToBay := 5;
                         "DbMSAI00LV03".PositionX[20 +  # tempOffsetPositionX].Right.BelongsToBay := 5;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             21 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          21 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             21 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          21 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Left.BelongsToBay := 5; //ERM 6;
                         "DbMSAI00LV03".PositionX[21 +  # tempOffsetPositionX].Right.BelongsToBay := 5; //ERM 6;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             22 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          22 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             22 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          22 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Left.BelongsToBay := 6;
                         "DbMSAI00LV03".PositionX[22 +  # tempOffsetPositionX].Right.BelongsToBay := 6;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             23 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          23 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             23 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          23 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Left.BelongsToBay := 6;
                         "DbMSAI00LV03".PositionX[23 +  # tempOffsetPositionX].Right.BelongsToBay := 6;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             24 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          24 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             24 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          24 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Left.BelongsToBay := 6;
                         "DbMSAI00LV03".PositionX[24 +  # tempOffsetPositionX].Right.BelongsToBay := 6;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             25 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          25 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             25 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          25 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Left.BelongsToBay := 6; //ERM 7;
                         "DbMSAI00LV03".PositionX[25 +  # tempOffsetPositionX].Right.BelongsToBay := 6; //ERM 7;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             26 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          26 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             26 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          26 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Left.BelongsToBay := 7;
                         "DbMSAI00LV03".PositionX[26 +  # tempOffsetPositionX].Right.BelongsToBay := 7;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             27 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          27 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             27 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          27 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Left.BelongsToBay := 7;
                         "DbMSAI00LV03".PositionX[27 +  # tempOffsetPositionX].Right.BelongsToBay := 7;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             28 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          28 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             28 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          28 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Left.BelongsToBay := 7; //ERM 8;
                         "DbMSAI00LV03".PositionX[28 +  # tempOffsetPositionX].Right.BelongsToBay := 7; //ERM 8;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             29 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          29 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             29 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          29 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Left.BelongsToBay := 8;
                         "DbMSAI00LV03".PositionX[29 +  # tempOffsetPositionX].Right.BelongsToBay := 8;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             30 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          30 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             30 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          30 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Left.BelongsToBay := 8;
                         "DbMSAI00LV03".PositionX[30 +  # tempOffsetPositionX].Right.BelongsToBay := 8;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             31 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          31 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             31 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          31 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Left.BelongsToBay := 8;
                         "DbMSAI00LV03".PositionX[31 +  # tempOffsetPositionX].Right.BelongsToBay := 8;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             32 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          32 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             32 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          32 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Left.BelongsToBay := 8; //ERM 9;
                         "DbMSAI00LV03".PositionX[32 +  # tempOffsetPositionX].Right.BelongsToBay := 8; //ERM 9;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             33 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          33 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             33 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          33 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Left.BelongsToBay := 9;
                         "DbMSAI00LV03".PositionX[33 +  # tempOffsetPositionX].Right.BelongsToBay := 9;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             34 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          34 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             34 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          34 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Left.BelongsToBay := 9;
                         "DbMSAI00LV03".PositionX[34 +  # tempOffsetPositionX].Right.BelongsToBay := 9;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             35 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          35 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             35 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          35 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Left.BelongsToBay := 9;
                         "DbMSAI00LV03".PositionX[35 +  # tempOffsetPositionX].Right.BelongsToBay := 9;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             36 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          36 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             36 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          36 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Left.BelongsToBay := 9; //ERM 10;
                         "DbMSAI00LV03".PositionX[36 +  # tempOffsetPositionX].Right.BelongsToBay := 9; //ERM 10;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             37 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          37 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             37 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          37 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Left.BelongsToBay := 10;
                         "DbMSAI00LV03".PositionX[37 +  # tempOffsetPositionX].Right.BelongsToBay := 10;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             38 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          38 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             38 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          38 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Left.BelongsToBay := 10;
                         "DbMSAI00LV03".PositionX[38 +  # tempOffsetPositionX].Right.BelongsToBay := 10;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             39 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          39 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             39 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          39 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Left.BelongsToBay := 10;
                         "DbMSAI00LV03".PositionX[39 +  # tempOffsetPositionX].Right.BelongsToBay := 10;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             40 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          40 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             40 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          40 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Left.BelongsToBay := 10; //ERM 11;
                         "DbMSAI00LV03".PositionX[40 +  # tempOffsetPositionX].Right.BelongsToBay := 10; //ERM 11;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             41 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          41 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             41 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          41 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Left.BelongsToBay := 11;
                         "DbMSAI00LV03".PositionX[41 +  # tempOffsetPositionX].Right.BelongsToBay := 11;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             42 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          42 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             42 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          42 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Left.BelongsToBay := 11;
                         "DbMSAI00LV03".PositionX[42 +  # tempOffsetPositionX].Right.BelongsToBay := 11;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             43 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          43 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             43 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          43 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Left.BelongsToBay := 11;
                         "DbMSAI00LV03".PositionX[43 +  # tempOffsetPositionX].Right.BelongsToBay := 11;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             44 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          44 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             44 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          44 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Left.BelongsToBay := 11; //ERM 12;
                         "DbMSAI00LV03".PositionX[44 +  # tempOffsetPositionX].Right.BelongsToBay := 11; //ERM 12;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             45 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          45 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             45 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          45 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Left.BelongsToBay := 12;
                         "DbMSAI00LV03".PositionX[45 +  # tempOffsetPositionX].Right.BelongsToBay := 12;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             46 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          46 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             46 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          46 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Left.BelongsToBay := 12;
                         "DbMSAI00LV03".PositionX[46 +  # tempOffsetPositionX].Right.BelongsToBay := 12;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             47 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          47 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             47 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          47 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Left.BelongsToBay := 12;
                         "DbMSAI00LV03".PositionX[47 +  # tempOffsetPositionX].Right.BelongsToBay := 12;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             48 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          48 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             48 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          48 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Left.BelongsToBay := 12; //ERM 13;
                         "DbMSAI00LV03".PositionX[48 +  # tempOffsetPositionX].Right.BelongsToBay := 12; //ERM 13;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             49 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          49 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             49 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          49 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Left.BelongsToBay := 13;
                         "DbMSAI00LV03".PositionX[49 +  # tempOffsetPositionX].Right.BelongsToBay := 13;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             50 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          50 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             50 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          50 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Left.BelongsToBay := 13;
                         "DbMSAI00LV03".PositionX[50 +  # tempOffsetPositionX].Right.BelongsToBay := 13;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             51 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          51 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             51 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          51 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Left.BelongsToBay := 13;
                         "DbMSAI00LV03".PositionX[51 +  # tempOffsetPositionX].Right.BelongsToBay := 13;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             52 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          52 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             52 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          52 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Left.BelongsToBay := 13; //ERM 14;
                         "DbMSAI00LV03".PositionX[52 +  # tempOffsetPositionX].Right.BelongsToBay := 13; //ERM 14;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             53 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          53 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             53 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          53 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Left.BelongsToBay := 14;
                         "DbMSAI00LV03".PositionX[53 +  # tempOffsetPositionX].Right.BelongsToBay := 14;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             54 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          54 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             54 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          54 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Left.BelongsToBay := 14;
                         "DbMSAI00LV03".PositionX[54 +  # tempOffsetPositionX].Right.BelongsToBay := 14;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             55 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          55 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             55 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          55 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Left.BelongsToBay := 14;
                         "DbMSAI00LV03".PositionX[55 +  # tempOffsetPositionX].Right.BelongsToBay := 14;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             56 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          56 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             56 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          56 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Left.BelongsToBay := 14; //ERM 15;
                         "DbMSAI00LV03".PositionX[56 +  # tempOffsetPositionX].Right.BelongsToBay := 14; //ERM 15;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             57 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          57 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             57 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          57 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Left.BelongsToBay := 15;
                         "DbMSAI00LV03".PositionX[57 +  # tempOffsetPositionX].Right.BelongsToBay := 15;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             58 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          58 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             58 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          58 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Left.BelongsToBay := 15;
                         "DbMSAI00LV03".PositionX[58 +  # tempOffsetPositionX].Right.BelongsToBay := 15;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             59 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          59 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             59 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          59 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Left.BelongsToBay := 15;
                         "DbMSAI00LV03".PositionX[59 +  # tempOffsetPositionX].Right.BelongsToBay := 15;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             60 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          60 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             60 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          60 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Left.BelongsToBay := 15; //ERM 16;
                         "DbMSAI00LV03".PositionX[60 +  # tempOffsetPositionX].Right.BelongsToBay := 15; //ERM 16;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             61 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          61 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             61 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          61 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Left.BelongsToBay := 16;
                         "DbMSAI00LV03".PositionX[61 +  # tempOffsetPositionX].Right.BelongsToBay := 16;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             62 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          62 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             62 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          62 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Left.BelongsToBay := 16;
                         "DbMSAI00LV03".PositionX[62 +  # tempOffsetPositionX].Right.BelongsToBay := 16;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             63 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          63 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             63 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          63 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Left.BelongsToBay := 16;
                         "DbMSAI00LV03".PositionX[63 +  # tempOffsetPositionX].Right.BelongsToBay := 16;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             64 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          64 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             64 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          64 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Left.BelongsToBay := 16; //ERM 17;
                         "DbMSAI00LV03".PositionX[64 +  # tempOffsetPositionX].Right.BelongsToBay := 16; //ERM 17;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             65 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          65 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             65 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          65 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Left.BelongsToBay := 17;
                         "DbMSAI00LV03".PositionX[65 +  # tempOffsetPositionX].Right.BelongsToBay := 17;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             66 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          66 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             66 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          66 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Left.BelongsToBay := 17;
                         "DbMSAI00LV03".PositionX[66 +  # tempOffsetPositionX].Right.BelongsToBay := 17;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             67 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          67 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             67 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          67 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Left.BelongsToBay := 17;
                         "DbMSAI00LV03".PositionX[67 +  # tempOffsetPositionX].Right.BelongsToBay := 17;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             68 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          68 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             68 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          68 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Left.BelongsToBay := 17; //ERM 18;
                         "DbMSAI00LV03".PositionX[68 +  # tempOffsetPositionX].Right.BelongsToBay := 17; //ERM 18;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             69 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          69 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             69 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          69 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Left.BelongsToBay := 18;
                         "DbMSAI00LV03".PositionX[69 +  # tempOffsetPositionX].Right.BelongsToBay := 18;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             70 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          70 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             70 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          70 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Left.BelongsToBay := 18;
                         "DbMSAI00LV03".PositionX[70 +  # tempOffsetPositionX].Right.BelongsToBay := 18;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             71 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          71 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             71 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          71 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Left.BelongsToBay := 18;
                         "DbMSAI00LV03".PositionX[71 +  # tempOffsetPositionX].Right.BelongsToBay := 18;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             72 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          72 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             72 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          72 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Left.BelongsToBay := 18; //ERM 19;
                         "DbMSAI00LV03".PositionX[72 +  # tempOffsetPositionX].Right.BelongsToBay := 18; //ERM 19;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             73 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          73 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             73 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          73 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Left.BelongsToBay := 19;
                         "DbMSAI00LV03".PositionX[73 +  # tempOffsetPositionX].Right.BelongsToBay := 19;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             74 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          74 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             74 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          74 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Left.BelongsToBay := 19;
                         "DbMSAI00LV03".PositionX[74 +  # tempOffsetPositionX].Right.BelongsToBay := 19;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             75 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          75 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             75 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          75 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Left.BelongsToBay := 19;
                         "DbMSAI00LV03".PositionX[75 +  # tempOffsetPositionX].Right.BelongsToBay := 19;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             76 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          76 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             76 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          76 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Left.BelongsToBay := 19; //ERM 20;
                         "DbMSAI00LV03".PositionX[76 +  # tempOffsetPositionX].Right.BelongsToBay := 19; //ERM 20;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             77 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          77 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             77 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          77 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Left.BelongsToBay := 20;
                         "DbMSAI00LV03".PositionX[77 +  # tempOffsetPositionX].Right.BelongsToBay := 20;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             78 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          78 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             78 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          78 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Left.BelongsToBay := 20;
                         "DbMSAI00LV03".PositionX[78 +  # tempOffsetPositionX].Right.BelongsToBay := 20;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             79 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          79 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             79 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          79 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Left.BelongsToBay := 20;
                         "DbMSAI00LV03".PositionX[79 +  # tempOffsetPositionX].Right.BelongsToBay := 20;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             80 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          80 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             80 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          80 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Left.BelongsToBay := 20; //ERM 21;
                         "DbMSAI00LV03".PositionX[80 +  # tempOffsetPositionX].Right.BelongsToBay := 20; //ERM 21;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             81 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          81 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             81 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          81 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Left.BelongsToBay := 21;
                         "DbMSAI00LV03".PositionX[81 +  # tempOffsetPositionX].Right.BelongsToBay := 21;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             82 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          82 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             82 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          82 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Left.BelongsToBay := 21;
                         "DbMSAI00LV03".PositionX[82 +  # tempOffsetPositionX].Right.BelongsToBay := 21;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             83 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          83 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             83 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          83 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Left.BelongsToBay := 21; //ERM 22;
                         "DbMSAI00LV03".PositionX[83 +  # tempOffsetPositionX].Right.BelongsToBay := 21; //ERM 22;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             84 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          84 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             84 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          84 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Left.BelongsToBay := 22;
                         "DbMSAI00LV03".PositionX[84 +  # tempOffsetPositionX].Right.BelongsToBay := 22;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             85 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          85 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             85 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          85 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Left.BelongsToBay := 22;
                         "DbMSAI00LV03".PositionX[85 +  # tempOffsetPositionX].Right.BelongsToBay := 22;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             86 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          86 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             86 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          86 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Left.BelongsToBay := 22;
                         "DbMSAI00LV03".PositionX[86 +  # tempOffsetPositionX].Right.BelongsToBay := 22;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             87 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          87 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             87 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          87 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Left.BelongsToBay := 22; //ERM 23;
                         "DbMSAI00LV03".PositionX[87 +  # tempOffsetPositionX].Right.BelongsToBay := 22; //ERM 23;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             88 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          88 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             88 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          88 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Left.BelongsToBay := 23;
                         "DbMSAI00LV03".PositionX[88 +  # tempOffsetPositionX].Right.BelongsToBay := 23;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             89 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          89 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             89 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          89 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Left.BelongsToBay := 23;
                         "DbMSAI00LV03".PositionX[89 +  # tempOffsetPositionX].Right.BelongsToBay := 23;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             90 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          90 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             90 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          90 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Left.BelongsToBay := 23;
                         "DbMSAI00LV03".PositionX[90 +  # tempOffsetPositionX].Right.BelongsToBay := 23;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             91 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          91 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             91 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          91 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Left.BelongsToBay := 23; //ERM 24;
                         "DbMSAI00LV03".PositionX[91 +  # tempOffsetPositionX].Right.BelongsToBay := 23; //ERM 24;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             92 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          92 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             92 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          92 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Left.BelongsToBay := 24;
                         "DbMSAI00LV03".PositionX[92 +  # tempOffsetPositionX].Right.BelongsToBay := 24;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             93 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          93 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             93 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          93 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Left.BelongsToBay := 24;
                         "DbMSAI00LV03".PositionX[93 +  # tempOffsetPositionX].Right.BelongsToBay := 24;

                                                  IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             94 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          94 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             94 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          94 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Left.BelongsToBay := 24;
                         "DbMSAI00LV03".PositionX[94 +  # tempOffsetPositionX].Right.BelongsToBay := 24;

                         // ERM | 95
Bin
Position
added
IF("InstMSC01".outEmulationMode)
THEN
"DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             95 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          95 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          ELSE
"DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Left.Offset_mm := 0;
                         "DbMSAI00LV03".PositionX[
                             95 +  # tempOffsetPositionX].Left.LocationType := #enumLocationType.Bin;
                             "DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Right.Offset_mm := 0;
                                                      "DbMSAI00LV03".PositionX[
                                                          95 +  # tempOffsetPositionX].Right.LocationType := #enumLocationType.Bin;
                                                          END_IF;
"DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Left.BelongsToBay := 24;
                         "DbMSAI00LV03".PositionX[95 +  # tempOffsetPositionX].Right.BelongsToBay := 24;

                                                  END_REGION

REGION
Shuttle
Hash
Table

REGION
Set
temp
variables
# tempHashIndex := 0;
# tempPort1Index := 0;
# tempPort2Index := 0;
# tempElementSize := DINT_TO_INT(UPPER_BOUND(ARR := #inoutHashTableElements, DIM := 1));
END_REGION

// Reset
Hash
Elements
FOR  # tempIndex := 1 TO #tempElementSize DO
# inoutHashTableElements[#tempIndex] := #tempHashElement;
END_FOR;

REGION
Port
1
Racks

REGION
MSAI00LL03RI10
# tempHashIndex += 1;

# tempHashElement.NameHash := "instMSAI00LL03RI10".outParameters.Group.NameHash;
# tempHashElement.PortNumber := 1;

IF  # tempHashElement.PortNumber = #enumSide.Left THEN
# tempPort1Index += 1;
# tempHashElement.Index := #tempPort1Index;
ELSE
# tempPort2Index += 1;
# tempHashElement.Index := #tempPort2Index;
END_IF;

# inoutHashTableElements[#tempHashIndex] := #tempHashElement;
END_REGION

END_REGION

REGION
Port
2
Racks

REGION
MSAI00LL03RO10
# tempHashIndex += 1;

# tempHashElement.NameHash := "instMSAI00LL03RO10".outParameters.Group.NameHash;
# tempHashElement.PortNumber := 2;

IF  # tempHashElement.PortNumber = #enumSide.Left THEN
# tempPort1Index += 1;
# tempHashElement.Index := #tempPort1Index;
ELSE
# tempPort2Index += 1;
# tempHashElement.Index := #tempPort2Index;
END_IF;

# inoutHashTableElements[#tempHashIndex] := #tempHashElement;
END_REGION

END_REGION

REGION
Sorting
Hash
"HashingElementTableSortShuttle"(inHashTableTailIndex :=  # tempHashIndex,
                                 outError = >  # tempError,
inoutHashTableElements :=  # inoutHashTableElements);

END_REGION

REGION
Get
start
index
of
RO
"ShuttleGetHashROStartIndex"(inHashTableTailIndex :=  # tempHashIndex,
                             outError = >  # tempError,
inoutROStartIndex :=  # inoutHashTableROStartIndex,
inHashTableElements :=  # inoutHashTableElements);

END_REGION

END_REGION

REGION
Shuttle
Routing
Table

// This is needed
so
we
can
process
missions
from Bin -> DS
on
the
shuttle
"DbMSAI00LV03SH10RoutingTable".DS[1].RackConveyorHash := "instMSAI00LL03RO10".outParameters.Group.NameHash;
"DbMSAI00LV03SH10RoutingTable".DS[1].Side :=  # enumSide.Right;
"DbMSAI00LV03SH10RoutingTable".DS[1].Hash := "InstMSAI00CR01DS10".outParameters.Group.NameHash;

END_REGION

REGION
SSBC

(*NOT
TO
BE
GENERATED
FOR
NOW
// This
mm
value is the
distance
between
index
1 and index
2
"DbMSAI00LV03".PositionX[1].PreConfiguredDistance_mm := 0;
// This
mm
value is the
distance
between
index
2 and index
3
"DbMSAI00LV03".PositionX[2].PreConfiguredDistance_mm := 0;
// This
mm
value is the
distance
between
index
3 and index
4
"DbMSAI00LV03".PositionX[3].PreConfiguredDistance_mm := 0;
// Continue
populating
preconfigured
locations
up
to
max
X
locations
for this level
         *)

END_REGION

REGION External Conveyor Screens

// TODO: Generate
according
to
layout
for each external conveyor screen

END_REGION
