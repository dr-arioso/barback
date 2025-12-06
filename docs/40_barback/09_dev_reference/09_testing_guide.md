
# Testing Guide

Barback requires multi-layer tests:

## 1. Unit Tests
- feature extractors
- scoring functions
- path resolvers
- tag inference rules

## 2. Integration Tests
- skill chains
- resolver flows
- pipeline merging logic

## 3. End-to-End Tests
Simulate:
- UPC-only resolution
- image-based flows
- ambiguous products → conflict prompts

## 4. Benchmark Tests
For classification speed & scaler performance.
