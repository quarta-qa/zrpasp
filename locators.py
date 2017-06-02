from selenium.webdriver.common.by import By


class LoginLocators(object):

    username = (By.ID, "UserName")
    password = (By.ID, "Password")
    lot = (By.XPATH, "//a[.='Выберите']")
    lotznach = (By.XPATH, "//li[.='Расчет зарплаты']")
    lotznachnumber = (By.XPATH, "//li[@value='7']")
    datestart =(By.XPATH, "//li[.='Период']")

class MenuLocators(object):
    menu = (By.XPATH, "//button[@class='left-menu-toggle']")
    ajax = (By.XPATH, "//span[.='Закрыть']")
    search = (By.ID, "grid_fdaae470-f3f1-4688-875c-8a815ce848e3_searchClear")


class ReportsEmployeeLocators(object):
    # для отчета Справ. о заработке госслуж.
    beginningOfPeriod = (By.ID, "283d32cb-6c36-4f0a-b1b6-80189345d2f6")
    endOfThePeriod = (By.ID, "44fdc642-4743-4eed-bfb6-acd320ae992c")
    # для отчета Справ. о з/п за период
    beginSalary = (By.ID, "71a3f1a1-c5ea-40d4-a324-6b321cf711dd")
    endSalary = (By.ID, "039c20a9-819d-4add-b8f8-2e6a8a94d80e")
    considerСulations = (By.ID, "c81eba36-5464-45f4-b1a0-5ce5c93a09d8")
    accordingАrchives = (By.ID, "e2dd805b-424c-486c-8336-b191960f2489")
    # для отчета Справ. для ПФР
    beginPFR = (By.ID, "a91d5ae4-c327-4c55-a4a1-14a89f4718f8")
    endPFR = (By.ID, "80e5faae-ec2c-4035-81ea-77b3d99044ad")
    considerPFR = (By.ID, "76c33d7c-d57b-4c39-9fe9-21e53f23b930")
    archivesPFR = (By.ID, "6fcd3f6e-1c6f-483a-9d7c-620ef0dffc00")
    # для отчета Справ. для Справка для ссуды
    beginForLoans = (By.ID, "043c8c48-dac8-425b-a523-d5d5d2c3ba1c")
    endForLoans = (By.ID, "bf093728-56ad-4991-85e2-fc6c70939474")
    branchBank = (By.ID, "9912a174-e94a-42ae-8b2a-3651346b3e87")
    # для отчета Справ. для биржи
    dateOfIssue = (By.ID, "62639b12-6ee1-404f-a8d5-cb5b04a13756")
    informationMonths = (By.ID, "e2f7d215-1ab0-4394-ad4e-5085d4f19af1")
    averageEarningsMonths = (By.ID, "8889ef31-6154-46fd-acea-3dcea1d9841e")
    monthIndexing = (By.ID, "7f02c990-1721-4aa5-aaf8-b13bdc189e66")
    considerRecalculations = (By.ID, "56fe8b49-83ab-481d-97af-d99cb103bf1a")
    archives = (By.ID, "dcb38300-1c58-406a-ae4d-25895d51519c")
    # для отчета Справ. для прикоман.
    beginForPrikomand =(By.ID, "821b6b7b-d73f-49c0-ab0d-97dfddb1807c")
    endForPrikomand =(By.ID, "73d13cac-ebd1-4f0e-a9f9-3c600ddcbf89")
    # для отчета Справ.для консульства
    beginTheConsulate = (By.ID, "c1cd4196-1998-47a2-b5e5-277a510ebb33")
    endTheConsulate = (By.ID, "14c574b8-3605-4eb0-ac92-c0ed3ea284c0")
    theConsulateEarningsMonths = (By.ID, "7451b84f-860e-4469-be7a-9e2fb39dbd1d")
    forSubmissionTo = (By.ID, "a7f74112-7c17-47bd-9ec4-609e9c458755")
    # для отчета Справ. для прикоман. 3 месяца
    beginForPrikomand3 = (By.ID, "0b870c09-1fca-4425-afb6-4bbf5b105285")
    dateInformation = (By.ID, "c73a3a1e-7d04-4df9-836f-c2cbd88248a8")
    # для отчета Справ. о з/п за 12 мес
    archivesSalary12months = (By.ID, "3c7bf57b-e434-42c7-843d-89e33785cfbd")
    # для отчета Справка о заработке для РУСЗН
    archivesRUSZN = (By.ID, "451410c3-eac4-4abc-a6f5-c30416ba63b9")
    RecalculationsRUSZN = (By.ID, "b76dc6e1-84f3-4eeb-bbc0-1e6a1ab9b478")
    # для Протокол расчета  доп. дней отпуска по уходу за реб.-инвалидом
    orderNumberChildrenDisabilities = (By.ID, "f8f84656-1743-4883-8179-bc72c529c829")
    beginChildrenDisabilities = (By.ID, "d440192c-25ff-4db6-ae99-e024a12978b4")
    endChildrenDisabilities = (By.ID, "809f1d24-384f-4827-a0a7-737c760b4d4b")
    dateChildrenDisabilities = (By.ID, "f1effdd5-2af4-4e11-bc88-099634ff0ab2")
    # для Платежно-расчетная ведомость по инструкции №70н
    numberStatements = (By.ID, "a5a1f9bf-f94e-42ea-bdb8-b232e93d74ea")
    cashDeskPayS = (By.ID, "17d08131-a193-4083-a68d-700000ce123c")
    cashDeskPayPo = (By.ID, "e6318c80-9986-4f5d-ae77-53a6a019c3f5")
    dateOfReport = (By.ID, "cb579de3-b5ee-433b-b437-11f150652ac2")
    includePaidSalary = (By.ID, "d247715c-29f0-41ab-8f2f-54bd9fa01de3")
    # для Сравнения долга
    archiveDebtComparison = (By.ID, "cf66d07d-90be-4ac9-bd71-73c2791f8342")
    # для Перечисл. в СБ
    allocationBank = (By.ID, "a03392c2-1155-4bda-99f7-cd80b48d45a0")
    # для Затраты по ЕСН и травматизму
    beginCostsOfESN = (By.ID, "70b230b1-f8db-4a3d-926f-fdeb91bdb849")
    endCostsOfESN = (By.ID, "aa406713-3169-44d5-95c3-ab7d6bb42971")
    # для Начисления по ЕСН и травматизму
    beginChargesForESN = (By.ID, "f79263ac-29f8-41b1-a05d-847f7383d470")
    endChargesForESN = (By.ID, "9c85bfa2-302b-4042-8453-bd191b3c64b8")
    # для Лицевая карточка списком
    facialCardListYear = (By.ID, "826e5bfb-5fef-4ffb-a0e6-7e6cfd3a6287")
    CountOnArchives = (By.ID, "ac0e99d0-e9ed-4baa-a8c5-82caa88ae0bd")
    AccountForRecalculations = (By.ID, "30c9b182-1039-4f3f-8469-30a87247fc77")
    hospital_leaveForPayment = (By.ID, "ca65ba41-82bd-48d1-b518-d3ccef7ec9de")
    # для Налоговый регистр списком
    taxRegisterListDate = (By.ID, "ee09c14d-bc76-4614-a43d-15fef6b94720")
    # для Расчетно-платежная ведомость по 52н
    numberSetPayroll52n = (By.ID, "b322c384-03f5-41ac-82a3-74753b23ca52")
    paymentOnTimeFromSetPayroll52n = (By.ID, "a9335742-368e-471f-b6f4-6f91e908371a")
    archivesSetPayroll52n = (By.ID, "7e88973b-587b-47ec-a5c3-3d0b688ad457")
    # для Список по заданному удержанию
    sortByLastName = (By.ID, "167fcccb-3df7-4721-8381-cb4d2cd97cd6")
    holdCode = (By.ID, "f951dd0c-522c-4b75-8905-9f60c78f3e9b")
    archivesListByPresetHold = (By.ID, "75069885-4eb6-4362-b85f-9540b440e0ef")
    beginListByPresetHold = (By.ID, "bdcce0c1-c494-4650-842f-a16aab71b66b")
    endListByPresetHold = (By.ID, "1aa01e2e-0d7d-4b51-92dd-60e708471eee")
    # для Свод расчетных ведомостей
    chargingByMonthSettOfPayroll = (By.ID, "2932e849-1dc6-44f9-80ea-fc95a8ea825b")
    holidaysByMonthSettOfPayroll = (By.ID, "90f470cf-eeae-4196-82c9-ede080246141")
    archivesSettOfPayroll = (By.ID, "405e0657-0013-4b79-952b-41fd42686783")
    ExpandSettOfPayroll = (By.ID, "e177c953-0cbb-4f9a-a716-beb44d04318f")
    newSVODSettOfPayroll = (By.ID, "e91bd445-703f-4afb-8426-52b2c0af2ada")
    SettOfPayroll = (By.ID, "")
    beginSettOfPayroll = (By.ID, "42c0a3c0-9aa6-46de-8957-684ca5eb3e27")
    endSettOfPayroll = (By.ID, "792f5953-f7f2-4fef-8862-626f786e891f")
    # для Мемориальный ордер краткий
    buchInvoice = (By.ID, "0421b11f-4cc9-41bb-b9da-7d6673cc5fb8")

    # Список сотрудников с заданным начислением
    beginSSN = (By.ID, "ec5fe57d-1a65-4f15-ac4d-29d030a7f431")
    endSSN = (By.ID, "9056c29e-9bc4-4807-aac7-c3a2b84e983d")
    # для SH2
    gropSH2 = (By.ID, "216c3c96-c3ab-462f-90ac-437076ec8683")
    # для SH5
    dateReportSH5 = (By.ID, "e635a84d-ac0b-4053-93c4-b211508da4f4")
    # для SVED_SP
    beginSVED_SP = (By.ID, "4fded10b-3ab0-4437-b46d-6b7b947114cc")
    endSVED_SP = (By.ID, "152a490a-e8c4-4b8e-bb95-f68ed2edc1af")
    # для SVN
    beginSVN = (By.ID, "e85a1658-37be-46f6-b241-46938a57cdcd")
    endSVN = (By.ID, "98e1fe15-d5fb-4583-978e-ddd5ddd6e054")
    gropSVN =(By.ID, "0ee8ef19-5e6d-4d0e-b2e2-0868b7cf99d6")
    # для Справка по вакансиям аппарата Счетной палаты РФ
    dateSP_VAC = (By.ID, "3dc17b19-d58b-42fc-aa9d-8ffa3bcfc23d")
    # для Справка по фактическим расходам по подразделениям (СП)
    beginKRS_P = (By.ID, "5150aeec-1325-4f89-ae11-b0fe1e363783")
    endKRS_P = (By.ID, "df714d21-c1c6-4081-9afc-6e42ee530edf")
    # для Протокол расчета страховых взносов с 2015 года
    datePESN15 = (By.ID, "68746090-a140-45df-9bb0-dfb33e9c5f43")
    #  для Свод по категориям и должностям (СП)
    beginSVD_DDGS = (By.ID, "31c063d7-13e6-41a6-b8ed-f3b0e021ba1f")
    endSVD_DDGS = (By.ID, "a587259c-77b6-47cc-bd15-00964a166463")
    # для Мониторинг фонда оплаты труда (СП)
    beginMON_SP = (By.ID, "8e11206b-0388-4a6e-80ed-1093a13e98e5")
    endMON_SP = (By.ID, "973719a8-9423-4073-acc8-fa06a894fe4e")
    # Сумма налоговых вычетов
    beginOT_VICH = (By.ID, "407bff93-8f36-4957-acbf-39344a12e09a")
    endOT_VICH = (By.ID, "723afe33-c3f3-4f4e-99a7-6e45d5e3f9de")
    # для Журнал учета рабочего времени
    beginJURV = (By.ID, "009daf6d-1ca1-44c0-a3b5-7f85a19cfb42")
    endJURV = (By.ID, "738ad9cb-73cf-41e1-bd2b-9ec304f5f9d5")
    unitJURV = (By.ID, "78570388-d247-4ec3-9489-78d0f2b1c32a")
    workerJURV= (By.ID, "29380f67-83be-49b8-96f0-878ca33b37a5")
    # Список сотрудников с окладом и надбавками
    unitOKN = (By.ID, "91f65d67-06ef-4010-8bb2-dd9fae97540d")
    # Список сотрудников по группе должностей
    unitDD1 = (By.ID, "b9f0cfd0-52fa-44ac-975b-a6d0fa0ef3e6")
    # Затраты по ЕСН и травматизму
    beginS21 = (By.ID, "70b230b1-f8db-4a3d-926f-fdeb91bdb849")
    endS21 = (By.ID, "aa406713-3169-44d5-95c3-ab7d6bb42971")
    codePFS21 = (By.ID, "401e5f1b-6f85-461c-931f-c5023ce579ec")
    buttonP4 = (By.ID, "e8cb4670-9b38-465a-a7ad-c483e5360623")
    # P4
    ResponsibleP4= (By.ID, "0e3b5486-11cf-45ac-a3b4-a052f5fc03e2")
    # Начисления по ЕСН и травматизму
    beginS23 = (By.ID, "f79263ac-29f8-41b1-a05d-847f7383d470")
    endS23 = (By.ID, "9c85bfa2-302b-4042-8453-bd191b3c64b8")
    # Лицевая карточка сотрудника.
    workerINC = (By.ID, "6b56b344-1e93-4696-951e-f0434b73af6c")
    # Реестр платежных ведомостей
    beginNVG = (By.ID, "20635903-ea2a-4608-8a4f-627d44751021")
    endNVG = (By.ID, "99a1fe51-6ba0-48ba-86f4-ec6ae1dd109f")
    # Справка по алиментам за период
    beginALM_PER = (By.ID, "11503241-2c46-43d8-b120-747347e1feeb")
    endALM_PER = (By.ID, "c5f32357-882c-4b93-80cf-0033793a2ba9")
    # Справка к форме 14 образца 2005 г. SF14_05
    dateSF14_05 = (By.ID, "7997bba5-512d-4eaa-bff9-16be226bb9a8")
    # Расшифровка ФОТ для формы П-4 по сотрудникам и начислениям
    gropP4_GR = (By.ID, "6d8aed9b-7750-4d3c-a8ca-f6f314250301")

    # Выверка подоходного налога
    beginFSS_SBL = (By.ID, "6e90067e-9fdd-4458-b7d4-374d0ac14612")
    endFSS_SBL = (By.ID, "95c84a72-09f6-4c4f-bd14-f3c6e6daec3b")
    workerFSS_SBL = (By.ID, "6336be92-119f-4871-87b2-93e15a314e49")
    # Форма 1-T(ГМС) 2016 г.
    dateT1DGS16 = (By.ID, "b9f5afd2-1b21-4a27-ba02-f82b93117d0a")
    # Расшифровка по сотрудникам к форме 1-T(ГМС) 2012 г.
    dateT1DGS12 = (By.ID, "b9f5afd2-1b21-4a27-ba02-f82b93117d0a")
    # Расчетная ведомость ФСС 2016 г.
    dateFSS4_15_16 = (By.ID, "01b91ebe-99d8-4a42-ab8b-5a4ddfc55843")
    codFSS4_15_16 = (By.ID, "25903bbb-e2c1-4df0-ab19-5ca916005052")
    injuryAccrualsFSS4_15_16 = (By.ID, "8845d69b-c82c-46c8-a8ed-e4513bfa8355")
    # SBL
    beginSBL = (By.ID, "22dfa05e-e982-4e69-bba7-ad44d05a4681")
    endSBL = (By.ID, "19c79922-298d-4ead-ad37-66783b3689d0")
    gropSBL = (By.ID, "e299ed41-d4f9-430e-aa1c-5950f92b42cc")
    SearchSBL = (By.ID, "grid_197ca8a1-ee8c-4c6d-b278-e52e9cd6afa5_field_0")

    #TSTp
    codeTSTp = (By.ID, "513fe673-81a2-4783-a9bc-4e5e5e8739a4")

    #SDT
    dateSDT = (By.ID, "fc75375b-4c7f-4602-985e-1ff6f506888f")
    #OTP
    codOTP = (By.ID, "bae3503e-cdff-41d2-92e3-dc7f1bb0dcfe")
    #TS1s
    codTS1s = (By.ID, "f951dd0c-522c-4b75-8905-9f60c78f3e9b")
    beginTS1s = (By.ID, "bdcce0c1-c494-4650-842f-a16aab71b66b")
    endTS1s = (By.ID, "1aa01e2e-0d7d-4b51-92dd-60e708471eee")
    # TSTs
    codTSTs = (By.ID, "")
    # STRinn
    gropSTRinn =(By.ID, "5364ae1c-e568-4fa3-b22e-65618be30c28")
    # TT5
    gropTT5 = (By.ID, "059e0b0c-d908-4b20-9064-874225c75158")

    # KRS
    beginKRS = (By.ID, "82f9330e-7eff-4b0b-8512-15394e849773")
    endKRS = (By.ID, "519e621e-fd6d-4924-962a-4f2abc56bc11")
    # NGR
    beginNGR = (By.ID, "a4cf1ce9-ffe6-4fc1-b868-86fd840872f9")
    endNGR = (By.ID, "de7d27f7-6e6e-471f-a774-8ef6b6fc7875")
    # NFF
    beginNFF = (By.ID, "53d3c4d1-2643-437c-bb45-6b194b33050c")
    endNFF = (By.ID, "3bb9de92-56a6-4a01-9cd6-c76fe036c0b4")
    # N_R
    beginN_R = (By.ID, "53d3c4d1-2643-437c-bb45-6b194b33050c")
    endN_R = (By.ID, "3bb9de92-56a6-4a01-9cd6-c76fe036c0b4")
    # SH1
    gropSH1 = (By.ID, "216c3c96-c3ab-462f-80ac-437076ec8684")
    dateSH1 = (By.ID, "07f8e428-5b73-450b-8c30-54e7ddc1e280")
    # TR1
    beginTR1 = (By.ID, "e2ee9754-8acd-4058-aea0-681fb130f7c5")
    endTR1 = (By.ID, "3e334294-91f3-4980-8002-d6343ecf7c4f")
    # VN1
    beginVN1 = (By.ID, "1db75c11-52b2-4df1-8565-d23b9ecbb526")
    endVN1 = (By.ID, "28a01391-a570-498a-973d-c80eb37b4a30")
    # RDC
    dateRDC = (By.ID, "ec9fee61-40a6-410f-9dca-7e7f963ca4dc")
    # SDP
    beginSDP = (By.ID, "0f38afb7-5f8a-41ac-be4c-eb905c45e3a4")
    endSDP = (By.ID, "e2025580-76ef-4800-90a5-1891744a1c94")
    # CMP
    dateCMP = (By.ID, "d314c60c-4d76-400b-bb1b-3a7425b65a85")
    # DGG
    dateDGG = (By.ID, "1c00dbf6-b45f-4d31-bf0b-19b4296f9ace")
    # DGR
    beginDGR = (By.ID, "c2161851-2e0e-41b6-9782-550c4a8ce2d5")
    endDGR = (By.ID, "d31e73bd-e99b-4559-973e-d2a7f7b47528")

    # DEG
    dateDEG = (By.ID, "fe8ad10a-f635-4c0a-91e8-74880a95df81")
    # T75
    dateT75 = (By.ID, "29065eae-d4d1-4e08-b65e-560b6b098e2e")
    # RPL
    beginRPL = (By.ID, "659440d9-5248-4e18-9ca3-f52c954191a0")
    endRPL = (By.ID, "50be41b5-79eb-4b70-a328-c536fe82f1da")
    # SH6
    gropSH6 = (By.ID, "216c3c96-c3ab-462f-80ac-437076ec8684")
    dateSH6 = (By.ID, "07f8e428-5b73-450b-8c30-54e7ddc1e280")
    # TSS
    beginTSS = (By.ID, "958d141c-5b64-4802-829f-8c627aac5fd4")
    endTSS = (By.ID, "859f48a3-6841-44f1-a267-d420076fba1a")
    gropTSS = (By.ID, "a69f3bb5-600d-4a86-bce9-89f3ceb2dc58")
    # DSR
    beginDSR = (By.ID, "0baa8278-855a-47f8-8d91-0c14e3e41c2b")
    endDSR = (By.ID, "90560e19-0330-44eb-b018-cf9ae0b78f4d")
    userDSR = (By.ID, "1356e23b-fd98-4a55-881e-a5f791c84cfc")
    # F441
    dateF441 = (By.ID, "24d4bcf8-f80f-4469-bc6c-d2f53fc97ac3")
    # F414
    dateF414 = (By.ID, "99d4344d-d7f2-4ef3-9e0f-21abde3febcb")
    # SH7
    gropSH7 = (By.ID, "5ed26076-bc78-43d3-a1dc-d78f76eb4eda")
    dateSH7 = (By.ID, "9e9359aa-2f36-4436-9cf6-db0980080972")

    # R92
    beginR92 = (By.ID, "46f44085-e2dd-41c8-a3f1-b19880318dfe")
    endR92 = (By.ID, "cb95c950-2739-470b-81b9-80974a549739")
    gropR92 = (By.ID, "9e425931-265c-4f9c-b65a-1812f470bae1")
    # OT1
    gropOT1 = (By.ID, "1cb9925a-51f9-43c2-9e58-39ba4a75964a")
    # R91
    beginR91 = (By.ID, "426e4f71-f828-4373-9afd-c10d24d57139")
    endR91 = (By.ID, "af9aa832-16fc-45ad-a6c7-46296a231cfd")
    # SV_PN
    dateSV_PN = (By.ID, "4b03759d-0eac-4cda-ae85-7334e32ade97")
    # PSV_PN
    datePSV_PN = (By.ID, "7619ac5d-9130-4748-be63-0a491d111ef3")
    gropPSV_PN = (By.ID, "892954b8-2a7e-43a4-8fad-cc28dd3e4ee3")
    # BLN
    codBLN = (By.ID, "02dab520-a65b-4d29-a5d0-641c5f762d1a")
    gropBLN = (By.ID, "0bc97aff-7621-48d9-9327-16e946214e7f")
    # SNCH
    beginSNCH = (By.ID, "a4cf1ce9-ffe6-4fc1-b868-86fd840872f9")
    endSNCH = (By.ID, "de7d27f7-6e6e-471f-a774-8ef6b6fc7875")
    # R1100
    beginR1100 = (By.ID, "699597a6-fc62-4c7a-81ba-d0b28e16ff64")
    endR1100 = (By.ID, "03455e8c-b3cd-4244-b258-aa07c8e99c35")
    codR1100 = (By.ID, "0ec5c9f9-a2bd-4587-bdbd-5287e498fc2f")
    # R91O
    beginR91O = (By.ID, "935e0d79-f551-4164-abd7-10df3de09d2a")
    endR91O = (By.ID, "2a80764d-4870-46bf-afb8-6adb1d48b7e0")
    gropR91O = (By.ID, "e24b45ee-1aeb-44ed-9ece-0d4440bdfc7b")
    codR91O = (By.ID, "6db512d6-0e7a-4e90-95dd-0634ff6c7716")
    # PTK
    beginPTK = (By.ID, "3a2c70c0-ab7c-42b7-9b84-08c12d886152")
    endPTK = (By.ID, "6e2b4c13-adc8-4399-afb8-11a1335f167d")
    gropPTK = (By.ID, "07663e33-e2d5-4825-b20d-1d4a2371a77e")
    # DBL
    beginDBL = (By.ID, "a27b563d-72f6-46e0-9b79-0203a606f002")
    endDBL = (By.ID, "e98b6204-6526-4681-bf1a-fbd45d52d232")
    gropDBL = (By.ID, "06f34580-e452-4e96-a684-797f5af5b005")
    # SPF
    dateSPF = (By.ID, "080fba8a-b79f-40bc-9e33-038cfcde3e58")
    gropFinSPF = (By.ID, "923b701b-5bdc-4cf4-9085-43197758673d")
    # SPNF
    dateCPNF = (By.ID, "4f66b6c7-513a-497a-8ece-682d003d9fb7")
    # VR1
    beginVR1 = (By.ID, "45351d55-4da0-4927-9881-6b15041f4cf9")
    endVR1 = (By.ID, "bab0f715-2e80-435f-946c-12cff1bad29e")
    gropVR1 = (By.ID, "93786bca-ffd0-4be8-bb28-7a78315f05ba")
    # BLNFZ
    beginBLNFZ = (By.ID, "006dbd3a-edec-4477-9f24-66b90053a041")
    endBLNFZ = (By.ID, "1d52656f-aa57-46d0-a168-39688686e72f")
    # SVSD
    beginSVSD = (By.ID, "16bd2abc-57b2-48b8-83a5-e4c8441cc869")
    endSVSD = (By.ID, "c1365d4e-0577-4a54-b0af-2b0fc5f37600")
    # UT53
    beginUT53 = (By.ID, "ac6f1cad-2faf-4431-9458-1c7ff9fb432a")
    endUT53 = (By.ID, "526555fe-27d6-4cdf-9d9c-cf5b188305c9")
    beginmonthUT53 = (By.ID, "cd0b87f8-e221-4b9f-ab56-b518c7b320b4")
    endmonthUT53 = (By.ID, "a70c905a-9f4e-431a-be30-df961cef7f4e")
    # PODQ
    datePODQ = (By.ID, "034fa3c0-4d4f-4b6a-ad3f-9b11e61b0254")
    gropPODQ = (By.ID, "e8530670-5104-4fa6-b25a-388b43e8c478")
    # JON_OKUD
    beginJON_OKUD = (By.ID, "ff033ee5-f0ea-4afb-8492-9cd9098c5693")
    endJON_OKUD = (By.ID, "bb41cfff-8bf9-47c8-b81a-489cd3bdd33d")
    analit1JON_OKUD= (By.ID, "cafead25-6782-4165-a69f-84de410f250d")
    analit2JON_OKUD= (By.ID, "751f21f0-a5ad-4bc0-9520-ac2f32531a29")
    analit3JON_OKUD= (By.ID, "08662b2e-6b98-4255-af1b-f5087239bf4b")
    # FETS
    gropFETS= (By.ID, "261f52c2-81d2-4442-b8fb-4b352e4e61eb")
    finansFETS= (By.ID, "578c9a68-9a05-4fa1-9a28-bf4b7efb65be")
    # SR_CH
    dateSR_CH= (By.ID, "049291cc-9e6a-46de-ad83-fa5ae61b0578")
    # SRSP14
    dateSRSP14= (By.ID, "0689a696-98a5-498c-a675-df11653a44ea")
    # NSGD
    beginNSGD = (By.ID, "83ec6e0b-d092-4011-bbfa-ea226bf9193a")
    endNSGD = (By.ID, "5b3760ac-763a-4c83-90bb-1cb9e1e97c5c")
    gropNSGD = (By.ID, "b6057f63-60b4-44f6-94a5-32e2c8065344")
    # KOR_P14
    dateKOR_P14= (By.ID, "1ed3a05c-caa1-4969-86da-d23ae5c7f1a6")
    # NOT_KNU
    kodNOT_KNU = (By.ID, "3abf3cbe-9181-41ab-9092-1319769d5f07")
    dateNOT_KNU = (By.ID, "27dfb618-2923-46f4-aeb6-ef6a38ba3077")
    # SRDN_GS
    beginSRDN_GS = (By.ID, "4a1b91ed-7cf4-4e10-a787-ee2e1be1a747")
    endSRDN_GS = (By.ID, "7318cd54-e690-4896-9e5f-ef6b3f4a6648")
    gropSRDN_GS = (By.ID, "36ad33cf-bb71-43c2-ad29-475df2463690")
    # SB_UVOLN
    beginSB_UVOLN = (By.ID, "010fda4b-89ad-48be-8e7c-ddf220a56b6f")
    endSB_UVOLN = (By.ID, "1cea9cc0-904e-4d79-948f-8c1790105af6")
    # SKID_MP
    beginSKID_MP = (By.ID, "9c1f6c57-e0ac-4132-8acb-25d538ba9c67")
    endSKID_MP = (By.ID, "edc54fdf-5480-495e-9999-69f5b1182829")
    # T57T
    montT57T= (By.ID, "725c6681-40ca-4b0a-88b7-e2355f326164")
    dateT57T= (By.ID, "78f4e4f1-ece3-4242-b8b4-45dfb58a2fb1")
    # SH8
    beginSH8 = (By.ID, "34573f7e-12b8-473a-8f25-95b0cbe84f4b")
    endSH8 = (By.ID, "d91384ae-7027-4772-9a55-3d48ef603a70")
    # SNP
    gropSNP = (By.ID, "b029bbb7-42ed-4857-afbd-48df7a556043")
    # P_TBL
    dateP_TBL = (By.ID, "9182f442-f2cf-44b0-b880-d816759b3168")
    gropP_TBL = (By.ID, "1f05bc41-ccd2-4457-a788-de0df0085944")
    # SVR
    beginSVR = (By.ID, "10d34c9d-d5b2-450c-b40e-f6034938405d")
    endSVR = (By.ID, "515e9d7f-ea4c-4515-b82e-aa07c965e68a")
    # TSTGOTP
    dateTSTGOTP = (By.ID, "782730b9-1c46-4185-9b19-b24518912375")
    # SP_DLT
    dateSP_DLT = (By.ID, "4795fd13-2c42-461d-8122-34db234af15e")
    # SPRF14
    beginSPRF14 = (By.ID, "748cdb87-38c1-4df8-ab69-917af9aa53af")
    endSPRF14= (By.ID, "a9411253-28dc-4549-81f1-fc04b24047d8")
    # SPD1
    gropSPD1= (By.ID, "7fbae786-b5b3-4ada-a6a1-4f7aba20e7f9")
    # SPD2
    gropSPD2 = (By.ID, "7fbae786-b5b3-4ada-a6a1-4f7aba20e7f9")
    # SPD3
    gropSPD3 = (By.ID, "7fbae786-b5b3-4ada-a6a1-4f7aba20e7f9")
    # SPD4
    gropSPD4 = (By.ID, "7fbae786-b5b3-4ada-a6a1-4f7aba20e7f9")
    # SRZDOLSP
    beginSRZDOLSP = (By.ID, "76351304-d2a0-44d8-9bf8-5d1e8bb5e8d8")
    endSRZDOLSP = (By.ID, "7eacaa98-00c1-4567-b2e0-380577988363")
    # SBUV
    beginSBUV = (By.ID, "fd72758b-407b-4e7a-a636-981c9f8d8cf5")
    endSBUV = (By.ID, "6112c6dc-31ff-4599-ae56-afa235ce4662")
    paymentMethodSBUV= (By.ID, "2b7ff072-9ed9-4bc1-9b02-c0f3b771f709")
