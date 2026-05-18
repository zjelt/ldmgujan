model Circuit_Clignotant
  Modelica.Electrical.Analog.Ideal.IdealDiode LED_Vert(Vknee = 0.3) annotation(
    Placement(visible = true, transformation(origin = {-80, 76}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Ideal.IdealDiode LED_Rouge(Vknee = 0.3) annotation(
    Placement(visible = true, transformation(origin = {60, 76}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R1(R = 220) annotation(
    Placement(visible = true, transformation(origin = {-80, 44}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R4(R = 220) annotation(
    Placement(visible = true, transformation(origin = {60, 46}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R2(R = 2200) annotation(
    Placement(visible = true, transformation(origin = {-30, 44}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Resistor R3(R = 2200) annotation(
    Placement(visible = true, transformation(origin = {12, 46}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Capacitor C1(C = 22e-5) annotation(
    Placement(visible = true, transformation(origin = {-60, 22}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor C2(C = 22e-5) annotation(
    Placement(visible = true, transformation(origin = {34, 24}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.ConstantVoltage Tension(V = 5) annotation(
    Placement(visible = true, transformation(origin = {88, 30}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-10, -36}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Semiconductors.NPN npn annotation(
    Placement(visible = true, transformation(origin = {50, 4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Semiconductors.NPN npn1(useHeatPort = false)  annotation(
    Placement(visible = true, transformation(origin = {-70, -8}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
equation
  connect(npn1.C, R1.n) annotation(
    Line(points = {{-80, -2}, {-80, 34}}, color = {0, 0, 255}));
  connect(C1.p, npn1.C) annotation(
    Line(points = {{-70, 22}, {-80, 22}, {-80, -2}}, color = {0, 0, 255}));
  connect(C1.n, R2.n) annotation(
    Line(points = {{-50, 22}, {-30, 22}, {-30, 34}}, color = {0, 0, 255}));
  connect(R1.p, LED_Vert.n) annotation(
    Line(points = {{-80, 54}, {-80, 66}}, color = {0, 0, 255}));
  connect(C2.p, npn.C) annotation(
    Line(points = {{44, 24}, {60, 24}, {60, 10}}, color = {0, 0, 255}));
  connect(npn.C, R4.n) annotation(
    Line(points = {{60, 10}, {60, 36}}, color = {0, 0, 255}));
  connect(R3.n, C2.n) annotation(
    Line(points = {{12, 36}, {12, 24}, {24, 24}}, color = {0, 0, 255}));
  connect(LED_Rouge.n, R4.p) annotation(
    Line(points = {{60, 66}, {60, 56}}, color = {0, 0, 255}));
  connect(LED_Vert.p, LED_Rouge.p) annotation(
    Line(points = {{-80, 86}, {-80, 92}, {60, 92}, {60, 86}}, color = {0, 0, 255}));
  connect(npn1.E, ground.p) annotation(
    Line(points = {{-80, -14}, {-80, -26}, {-10, -26}}, color = {0, 0, 255}));
  connect(ground.p, npn.E) annotation(
    Line(points = {{-10, -26}, {60, -26}, {60, -2}}, color = {0, 0, 255}));
  connect(Tension.n, ground.p) annotation(
    Line(points = {{88, 20}, {88, -26}, {-10, -26}}, color = {0, 0, 255}));
  connect(npn1.B, R3.n) annotation(
    Line(points = {{-60, -8}, {12, -8}, {12, 36}}, color = {0, 0, 255}));
  connect(npn.B, R2.n) annotation(
    Line(points = {{40, 4}, {-30, 4}, {-30, 34}}, color = {0, 0, 255}));
  connect(R3.p, LED_Rouge.p) annotation(
    Line(points = {{12, 56}, {12, 92}, {60, 92}, {60, 86}}, color = {0, 0, 255}));
  connect(R2.p, LED_Rouge.p) annotation(
    Line(points = {{-30, 54}, {-30, 92}, {60, 92}, {60, 86}}, color = {0, 0, 255}));
  connect(Tension.p, LED_Rouge.p) annotation(
    Line(points = {{88, 40}, {88, 92}, {60, 92}, {60, 86}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "4.0.0")));
end Circuit_Clignotant;
