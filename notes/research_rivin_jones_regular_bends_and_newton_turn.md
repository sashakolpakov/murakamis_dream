# Regular bends for the external braid representation and the Newton turn

Private research proof, 14 November 2026. Frozen manuscripts are unchanged.

The external repository at commit
`e956fb919ac7d1bbc7cb3d3873fbac993feb94b7` implements braid matrices
and a prescribed reduced trace. It does not implement a cup, cap, or
quarter-turn API. This note specifies a self-dual boundary extension of
that braid representation and checks its bends explicitly. At the
principal root its turn becomes the recorded full Newton reversal,
with the original cup and cap scalars. No equality of unmarked closed
scalars is used to identify open operators.

## 1. A regular external cup and cap

Fix \(N\ge2\), put \(d=N-1\), and use
\[
 \zeta=A^{-2},\qquad v=A^2=\zeta^{-1},\qquad
 q=e^{\pi i/N},\qquad \rho_\zeta=\zeta-\zeta^{-1}.
 \tag{1}
\]
All parameter families below are taken near \(\zeta=q\).
We use \([a]_\zeta=(\zeta^a-\zeta^{-a})/(\zeta-\zeta^{-1})\)
and \([a]_\zeta!=\prod_{r=1}^a[r]_\zeta\), with
\([0]_\zeta!=1\); the same convention applies to \(v\).
The external divided-power basis \(e_0,\ldots,e_d\) has
\[
 K_v e_i=v^{d-2i}e_i,\qquad
 E_v e_i=[N-i]_v e_{i-1},\qquad
 F_v e_i=[i+1]_v e_{i+1},
 \tag{2}
\]
with missing endpoint vectors zero. The coproduct is
\[
 \Delta E_v=E_v\otimes K_v+1\otimes E_v,
 \qquad
 \Delta F_v=F_v\otimes1+K_v^{-1}\otimes F_v.
 \tag{3}
\]
The external positive-crossing formula is the checked universal
crossing in this basis: \(E_v^k\) supplies the product of
\([N-i]_v,\ldots,[N-i+k-1]_v\), and \(F_v^k/[k]_v!\)
supplies \({j+k\brack k}_v\). Thus (2) is a concrete realization
of the coefficients used by the external code, not an independently
chosen representation with the same dimension.

Define
\[
 r_i(\zeta)=\frac{[i]_\zeta![d-i]_\zeta!}{[d]_\zeta!},
 \qquad c_0(\zeta)=N\zeta^{d(d-1)/2},
\]
and the two coefficient lists
\[
 \begin{split}
 c_i(\zeta)&=c_0(\zeta)(-1)^i
                    v^{i(d-i-1)}r_i(\zeta),\\
 b_i(\zeta)&=\frac{(-1)^d v^d}{c_0(\zeta)}
                   (-1)^i v^{i(i-d-1)}r_i(\zeta)^{-1}.
 \end{split}
 \tag{4}
\]
The cup \(p_v\) and cap \(\ell_v\) are
\[
 p_v(1)=\sum_{i=0}^d c_i e_i\otimes e_{d-i},
 \qquad
 \ell_v(e_i\otimes e_j)=b_i\mathbf1_{i+j=d}.
 \tag{5}
\]
Every factor \([a]_\zeta\), \(1\le a<N\), is nonzero at
\(q\). Thus these are regular families, with no quantum-dimension
denominator.

**Lemma 1.** The maps (5) are invariant for (2)--(3), and both
snake contractions equal the identity.

**Proof.** The weight of every supported pair is zero. The raising
equation for the cup and the lowering equation for the cap are,
respectively,
\[
 \frac{c_{i+1}}{c_i}
   =-v^{d-2i-2}\frac{[i+1]_v}{[d-i]_v},
 \qquad
 \frac{b_{i+1}}{b_i}
   =-v^{-d+2i}\frac{[d-i]_v}{[i+1]_v}.
 \tag{6}
\]
They follow immediately from (4), since
\([a]_v=[a]_\zeta\). Substitution in the other two equations
gives \(\Delta F_v p_v=0\) and \(\ell_v\Delta E_v=0\)
as well. More explicitly, the coefficient at
\(e_a\otimes e_{d+1-a}\) in the first is
\([a]_v c_{a-1}+v^{-d+2a}[d+1-a]_v c_a=0\);
the corresponding cap equation is
\(v^{-d-2+2a}[d+1-a]_v b_{a-1}+[a]_v b_a=0\).

For the snakes, \(r_i=r_{d-i}\) and direct multiplication give
\[
                    c_i b_{d-i}=b_i c_{d-i}=1.
 \tag{7}
\]
Each contraction has exactly one surviving summand at a given input
index, with coefficient (7). This proves both identities. \(\square\)

The invariant cup line is one-dimensional: the nonzero adjacent
coefficients in (6) determine it from \(c_0\). The cap is then
fixed by the snakes. The choice of \(c_0\) in (4) specifies the
normalization needed below. Replacing the cup and cap by reciprocal
nonzero scalar multiples does not change their quarter-turn contraction.

There is a convention worth keeping explicit. The all-primal loop is
\[
                      \ell_v p_v=(-1)^d[N]_v.
 \tag{8}
\]
Indeed \(c_i b_i=(-1)^d v^{d-2i}\). This is the signed
self-dual convention, not a claim that the external code's prescribed
\(K_v\)-trace has acquired the factor \((-1)^d\). That trace
and its marked cut must be transported separately.

## 2. The actual change of basis and its root value

In the generic balanced module use
\[
 K|a\rangle=\zeta^{d-2a}|a\rangle,\quad
 \mathcal E|a\rangle=(\zeta^{-N}-\zeta^{N-2a})|a-1\rangle,
 \quad
 \mathcal F|a\rangle=(1-\zeta^{2a+2})|a+1\rangle.
 \tag{9}
\]
These are the regular highest-weight family in the Newton manuscript.
Its explicit basis change from the ordinary basis \(u_a\) is
\[
 |a\rangle=\frac{\rho_\zeta^a}{(\zeta^2;\zeta^2)_a}u_a.
 \tag{10}
\]
Every denominator in (10) is nonzero near the selected root.

The local crossing adapter uses the regular anti-diagonal matrix
\[
       T_\zeta e_i=t_i(\zeta)|d-i\rangle,
       \qquad t_i(\zeta)=\zeta^{-i(i-1)/2}.
 \tag{11}
\]
It respects the generator structure, not only the crossing matrix:
direct substitution gives
\[
 \begin{split}
 T_\zeta K_vT_\zeta^{-1}&=K,\\
 T_\zeta E_vT_\zeta^{-1}
       &=-\zeta^{-2}\rho_\zeta^{-1}\mathcal F K,\\
 T_\zeta F_vT_\zeta^{-1}
       &=-\zeta^2\rho_\zeta^{-1}K^{-1}\mathcal E.
 \end{split}
 \tag{12}
\]
For example, the first raising coefficient on the left is
\([a+1]_\zeta\zeta^{d-a-1}\). On the right use
\(1-\zeta^{2a+2}=-\rho_\zeta\zeta^{a+1}[a+1]_\zeta\).
The lowering identity follows from
\(\zeta^{-N}-\zeta^{N-2a}
 =-\rho_\zeta\zeta^{-a}[N-a]_\zeta\).
Also
\[
 \Delta(\mathcal F K)=\mathcal F K\otimes K+1\otimes\mathcal F K,
 \quad
 \Delta(K^{-1}\mathcal E)=K^{-1}\mathcal E\otimes1
                              +K^{-1}\otimes K^{-1}\mathcal E.
 \tag{13}
\]
Thus (12) respects the displayed coproducts. In particular, the
transported cup and cap are actual invariant bends of (9).

Put \(x=q^d\). At the root, factorial reflection gives
\(r_i(q)=1\), since \([N-a]_q=[a]_q\). For a supported
external pair \((i,d-i)\), multiply (4) by
\(t_i(q)t_{d-i}(q)\). The result is
\[
 t_i t_{d-i}c_i=N(-q)^i=Nx^{-i},
 \qquad
 \frac{b_i}{t_i t_{d-i}}=\frac{x^{d-i}}N,
 \tag{14}
\]
using \(x=-q^{-1}\). Consequently
\[
 (T_q\otimes T_q)p_v=p,
 \qquad
 \ell_v(T_q\otimes T_q)^{-1}=\ell,
 \tag{15}
\]
where the literal recorded balanced maps are
\[
       p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\qquad
       \ell_{ab}=\frac{x^a}{N}\mathbf1_{a+b=d}.
 \tag{16}
\]
Equation (14) checks the scalar on every supported entry. No scalar
is left unspecified in (15).

## 3. Quarter-turns and the full Newton algebra

Define the external quarter-turn by the actual contraction
\[
 \mathcal T_v(B)=
 (I^{\otimes2}\otimes\ell_v)(I\otimes B\otimes I)
                         (p_v\otimes I^{\otimes2}).
 \tag{17}
\]
Write \(T_{2,\zeta}=T_\zeta\otimes T_\zeta\). With the
regular transported bends from Section 2, the corresponding balanced
turn satisfies
\[
 T_{2,\zeta}\mathcal T_v(B)T_{2,\zeta}^{-1}
       =\mathcal T_{\mathrm{bal},\zeta}
                  (T_{2,\zeta}BT_{2,\zeta}^{-1}).
 \tag{18}
\]
This follows by substituting the two tensors from (5) and (11) into
(17). Every internal index has one factor \(t_i\) and its inverse;
they cancel. The two factors at the cup and cap are precisely those
in their transported coefficients. The four remaining boundary factors
are the two outer matrices in (18). This is an entrywise finite tensor
identity, without a semisimple decomposition.

At \(\zeta=q\), (15) identifies the balanced turn in (18) with
the exact turn in the Newton manuscript. Let
\[
 P_N(z)=2T_N(z/2)+2,\quad
 e_r(z)=\frac{\prod_{j<r}(q^{2j+1}+q^{-2j-1}-z)}
                  {\prod_{j=1}^r4\sin^2(\pi j/N)},
 \qquad 0\le r<N,
\]
and \(\Omega_{\mathrm{ext}}=T_{2,q}^{-1}\Omega T_{2,q}\).
The full commutant and Newton-turn propositions therefore give
\[
 \boxed{\quad
  \mathcal T_v\bigl(e_r(\Omega_{\mathrm{ext}})\bigr)
                   =e_{d-r}(\Omega_{\mathrm{ext}}).
       \quad}
 \tag{19}
\]
The underlying matrix algebra is faithful to
\(\mathbb C[z]/P_N(z)\). Its double-root blocks retain both
\(f(c)\) and \(f'(c)\); hence (19) includes every Casimir first
normal. It is stronger than equality at the distinct eigenvalues.

Equations (4)--(13) and (17)--(18) are regular parameter identities, so
they can be differentiated in \(\zeta\) to any fixed order while
retaining the derivatives of \(T_\zeta,p_v,\ell_v\). Formula
(19) is the root specialization. It does not license replacing the
generic turn by constant reversal when taking parameter derivatives.

For completeness, the original marked cap can also be retained
entrywise at the root. If \(m_{ab}=x^b/N^2\), its transported row is
\[
             m^{\mathrm{ext}}_{ij}
                =\frac{t_i(q)t_j(q)x^{d-j}}{N^2},
 \tag{20}
\]
without a condition \(i+j=d\). On the cup (5), its \(N\)
surviving summands are each \(1/N\), so
\(m^{\mathrm{ext}}p_v=1\). The marked row is not substituted
for the ordinary cap in (17). Nor is a generic extension of this
marked row being inferred from its root value; the external code's
prescribed open trace has its separately specified generic family.

## 4. Sources and limits of the conclusion

The external entry formula is in
`python/rivin_jones/r_matrix.py` at the commit stated above,
SHA256 `b6c5b48a9094587faa2ea6a9467ff801d838cfb007974a0fcd22a6e11aabfa76`.
Its actual crossing comparison under (11), including the reversed
crossing sign, is proved separately in
`research_rivin_jones_local_crossing_adapter.md`.

The physical pair algebra, generic balanced family, literal maps (16),
and full Newton-turn proposition used in (19) are in Sections 1--2
of `papers/newton-calculus/finite.tex`, SHA256
`2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e`.
The proof there uses physical block support and the unique outermost
tridiagonal path, so the repeated-root coefficients are not inferred
from a limit of eigenvalue-only identities.

This result supplies a regular local boundary adapter for bends. It
does not assert that the external repository already offers such a
boundary API, that its prescribed cut trace can be replaced on an
arbitrary exterior by a scalar average, or that a resulting quantum
period has a nonzero geometric asymptotic coefficient.
