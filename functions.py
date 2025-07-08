# Input types: bool, int, float, str, Tuple, List, choice, none
# Output types: Optional, Dict, List, Tuple, none
# When the output can be an image or none, use: Optional[np.ndarray]

functions = {
    "control": {
        "arm": {
            "set_position": {
                "inputs": {
                    "shoulder_deg": "Any",
                    "elbow_deg": "Any",
                    "wrist_deg": "Any"
                },
                "output": "NoneType"
            },
            "set_shoulder_position": {
                "inputs": {
                    "shoulder_deg": "Any"
                },
                "output": "NoneType"
            },
            "set_elbow_position": {
                "inputs": {
                    "elbow_deg": "Any"
                },
                "output": "NoneType"
            },
            "set_wrist_position": {
                "inputs": {
                    "wrist_deg": "Any"
                },
                "output": "NoneType"
            },
            "move_shoulder_left": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_shoulder_right": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_shoulder_up": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_shoulder_down": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_elbow_left": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_elbow_right": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_elbow_up": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_elbow_down": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_right": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_left": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_down": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_up": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_roll_right": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "move_wrist_roll_left": {
                "inputs": {
                    "degrees": "Any"
                },
                "output": "NoneType"
            },
            "get_shoulder_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_elbow_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_wrist_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "reset": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "head": {
            "move_right": {
                "inputs": {
                    "degrees": "Any",
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "move_left": {
                "inputs": {
                    "degrees": "Any",
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "move_down": {
                "inputs": {
                    "degrees": "Any",
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "move_up": {
                "inputs": {
                    "degrees": "Any",
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "get_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "reset": {
                "inputs": {
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "rotate_head_value": {
                "inputs": {
                    "angle_yaw": "Any",
                    "angle_pitch": "Any",
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "predefined_gaze": {
                "inputs": {},
                "output": "NoneType"
            },
            "gaze_once": {
                "inputs": {
                    "x": "Any",
                    "y": "Any",
                    "z": "Any",
                    "origin_frame": "Any"
                },
                "output": "NoneType"
            },
            "start_gaze": {
                "inputs": {
                    "point": "Any",
                    "frame": "Any",
                    "origin_frame": "Any"
                },
                "output": "NoneType"
            },
            "stop_gaze": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "pal_gripper": {
            "set_position": {
                "inputs": {
                    "left_gripper": "Any",
                    "right_gripper": "Any"
                },
                "output": "NoneType"
            },
            "set_position_percentage": {
                "inputs": {
                    "percentage": "Any"
                },
                "output": "NoneType"
            },
            "open": {
                "inputs": {},
                "output": "NoneType"
            },
            "close": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_position_percentage": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "reset": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "robotiq_gripper": {
            "set_position": {
                "inputs": {
                    "value": "Any"
                },
                "output": "NoneType"
            },
            "get_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "open": {
                "inputs": {},
                "output": "NoneType"
            },
            "close": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "torso": {
            "set_position": {
                "inputs": {
                    "position": "Any",
                    "wait": "Any",
                    "timeout": "Any",
                    "bypass_torso_limits": "Any"
                },
                "output": "NoneType"
            },
            "move_up": {
                "inputs": {
                    "distance": "Any",
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "move_down": {
                "inputs": {
                    "distance": "Any",
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "get_position": {
                "inputs": {},
                "output": "NoneType"
            },
            "reset": {
                "inputs": {
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "change_torso_limits": {
                "inputs": {
                    "torso_max": "Any",
                    "torso_min": "Any"
                },
                "output": "NoneType"
            },
            "reset_torso_limits": {
                "inputs": {},
                "output": "NoneType"
            }
        }
    },
    "hri": {
        "hri": {
            "gaze_start": {
                "inputs": {
                    "point": "Any"
                },
                "output": "NoneType"
            },
            "gaze_stop": {
                "inputs": {},
                "output": "NoneType"
            },
            "say": {
                "inputs": {
                    "text": "str"
                },
                "output": "NoneType"
            },
            "say_and_wait": {
                "inputs": {
                    "text": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "set_eyes": {
                "inputs": {
                    "config": "Any"
                },
                "output": "NoneType"
            }
        },
        "tts": {
            "say_words": {
                "inputs": {
                    "words": "Any",
                    "blocking": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            }
        }
    },
    "manipulation": {
        "ManipulationPlanningScene": {
            "add_collision_object": {
                "inputs": {
                    "is_box": "Any",
                    "id": "Any",
                    "collision_dim": "Any",
                    "collision_pose": "Any"
                },
                "output": "NoneType"
            },
            "remove_object_collision": {
                "inputs": {
                    "id": "Any"
                },
                "output": "NoneType"
            },
            "remove_all_objects": {
                "inputs": {},
                "output": "NoneType"
            },
            "remove_object_collision_allowance": {
                "inputs": {
                    "id": "Any"
                },
                "output": "NoneType"
            },
            "attach_object_to_robot": {
                "inputs": {
                    "id": "Any"
                },
                "output": "NoneType"
            },
            "detach_object_from_robot": {
                "inputs": {
                    "id": "Any"
                },
                "output": "NoneType"
            }
        },
        "ManipulationPredefinedMotions": {
            "start_predefined_motion": {
                "inputs": {
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "run_predefined_motion": {
                "inputs": {
                    "motion_name": "Any",
                    "wait": "Any",
                    "run_safely": "Any"
                },
                "output": "NoneType"
            },
            "head_look_around": {
                "inputs": {},
                "output": "NoneType"
            },
            "pregrasp": {
                "inputs": {
                    "pregrasp_name": "Any"
                },
                "output": "NoneType"
            },
            "transporting_position": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "ManipulationUtils": {
            "compute_euler_angles": {
                "inputs": {
                    "approach": "Any",
                    "binormal": "Any",
                    "axis": "Any"
                },
                "output": "NoneType"
            },
            "get_camera_device_info": {
                "inputs": {
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "get_link_pose": {
                "inputs": {
                    "link": "Any",
                    "frame": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "get_segmented_pc2": {
                "inputs": {
                    "object_name": "Any",
                    "camera_device": "Any",
                    "sync_node": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "transform_pointcloud_frame": {
                "inputs": {
                    "pc2": "Any",
                    "frame_id": "Any",
                    "time_for_transform": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            }
        },
        "manipulation": {
            "gpd_result_cb": {
                "inputs": {
                    "msg": "Any"
                },
                "output": "NoneType"
            },
            "manipulation_result_cb": {
                "inputs": {
                    "msg": "Any"
                },
                "output": "NoneType"
            },
            "visual_servoing_cb": {
                "inputs": {
                    "msg": "Any"
                },
                "output": "NoneType"
            },
            "object_result_cb": {
                "inputs": {
                    "msg": "Any"
                },
                "output": "NoneType"
            },
            "start_octomap_service": {
                "inputs": {},
                "output": "NoneType"
            },
            "clear_octomap": {
                "inputs": {},
                "output": "NoneType"
            },
            "gpd": {
                "inputs": {
                    "pregrasp": "Any",
                    "object_pose": "Any",
                    "object_name": "Any",
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "get_gpd_grasps_pose": {
                "inputs": {
                    "object_pose": "Any",
                    "pc2": "Any",
                    "error": "Any"
                },
                "output": "NoneType"
            },
            "init_pick": {
                "inputs": {
                    "pregrasp": "Any",
                    "head_look_around": "Any",
                    "clear_octomap": "Any"
                },
                "output": "NoneType"
            },
            "calculate_pregrasp_pose": {
                "inputs": {
                    "pose": "Any",
                    "distance": "Any"
                },
                "output": "NoneType"
            },
            "moveit": {
                "inputs": {
                    "pregrasp_pose": "Any",
                    "motion_timeout": "Any"
                },
                "output": "NoneType"
            },
            "moveit_cartesian_path": {
                "inputs": {
                    "waypoints": "Any",
                    "motion_timeout": "Any"
                },
                "output": "NoneType"
            },
            "cancel_moveit": {
                "inputs": {},
                "output": "NoneType"
            },
            "visual_servoing": {
                "inputs": {
                    "grasp_pose": "Any",
                    "start": "Any"
                },
                "output": "NoneType"
            },
            "stop_visual_servoing": {
                "inputs": {},
                "output": "NoneType"
            }
        }
    },
    "navigation": {
        "navigation": {
            "distance_estimation": {
                "inputs": {
                    "number_of_points": "Any",
                    "scan_topic": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "approximate_object": {
                "inputs": {
                    "position": "Any",
                    "target_dist": "Any",
                    "safety_margin": "Any",
                    "min_detection_width": "Any",
                    "scan": "Any"
                },
                "output": "NoneType"
            },
            "move_to": {
                "inputs": {
                    "goal": "Any",
                    "wait": "Any",
                    "safe": "Any",
                    "dwa_config": "Any",
                    "navigation_config": "Any",
                    "use_pcl_obstacle_avoidance": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "move_to_pose": {
                "inputs": {
                    "pose": "Any",
                    "wait": "Any",
                    "safe": "Any",
                    "dwa_config": "Any",
                    "navigation_config": "Any",
                    "use_pcl_obstacle_avoidance": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "calculate_dist_two_poses": {
                "inputs": {
                    "pose_w_ref": "Any",
                    "pose_2_w_ref": "Any"
                },
                "output": "NoneType"
            },
            "move_base_relative_angular": {
                "inputs": {
                    "speed": "Any",
                    "angle": "Any"
                },
                "output": "NoneType"
            },
            "move_base_relative_linear": {
                "inputs": {
                    "speed": "Any",
                    "dist": "Any"
                },
                "output": "NoneType"
            },
            "get_nearest_location": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_position_3d": {
                "inputs": {
                    "global_reference_frame": "Any",
                    "robot_reference_frame": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "get_current_pose": {
                "inputs": {
                    "global_reference_frame": "Any",
                    "robot_reference_frame": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "get_available_poses": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_waypoint_pose": {
                "inputs": {
                    "waypoint_name": "Any"
                },
                "output": "NoneType"
            },
            "push_door": {
                "inputs": {
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "stop_movement": {
                "inputs": {},
                "output": "NoneType"
            },
            "restart_movement": {
                "inputs": {
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "check_goal": {
                "inputs": {
                    "wait": "Any",
                    "safe": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "get_navigation_status": {
                "inputs": {
                    "safe": "Any"
                },
                "output": "NoneType"
            },
            "localize_in_location": {
                "inputs": {
                    "location_name": "Any"
                },
                "output": "NoneType"
            },
            "align_with_object": {
                "inputs": {
                    "x": "Any",
                    "y": "Any",
                    "speed": "Any",
                    "wait": "Any"
                },
                "output": "NoneType"
            },
            "clear_costmap": {
                "inputs": {},
                "output": "NoneType"
            },
            "follow_object": {
                "inputs": {
                    "wait": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            }
        },
        "people_following": {
            "dyn_goal": {
                "inputs": {
                    "active": "Any",
                    "object_point_stamped": "Any",
                    "wait": "Any",
                    "dist": "Any",
                    "stop": "Any",
                    "timeout": "Any",
                    "dyn_goal_tf": "Any",
                    "origin_tf": "Any"
                },
                "output": "NoneType"
            },
            "get_dyn_goal_status": {
                "inputs": {},
                "output": "NoneType"
            }
        }
    },
    "perception": {
        "PerceptionFaceRecognition": {
            "getPeopleDetection": {
                "inputs": {
                    "read_record": "Any"
                },
                "output": "NoneType"
            },
            "getImgById": {
                "inputs": {
                    "person_id": "Any"
                },
                "output": "NoneType"
            },
            "genderAndAgeDetection": {
                "inputs": {
                    "person_info": "Any"
                },
                "output": "NoneType"
            },
            "faceAnalysis": {
                "inputs": {
                    "person_id": "Any",
                    "actions": "Any"
                },
                "output": "NoneType"
            },
            "getClosestPersonToCamera": {
                "inputs": {
                    "readAgeGender": "Any"
                },
                "output": "NoneType"
            },
            "getPersonAtTheCenterOfTheCamera": {
                "inputs": {
                    "readAgeGender": "Any",
                    "camera_device": "Any"
                },
                "output": "NoneType"
            }
        },
        "PerceptionManipulation": {
            "visual_servoing_detection": {
                "inputs": {
                    "object_name": "Any",
                    "localizer_instance": "Any",
                    "confidence": "Any",
                    "new_orientation": "Any",
                    "shift_xyz": "Any"
                },
                "output": "NoneType"
            }
        },
        "PerceptionMediapipe": {
            "getMpLandmarks": {
                "inputs": {
                    "option": "Any"
                },
                "output": "NoneType"
            },
            "readMpLandmarks": {
                "inputs": {
                    "option": "Any"
                },
                "output": "NoneType"
            },
            "getMpEstimatedLength": {
                "inputs": {
                    "option": "Any"
                },
                "output": "NoneType"
            },
            "readMpLength": {
                "inputs": {
                    "option": "Any"
                },
                "output": "NoneType"
            },
            "getPointingInfo": {
                "inputs": {
                    "option": "Any"
                },
                "output": "NoneType"
            },
            "readPointingInfo": {
                "inputs": {
                    "topic_name": "Any"
                },
                "output": "NoneType"
            },
            "detectPointingObjectWithCustomMsg": {
                "inputs": {
                    "classNameToBeDetected": "Any",
                    "easyDetection": "Any",
                    "useFilteredObjects": "Any",
                    "score": "Any",
                    "detectron_instance": "Any",
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "detectPointingObject": {
                "inputs": {
                    "classNameToBeDetected": "Any",
                    "useYolo": "Any",
                    "easyDetection": "Any",
                    "useFilteredObjects": "Any",
                    "score": "Any",
                    "detectron_instance": "Any",
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "returnPointedObject": {
                "inputs": {
                    "easyDetection": "Any",
                    "useYolo": "Any",
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "findObjectSimplifiedVersion": {
                "inputs": {
                    "pointingDirection": "Any"
                },
                "output": "NoneType"
            },
            "lineIntersectionPolygon": {
                "inputs": {
                    "img": "Any",
                    "slope": "Any",
                    "intercept": "Any"
                },
                "output": "NoneType"
            },
            "findClosestObjectToLine": {
                "inputs": {
                    "slope": "Any",
                    "intercept": "Any"
                },
                "output": "NoneType"
            },
            "detect_person_stance_startup": {
                "inputs": {},
                "output": "NoneType"
            },
            "detect_mult_persons_stance": {
                "inputs": {
                    "arm_pose_mode": "Any"
                },
                "output": "NoneType"
            },
            "detect_person_stance": {
                "inputs": {
                    "arm_pose_mode": "Any"
                },
                "output": "NoneType"
            },
            "slope_based_person_pose_detection": {
                "inputs": {
                    "nose": "Any",
                    "right_shoulder": "Any",
                    "left_shoulder": "Any",
                    "right_hip": "Any",
                    "left_hip": "Any",
                    "right_knee": "Any",
                    "left_knee": "Any",
                    "right_wrist": "Any",
                    "left_wrist": "Any",
                    "right_elbow": "Any",
                    "left_elbow": "Any",
                    "right_heel": "Any",
                    "left_heel": "Any",
                    "arm_pose_mode": "Any"
                },
                "output": "NoneType"
            },
            "detect_person_stance_w_assumed_associated_world_position": {
                "inputs": {
                    "arm_pose_mode": "Any"
                },
                "output": "NoneType"
            }
        },
        "PerceptionNodeManagment": {
            "launch_rospkg": {
                "inputs": {
                    "package_name": "Any",
                    "launch_file_sub_path": "Any"
                },
                "output": "NoneType"
            },
            "kill_node": {
                "inputs": {
                    "node_name": "Any"
                },
                "output": "NoneType"
            },
            "startObjLocalizer": {
                "inputs": {},
                "output": "NoneType"
            },
            "stopObjLocalizer": {
                "inputs": {},
                "output": "NoneType"
            },
            "resetObjLocalizer": {
                "inputs": {},
                "output": "NoneType"
            },
            "startFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "stopFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "resetFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "takePhotoFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "enableAutomaticFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "disableAutomaticFaceRecognition": {
                "inputs": {},
                "output": "NoneType"
            },
            "startMediapipeHolistic": {
                "inputs": {},
                "output": "NoneType"
            },
            "stopMediapipeHolistic": {
                "inputs": {},
                "output": "NoneType"
            },
            "resetMediapipeHolistic": {
                "inputs": {},
                "output": "NoneType"
            },
            "startDetectron": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "startDetectrons": {
                "inputs": {},
                "output": "NoneType"
            },
            "stopDetectrons": {
                "inputs": {},
                "output": "NoneType"
            },
            "startDetectronTopics": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "stopDetectron": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "stopDetectronTopics": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "startDetectronPersonKeypointDetection": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "stopDetectronPersonKeypointDetection": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "startYolov8": {
                "inputs": {},
                "output": "NoneType"
            },
            "stopYolov8": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "PerceptionObjectDetection": {
            "getDetectronTopicInfo": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "returnDetectedObjects": {
                "inputs": {
                    "useYolo": "Any",
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "returnDetectedObjectsDetectronMsg": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "filterObjectionDetectionMsg": {
                "inputs": {
                    "data": "Any",
                    "useFilteredObjects": "Any",
                    "classNameToBeDetected": "Any",
                    "score": "Any"
                },
                "output": "NoneType"
            },
            "readSynchronizedMsgs": {
                "inputs": {
                    "objectDetectorTopicName": "Any",
                    "camera_info": "Any",
                    "filtered": "Any",
                    "useYolo": "Any",
                    "detectWaving": "Any",
                    "cameraImgTopic": "Any",
                    "forPoseEstimation": "Any"
                },
                "output": "NoneType"
            },
            "unregisterSync": {
                "inputs": {},
                "output": "NoneType"
            },
            "getObjectNames": {
                "inputs": {
                    "detectron_instance": "Str",
                    "detectron_msg": "bool"
                },
                "output": "List"
            },
            "returnPersonKeypointDetectronMsg": {
                "inputs": {
                    "detectron_instance": "Any"
                },
                "output": "NoneType"
            },
            "isRaisingHand": {
                "inputs": {
                    "useYolo": "Any"
                },
                "output": "NoneType"
            },
            "yoloSeeingObjects": {
                "inputs": {},
                "output": "NoneType"
            },
            "getObjectsPoses": {
                "inputs": {
                    "detectron_instance": "Any",
                    "camera_device": "Any",
                    "get_mask_dimensions": "Any",
                    "useYolo": "Any"
                },
                "output": "NoneType"
            },
            "showBoundingBox": {
                "inputs": {
                    "objectClass": "Any",
                    "detectron_instance": "Any",
                    "camera_device": "Any",
                    "detectWaving": "Any",
                    "useYolo": "Any",
                    "cameraImgTopic": "Any"
                },
                "output": "NoneType"
            },
            "closeImgWindows": {
                "inputs": {},
                "output": "NoneType"
            },
            "displayImg": {
                "inputs": {},
                "output": "NoneType"
            }
        },
        "PerceptionPoseEstimation": {
            "seeingPersonWithinDistance": {
                "inputs": {
                    "distance_threshold": "Any"
                },
                "output": "NoneType"
            },
            "get_localized_objects_poses": {
                "inputs": {
                    "object_class": "Any",
                    "confidence": "Any",
                    "timeout": "Any",
                    "localizer_instance": "Any"
                },
                "output": "NoneType"
            },
            "get_localized_objects_poses_transform": {
                "inputs": {
                    "className": "Any",
                    "confidence": "Any",
                    "to_frame": "Any"
                },
                "output": "NoneType"
            },
            "get_localized_objects_poses_dict": {
                "inputs": {
                    "obj_list": "Any",
                    "confidence": "Any",
                    "to_frame": "Any",
                    "exclusion_mode": "Any",
                    "localizer_instance": "Any"
                },
                "output": "NoneType"
            },
            "get_median_localized_poses": {
                "inputs": {
                    "obj_list": "Any",
                    "confidence": "Any",
                    "to_frame": "Any",
                    "same_obj_assump_dist": "Any",
                    "min_samples": "Any",
                    "timeout": "Any",
                    "quick_mode": "Any",
                    "exclusion_mode": "Any",
                    "localizer_instance": "Any"
                },
                "output": "NoneType"
            },
            "get_localized_persons_bayes_tracker": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_pointing_object_pose": {
                "inputs": {
                    "pointing_object": "Any",
                    "depth_frame": "Any",
                    "fast_method": "Any",
                    "camera_device": "Any",
                    "get_mask_dimensions": "Any"
                },
                "output": "NoneType"
            },
            "get_objects_pose_boundbox": {
                "inputs": {
                    "objects": "Any",
                    "depth_frame": "Any",
                    "camera_device": "Any",
                    "get_mask_dimensions": "Any",
                    "useYolo": "Any"
                },
                "output": "NoneType"
            },
            "test_happypose": {
                "inputs": {
                    "obj_name_arr": "Any",
                    "frame_id": "Any"
                },
                "output": "NoneType"
            },
            "publish_object_marker": {
                "inputs": {
                    "object_name": "Any",
                    "pose": "Any",
                    "mesh_path": "Any",
                    "marker_id": "Any",
                    "frame_id": "Any",
                    "render_arrow": "Any"
                },
                "output": "NoneType"
            },
            "remove_object_marker": {
                "inputs": {
                    "object_name": "Any",
                    "marker_id": "Any",
                    "frame_id": "Any"
                },
                "output": "NoneType"
            },
            "call_pose_estimation_action": {
                "inputs": {
                    "object_names": "Any",
                    "frame": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            }
        },
        "PerceptionRobocupTasks": {
            "is_door_open": {
                "inputs": {
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "class_to_objects_dict": {
                "inputs": {
                    "object": "Any",
                    "object2": "Any"
                },
                "output": "NoneType"
            },
            "class_to_objects_list": {
                "inputs": {
                    "object": "Any",
                    "object2": "Any"
                },
                "output": "NoneType"
            },
            "object_to_class": {
                "inputs": {
                    "object_name": "Any"
                },
                "output": "NoneType"
            },
            "getRaisedHandsPoses": {
                "inputs": {
                    "detectron_instance": "Any",
                    "camera_device": "Any",
                    "get_mask_dimensions": "Any",
                    "useYolo": "Any"
                },
                "output": "NoneType"
            },
            "isObjectOntheFloor": {
                "inputs": {
                    "distance_threshold": "Any",
                    "use_median_localized": "Any",
                    "same_obj_assump_dist": "Any",
                    "min_samples": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "intersectingMasksSync": {
                "inputs": {
                    "pixelMaskIntersectionThreshold": "Any",
                    "class_name_1": "Any",
                    "class_name_2": "Any"
                },
                "output": "NoneType"
            },
            "isPersonHoldingDrinkSync": {
                "inputs": {},
                "output": "NoneType"
            },
            "isPersonHoldingTrashSync": {
                "inputs": {},
                "output": "NoneType"
            },
            "isPersonWearingShoesSync": {
                "inputs": {},
                "output": "NoneType"
            },
            "isPersonHoldingDrink": {
                "inputs": {
                    "pixelMaskIntersectionThreshold": "Any"
                },
                "output": "NoneType"
            },
            "isPersonWearingShoes": {
                "inputs": {
                    "pixelMaskIntersectionThreshold": "Any",
                    "specific_overall_dataset": "Any"
                },
                "output": "NoneType"
            }
        },
        "PerceptionSurfaces": {
            "get_all_surfaces": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_polygon": {
                "inputs": {
                    "name": "Any"
                },
                "output": "NoneType"
            },
            "get_polygon_height": {
                "inputs": {
                    "name": "Any"
                },
                "output": "NoneType"
            },
            "get_associated_surface": {
                "inputs": {
                    "point": "Any"
                },
                "output": "NoneType"
            }
        },
        "perception": {
            "apiInitialization": {
                "inputs": {},
                "output": "NoneType"
            },
            "objectsNamesFromSemanticMap": {
                "inputs": {},
                "output": "NoneType"
            },
            "getCameraDeviceInfo": {
                "inputs": {
                    "camera_device": "Any"
                },
                "output": "NoneType"
            },
            "getImg": {
                "inputs": {
                    "useYolo": "Any",
                    "camera_info": "Any"
                },
                "output": "NoneType"
            }
        }
    },
    "semantic_map": {
        "semantic_map": {
            "clear_semantic_map": {
                "inputs": {},
                "output": "NoneType"
            },
            "start_semantic_map": {
                "inputs": {},
                "output": "NoneType"
            },
            "stop_semantic_map": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_semantic_map_yaml": {
                "inputs": {
                    "filters": "Any"
                },
                "output": "NoneType"
            },
            "get_semantic_map": {
                "inputs": {
                    "filters": "Any"
                },
                "output": "NoneType"
            },
            "save_semantic_map": {
                "inputs": {
                    "path": "Any",
                    "filters": "Any"
                },
                "output": "NoneType"
            },
            "get_objects": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_surfaces": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_rooms": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_available_location_names": {
                "inputs": {
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "get_location_by_name": {
                "inputs": {
                    "semantic_name": "Any"
                },
                "output": "Union[Tuple]"
            },
            "get_room_by_uuid": {
                "inputs": {
                    "room_uuid": "Any"
                },
                "output": "NoneType"
            },
            "get_surface_by_uuid": {
                "inputs": {
                    "surface_uuid": "Any"
                },
                "output": "NoneType"
            },
            "get_object_by_uuid": {
                "inputs": {
                    "object_uuid": "Any"
                },
                "output": "NoneType"
            },
            "get_objects_on_surface": {
                "inputs": {
                    "surface_uuid": "Any"
                },
                "output": "NoneType"
            },
            "get_room_by_name": {
                "inputs": {
                    "semantic_name": "Any"
                },
                "output": "NoneType"
            },
            "get_room_by_property": {
                "inputs": {
                    "property": "Any",
                    "value": "Any"
                },
                "output": "NoneType"
            },
            "get_surface_by_name": {
                "inputs": {
                    "semantic_name": "Any",
                    "return_one": "Any"
                },
                "output": "NoneType"
            },
            "get_surface_by_property": {
                "inputs": {
                    "property": "Any",
                    "value": "Any"
                },
                "output": "NoneType"
            },
            "get_objects_by_name": {
                "inputs": {
                    "name": "Any"
                },
                "output": "NoneType"
            },
            "cluster_objects_surface": {
                "inputs": {
                    "surface_uuid": "Any"
                },
                "output": "NoneType"
            },
            "cluster_all": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_cluster": {
                "inputs": {
                    "surface_uuid": "Any"
                },
                "output": "NoneType"
            },
            "get_all_clusters": {
                "inputs": {},
                "output": "NoneType"
            },
            "add_cluster": {
                "inputs": {
                    "cluster_uuid": "Any"
                },
                "output": "NoneType"
            },
            "object_cluster": {
                "inputs": {
                    "list_objects": "Any",
                    "uuid": "Any",
                    "score": "Any"
                },
                "output": "NoneType"
            },
            "order_xy_points": {
                "inputs": {
                    "xy_points": "Any"
                },
                "output": "NoneType"
            },
            "detectron_name_to_semantic_name": {
                "inputs": {
                    "detectron_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "semantic_name_to_detectron_name": {
                "inputs": {
                    "semantic_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "detectron_name_to_object_category": {
                "inputs": {
                    "detectron_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "semantic_name_to_object_category": {
                "inputs": {
                    "semantic_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "detectron_name_to_object_dimensions": {
                "inputs": {
                    "detectron_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "semantic_name_to_object_dimensions": {
                "inputs": {
                    "semantic_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "detectron_name_to_default_location": {
                "inputs": {
                    "detectron_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "semantic_name_to_default_location": {
                "inputs": {
                    "semantic_name": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "category_to_objects_semantic_names": {
                "inputs": {
                    "category": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "category_to_default_location": {
                "inputs": {
                    "category": "Any",
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "get_people_names": {
                "inputs": {
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            },
            "cache_map": {
                "inputs": {
                    "semantic_map_yaml_path": "Any"
                },
                "output": "NoneType"
            }
        }
    },
    "speech": {
        "speech": {
            "speech_to_text_service": {
                "inputs": {
                    "time": "Any",
                    "audio_path": "Any",
                    "asr": "Any",
                    "delete": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "microphone_start": {
                "inputs": {},
                "output": "NoneType"
            },
            "microphone_stop": {
                "inputs": {},
                "output": "NoneType"
            },
            "microphone_active": {
                "inputs": {},
                "output": "NoneType"
            },
            "speech_to_text_start": {
                "inputs": {
                    "asr": "Any"
                },
                "output": "NoneType"
            },
            "speech_to_text_stop": {
                "inputs": {},
                "output": "NoneType"
            },
            "keyword_detection_start": {
                "inputs": {},
                "output": "NoneType"
            },
            "keyword_detection_stop": {
                "inputs": {},
                "output": "NoneType"
            },
            "wait_for_keyword_detection": {
                "inputs": {
                    "timeout": "Any"
                },
                "output": "bool"
            },
            "wait_for_keywords": {
                "inputs": {
                    "keywords": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "clear_asr_log": {
                "inputs": {
                    "w_nlu_result": "Any"
                },
                "output": "NoneType"
            },
            "speech_to_text_history": {
                "inputs": {
                    "w_nlu_result": "Any"
                },
                "output": "NoneType"
            },
            "speech_to_text": {
                "inputs": {
                    "time": "Any",
                    "use_keyword_detection": "Any",
                    "use_nlu": "Any",
                    "remove_keyword": "Any",
                    "timeout": "Any"
                },
                "output": "NoneType"
            },
            "wait_for_speech_hypothesis": {
                "inputs": {
                    "time_secs": "Any",
                    "use_keyword_detection": "Any"
                },
                "output": "ASRNBestList"
            },
            "wait_for_reply": {
                "inputs": {
                    "time_secs": "Any",
                    "basic_reply": "Any",
                    "use_keyword_detection": "Any"
                },
                "output": "NoneType"
            },
            "get_previous_reply": {
                "inputs": {
                    "basic_reply": "Any"
                },
                "output": "NoneType"
            },
            "audio_callback": {
                "inputs": {
                    "msg": "Any"
                },
                "output": "NoneType"
            },
            "set_sample_audio": {
                "inputs": {
                    "sample_path": "Any"
                },
                "output": "NoneType"
            },
            "record_sample_audio": {
                "inputs": {
                    "time": "Any",
                    "audio_dir": "Any",
                    "set_param": "Any"
                },
                "output": "NoneType"
            },
            "listen_sample_audio": {
                "inputs": {
                    "timeout": "Any",
                    "confidence_thereshold": "Any"
                },
                "output": "NoneType"
            },
            "get_pos_labels": {
                "inputs": {
                    "string": "Any",
                    "pos_labels": "Any",
                    "pos_labels_blacklist": "Any"
                },
                "output": "NoneType"
            },
            "remove_keyword_gpsr": {
                "inputs": {
                    "sentence": "Any",
                    "keyword_possibilities": "Any"
                },
                "output": "NoneType"
            },
            "get_sentiment_keyword_based": {
                "inputs": {
                    "sentence": "Any",
                    "positive_keywords": "Any",
                    "negative_keywords": "Any"
                },
                "output": "NoneType"
            },
            "remove_keyword": {
                "inputs": {
                    "string": "Any",
                    "keyword_possibilities": "Any"
                },
                "output": "NoneType"
            },
            "remove_pos_labels": {
                "inputs": {
                    "string": "Any",
                    "pos_labels": "Any"
                },
                "output": "NoneType"
            },
            "remove_pos_labels_from_tree": {
                "inputs": {
                    "tree": "Any",
                    "pos_labels": "Any"
                },
                "output": "NoneType"
            },
            "compare_list_of_sentences": {
                "inputs": {
                    "sentence": "Any",
                    "list_of_sentences": "Any",
                    "threshold": "Any"
                },
                "output": "NoneType"
            },
            "get_similar_entity": {
                "inputs": {
                    "string": "Any",
                    "entity_name": "Any",
                    "pos_labels": "Any",
                    "pos_labels_blacklist": "Any"
                },
                "output": "NoneType"
            },
            "get_common_errors_dict": {
                "inputs": {},
                "output": "NoneType"
            },
            "get_common_errors": {
                "inputs": {
                    "categories": "Any"
                },
                "output": "NoneType"
            },
            "get_common_errors_for_word": {
                "inputs": {
                    "word": "Any"
                },
                "output": "NoneType"
            },
            "get_similar_keyword": {
                "inputs": {
                    "string": "Any",
                    "word_list": "Any",
                    "threshold": "Any",
                    "pos_labels": "Any",
                    "pos_labels_blacklist": "Any",
                    "correct_for_asr_errors": "Any"
                },
                "output": "NoneType"
            },
            "get_sentiment": {
                "inputs": {
                    "sentence": "Any"
                },
                "output": "NoneType"
            },
            "compare_sentences": {
                "inputs": {
                    "sentence1": "Any",
                    "sentence2": "Any"
                },
                "output": "NoneType"
            },
            "start_semantic_similarity": {
                "inputs": {},
                "output": "NoneType"
            },
            "stop_semantic_similarity": {
                "inputs": {},
                "output": "NoneType"
            }
        }
    },
    "tools": {
        "pre_arena_checklist": {
            "is_node_running": {
                "inputs": {
                    "node_name": "Any"
                },
                "output": "NoneType"
            },
            "check_nodes": {
                "inputs": {
                    "required_nodes": "Any"
                },
                "output": "NoneType"
            },
            "check_topics": {
                "inputs": {
                    "required_topics": "Any"
                },
                "output": "NoneType"
            },
            "load_configuration": {
                "inputs": {
                    "config_file": "Any"
                },
                "output": "NoneType"
            },
            "run_api_check": {
                "inputs": {},
                "output": "NoneType"
            }
        }
    }
}
