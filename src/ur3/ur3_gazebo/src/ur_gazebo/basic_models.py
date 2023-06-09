SPHERE = '<?xml version="1.0" ?> \
<sdf version="1.5"> \
  <model name="%s"> \
    <static>true</static> \
    <link name="link"> \
      <pose>0 0 0 0 0 0</pose> \
      <visual name="visual"> \
        <transparency> 0.5 </transparency> \
        <geometry> \
          <sphere> \
            <radius>%s</radius> \
          </sphere> \
        </geometry> \
        <material> \
          <script> \
            <uri>model://media/materials/scripts/gazebo.material</uri> \
            <name>Gazebo/%s</name> \
          </script> \
        </material> \
      </visual> \
    </link> \
  </model> \
</sdf>'

SPHERE_COLLISION = '<?xml version="1.0" ?> \
<sdf version="1.5"> \
  <model name="{}"> \
    <static>true</static> \
    <link name="link"> \
      <pose>0 0 0 0 0 0</pose> \
      <visual name="visual"> \
        <transparency> 0.5 </transparency> \
        <geometry> \
          <sphere> \
            <radius>{}</radius> \
          </sphere> \
        </geometry> \
        <material> \
          <script> \
            <uri>model://media/materials/scripts/gazebo.material</uri> \
            <name>Gazebo/{}</name> \
          </script> \
        </material> \
      </visual> \
      <collision name="collision"> \
        <pose frame=''>0 0 0 0 0 0</pose> \
        <laser_retro>0</laser_retro> \
        <max_contacts>10</max_contacts> \
        <geometry> \
          <sphere> \
            <radius>{}</radius> \
          </sphere> \
        </geometry> \
        <surface> \
          <friction> \
            <ode> \
              <mu>1</mu> \
              <mu2>1</mu2> \
              <fdir1>0 0 0</fdir1> \
              <slip1>0.1</slip1> \
              <slip2>0.1</slip2> \
            </ode> \
            <torsional> \
              <coefficient>1</coefficient> \
              <patch_radius>0</patch_radius> \
              <surface_radius>0</surface_radius> \
              <use_patch_radius>1</use_patch_radius> \
              <ode> \
                <slip>0</slip> \
              </ode> \
            </torsional> \
          </friction> \
          <bounce> \
            <restitution_coefficient>0</restitution_coefficient> \
            <threshold>1e+06</threshold> \
          </bounce> \
          <contact> \
            <collide_without_contact>0</collide_without_contact> \
            <collide_without_contact_bitmask>1</collide_without_contact_bitmask> \
            <collide_bitmask>1</collide_bitmask> \
            <ode> \
              <kp>{}</kp> \
              <kd>1</kd> \
              <max_vel>0.01</max_vel> \
              <min_depth>0</min_depth> \
            </ode> \
          </contact> \
        </surface> \
      </collision> \
    </link> \
  </model> \
</sdf>'

BOX = '<?xml version="1.0" ?> \
<sdf version="1.5"> \
  <model name="%s"> \
    <static>true</static> \
    <link name="link"> \
      <pose>0 0 0 0 0 0</pose> \
      <visual name="visual"> \
        <transparency> 0.2 </transparency> \
        <geometry> \
          <box> \
            <size>%s %s %s</size> \
          </box> \
        </geometry> \
        <material> \
          <script> \
            <uri>model://media/materials/scripts/gazebo.material</uri> \
            <name>Gazebo/%s</name> \
          </script> \
        </material> \
      </visual> \
      <collision name="boxcollision"> \
        <pose frame=''>0 0 0 0 0 0</pose> \
        <laser_retro>0</laser_retro> \
        <max_contacts>10</max_contacts> \
        <geometry> \
          <box> \
            <size>%s %s %s</size> \
          </box> \
        </geometry> \
        <surface> \
          <friction> \
            <ode> \
              <mu>1</mu> \
              <mu2>1</mu2> \
              <fdir1>0 0 0</fdir1> \
              <slip1>0.1</slip1> \
              <slip2>0.1</slip2> \
            </ode> \
            <torsional> \
              <coefficient>1</coefficient> \
              <patch_radius>0</patch_radius> \
              <surface_radius>0</surface_radius> \
              <use_patch_radius>1</use_patch_radius> \
              <ode> \
                <slip>0</slip> \
              </ode> \
            </torsional> \
          </friction> \
          <bounce> \
            <restitution_coefficient>0</restitution_coefficient> \
            <threshold>1e+06</threshold> \
          </bounce> \
          <contact> \
            <collide_without_contact>0</collide_without_contact> \
            <collide_without_contact_bitmask>1</collide_without_contact_bitmask> \
            <collide_bitmask>1</collide_bitmask> \
            <ode> \
              <kp>1e5</kp> \
              <kd>1</kd> \
              <max_vel>0.01</max_vel> \
              <min_depth>0</min_depth> \
            </ode> \
          </contact> \
        </surface> \
      </collision> \
    </link> \
    <static>1</static> \
  </model> \
</sdf>'

PEG_BOARD = "<?xml version='1.0'?> \
<sdf version='1.6'> \
  <model name='simple_peg_board'> \
    <static>true</static> \
    <link name='board'> \
      <pose frame=''>0.0 0.0 -0.01 1.5707 0 0</pose> \
      <self_collide>0</self_collide> \
      <kinematic>0</kinematic> \
      <gravity>0</gravity> \
      <inertial> \
        <mass>1</mass> \
        <pose frame=''>0 0 0 0 0 0</pose> \
        <inertia> \
          <ixx>0.999223</ixx> \
          <ixy>0.039421</ixy> \
          <ixz>0.000141</ixz> \
          <iyy>0.999222</iyy> \
          <iyz>-0.001474</iyz> \
          <izz>0.999999</izz> \
        </inertia> \
      </inertial> \
      <visual name='visual'> \
        <transparency> {} </transparency> \
        <pose frame=''>0 0 0 0 0 0</pose> \
        <geometry> \
          <mesh> \
            <uri>model://simple_peg_board/meshes/simple_board.dae</uri> \
              <scale>0.97 0.97 0.97</scale> \
          </mesh> \
        </geometry> \
        <material> \
          <ambient>0 0 0 1</ambient> \
          <diffuse>0 0 0 1</diffuse> \
          <specular>0 0 0 0</specular> \
          <emissive>{} {} {} 1</emissive> \
        </material> \
        <transparency>0</transparency> \
        <cast_shadows>1</cast_shadows> \
      </visual> \
      <collision name='collision'> \
        <pose frame=''>0 0 0 0 0 0</pose> \
        <laser_retro>0</laser_retro> \
        <max_contacts>10</max_contacts> \
        <geometry> \
          <mesh> \
            <uri>model://simple_peg_board/meshes/simple_board.dae</uri> \
            <scale>0.97 0.97 0.97</scale> \
          </mesh> \
        </geometry> \
        <surface> \
          <friction> \
            <ode> \
              <mu>1</mu> \
              <mu2>1</mu2> \
              <fdir1>0 0 0</fdir1> \
              <slip1>0.1</slip1> \
              <slip2>0.1</slip2> \
            </ode> \
            <torsional> \
              <coefficient>1</coefficient> \
              <patch_radius>0</patch_radius> \
              <surface_radius>0</surface_radius> \
              <use_patch_radius>1</use_patch_radius> \
              <ode> \
                <slip>0</slip> \
              </ode> \
            </torsional> \
          </friction> \
          <bounce> \
            <restitution_coefficient>0</restitution_coefficient> \
            <threshold>1e+06</threshold> \
          </bounce> \
          <contact> \
            <collide_without_contact>0</collide_without_contact> \
            <collide_without_contact_bitmask>1</collide_without_contact_bitmask> \
            <collide_bitmask>1</collide_bitmask> \
            <ode> \
              <kp>{}</kp> \
              <kd>1</kd> \
              <max_vel>0.01</max_vel> \
              <min_depth>0</min_depth> \
            </ode> \
          </contact> \
        </surface> \
      </collision> \
    </link> \
    <static>1</static> \
    <allow_auto_disable>1</allow_auto_disable> \
  </model> \
</sdf>"