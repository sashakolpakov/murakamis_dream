# Semantic addendum: formal regrading and finite jets

Read-only review, 1 November 2026. No Lean compiler, test, or build was run. No source was edited. This addendum is separate from the frozen central-source/volume report.

I read the complete `formal/VolumeLogic/FormalRegrading.lean` and the added passage in `manuscript/sections/M-directed-all-orders.tex`, lines 406–435, between equations `dao:eq-32` and `dao:eq-33`.

No correction is required in the statements inspected. A bivariate coefficient table is an arbitrary function on the nonnegative integer quadrant. `regrade B n b` is `B (n-b) b` when `b<=n`, and zero otherwise. The conditional prevents truncated natural subtraction from aliasing coefficients above the diagonal. `recoverRegrading D a b = D (a+b) b` therefore recovers every original coefficient exactly. The injectivity proof applies this actual left inverse, without imposing finite support or analytic convergence.

The range characterization has the necessary support assumption: coefficients above the diagonal must vanish. The finite-order iff says agreement through h-order L recovers precisely the original coefficients with a+b<=L. It makes no claim that a finite jet determines the whole series. The hidden example is the monomial h^(L+1); its truncation is zero, and its nonzero theorem expressly assumes 1!=0 in the coefficient ring. Thus the nonzero example is not vacuous in a zero ring, and the other identities remain valid there.

The additive and scalar identities are correct. No convolution multiplication, ring homomorphism, composition theorem, analytic extension, or statement about the quantum source is formalized in this module. Treating the tables as coefficients of a formal double series is legitimate for the stated regrading because at fixed output h-degree n only n+1 input pairs can occur. The existing CommRing hypothesis is stronger than necessary for some declarations but does not conceal a missing hypothesis.

M accurately separates this finite coefficient fact from its upstream analytic argument. It first uses the all-order source expansion and the genuine all-level annihilator to obtain vanishing coefficient identities. After clearing denominators it places the operator expression in C[[h,u]]. Only then does it invoke injectivity to move from the substituted zero series to the original one. The h^(-1) leading action was already removed from the finite shift difference; the added paragraph does not independently prove that analytic or formal-domain premise. It also does not justify a fixed-u analytic expansion from data at u=hs. These limitations are correctly reflected in its wording.

This read covers the new paragraph and finite module, not a fresh proof of the all-order source theorem, denominator-cleared gauge identity, or geometric characteristic identification.

Exact source hashes:
- `formal/VolumeLogic/FormalRegrading.lean`: `9fe0b604cfe2857cc26569442ee9c608c214307adb5fdfd666e154fcbadc7a2c`
- `manuscript/sections/M-directed-all-orders.tex`: `90bde811854ea8d259b9086516703bde0684a6de7d07b99e92a56e0adab49986`
