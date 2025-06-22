#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
融資診断プログラムのテスト実行（入力値を直接設定）
"""

def calculate_loan_assessment_test():
    """テスト用の融資診断計算"""
    print("=" * 50)
    print("中小企業向け融資診断システム（テスト実行）")
    print("=" * 50)
    
    # テスト用入力値
    annual_profit = 800  # 年間営業利益
    depreciation = 200   # 年間減価償却費
    current_monthly_payment = 30  # 現在の毎月返済額
    loan_amount = 500    # 借入希望金額
    loan_period = 5      # 借入期間
    profit_increase = 5  # 毎月営業利益増加見込み
    equipment_depreciation_period = 5  # 設備減価償却期間
    
    print("【入力値】")
    print(f"現在の年間営業利益: {annual_profit}万円")
    print(f"年間の減価償却費: {depreciation}万円")
    print(f"現在の毎月の借入返済額: {current_monthly_payment}万円")
    print(f"今回新たに借りたい金額: {loan_amount}万円")
    print(f"借入希望期間: {loan_period}年")
    print(f"借入により見込まれる毎月の営業利益増加額: {profit_increase}万円")
    print(f"設備資金の減価償却期間: {equipment_depreciation_period}年")
    
    # 計算処理
    print("\n" + "=" * 50)
    print("診断結果")
    print("=" * 50)
    
    # 1. 新たな毎月返済額を計算
    new_monthly_payment = loan_amount / (loan_period * 12)
    
    # 2. 新たな年間返済額を計算
    new_annual_payment = new_monthly_payment * 12
    
    # 3. 現在の年間返済額と合算
    current_annual_payment = current_monthly_payment * 12
    total_annual_payment = current_annual_payment + new_annual_payment
    
    # 4. 年間返済原資を計算
    profit_increase_annual = profit_increase * 12
    equipment_depreciation_annual = loan_amount / equipment_depreciation_period if equipment_depreciation_period > 0 else 0
    annual_repayment_capacity = annual_profit + depreciation + profit_increase_annual + equipment_depreciation_annual
    
    # 計算結果の表示
    print("【計算過程】")
    print(f"新規借入の毎月返済額: {new_monthly_payment:,.1f}万円")
    print(f"新規借入の年間返済額: {new_annual_payment:,.0f}万円")
    print(f"現在の年間返済額: {current_annual_payment:,.0f}万円")
    print(f"合計年間返済額: {total_annual_payment:,.0f}万円")
    print()
    print(f"現在の年間営業利益: {annual_profit:,.0f}万円")
    print(f"年間減価償却費: {depreciation:,.0f}万円")
    print(f"営業利益増加見込み（年間）: {profit_increase_annual:,.0f}万円")
    print(f"設備減価償却費（年間）: {equipment_depreciation_annual:,.0f}万円")
    print(f"年間返済原資: {annual_repayment_capacity:,.0f}万円")
    
    print("\n" + "-" * 30)
    
    # 5. 診断結果
    surplus_deficit = annual_repayment_capacity - total_annual_payment
    
    if annual_repayment_capacity > total_annual_payment:
        print("【診断結果】融資可能性あり")
        print(f"返済余力: {surplus_deficit:,.0f}万円")
    else:
        print("【診断結果】返済余力が不足しています")
        print(f"不足額: {abs(surplus_deficit):,.0f}万円")
    
    print("=" * 50)

if __name__ == "__main__":
    calculate_loan_assessment_test()