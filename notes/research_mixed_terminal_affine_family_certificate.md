# Enclosing a canonical terminal family over a parameter disk

Research protocol, 6 November 2026. The terminal comparison has a complete
proof at four fixed central parameters. To make it uniform, the next step is
to control the correlated motion of the critical coordinates. The
criterion below encloses the entire family by an affine function of its
single incoming parameter. Its proof uses the original logarithmic
equations. A proposed inverse matrix is accepted only after a contraction
inequality has been verified. This note prescribes a finite calculation;
it does not assert its outcome.

## 1. Equations and the family to be enclosed

Write \(q=(e,\xi,t,a,s)\). Let \(f(q;b)\) be the five equations (2) in
[the canonical suffix construction](research_mixed_terminal_horizontal_envelope_diagnostic.md).
For each terminal type \(\epsilon\), that construction proves that the
original zero \(q_*(b)\) exists and is unique in

\[
 \mathcal D=([.33,.47]+i[-.09,.08])
 \times([.21,.25]+i[.01,.10])
 \times([.23,.45]+i[-.12,.12])^3
\]

for every \(b\) in the appropriate disk \(D_3\) or \(D_4\). The original
logarithms are regular on a neighborhood of this product and of the
parameter disks. Put \(J=f_q\) and \(L=j'(s+b)+i\pi\), where

\[
 j'(z)=\pi\cot(\pi z),\qquad f_b=L\mathbf e_s.
\]

Fix a disk \(K=\{|b-b_0|\le r\}\) on which the preceding existence
statement applies. Let \(q^0\), a matrix \(B\), and a vector \(u\) have
exact rational real and imaginary parts. Their intended roles are a
central critical point, an approximate inverse of \(J(q^0;b_0)\), and
an approximate derivative of the family. These interpretations are not
hypotheses. Define

\[
 q^{\mathrm{aff}}(b)=q^0+u(b-b_0).
\]

Choose positive error radii \(\rho_i\). Let \(Q_0\) be any rectangular
complex box containing all \(q^{\mathrm{aff}}(b)\), and let \(Q\)
contain the coordinatewise complex disks of radii \(\rho_i\) around
every such vector. Require \(Q\subset\operatorname{int}\mathcal D\).
All matrix enclosures below are on these full boxes, without imposing
stationarity at their points.

## 2. A uniform contraction criterion

Enclose the following quantities:

\[
 \begin{split}
 c&=Bf(q^0;b_0),\\
 v&=B\bigl(J(q;b)u+L(q;b)\mathbf e_s\bigr)
                     &&(q,b\in Q_0\times K),\\
 E&=I-BJ(q;b) &&(q,b\in Q\times K).
 \end{split}
\]

Here \(Q_0\times K\) deliberately permits more pairs than the affine
graph. Suppose certified nonnegative real bounds satisfy

\[
 |c_i|\le c_i^+,
 \quad |v_i|\le v_i^+,
 \quad |E_{ij}|\le E_{ij}^+,
 \qquad
 c_i^++r v_i^++\sum_jE_{ij}^+\rho_j<\rho_i
 \quad\text{for every }i.                                      \tag{1}
\]

**Proposition.** For every \(b\in K\),

\[
 |q_{*,i}(b)-q_i^0-u_i(b-b_0)|\le\rho_i.
                                                               \tag{2}
\]

*Proof.* Along the straight segment from \(b_0\) to \(b\),

\[
 Bf(q^{\mathrm{aff}}(b);b)
 =c+(b-b_0)\int_0^1
 B\{J(q^{\mathrm{aff}}(b_0+\theta(b-b_0));b_0+\theta(b-b_0))u
              +L\mathbf e_s\}\,d\theta .
\]

Its \(i\)-th modulus is at most \(c_i^++rv_i^+\). For this fixed \(b\),
consider \(T_b(q)=q-Bf(q;b)\) on the closed polydisk centered at
\(q^{\mathrm{aff}}(b)\) with radii \(\rho_i\). Its derivative is
\(I-BJ\). The last term of (1) bounds the change of \(T_b\) along every
segment in that polydisk. Thus (1) maps the polydisk strictly into
itself. In the norm \(\|z\|_\rho=\max_i|z_i|/\rho_i\), its Lipschitz
constant is at most

\[
 \eta=\max_i\rho_i^{-1}\sum_j E_{ij}^+\rho_j<1.
\]

The contraction theorem gives a unique fixed point. The same inequality
implies that \(BJ\) is invertible at every point of the polydisk, by
the geometric series for \(I-(I-BJ)\). Hence \(B\) is invertible, and
the fixed point solves \(f=0\). It lies in \(\mathcal D\), so the
original uniqueness theorem identifies it with \(q_*(b)\). This proves
(2). \(\square\)

The expression \(Ju+L\mathbf e_s\) retains the first-order cancellation
that would be lost by enclosing \(f(q^{\mathrm{aff}}(b);b)\) directly.
No numerical inverse is assumed to be an exact inverse. Failure of (1)
only means that the proposed enclosure is insufficient.

## 3. Fixed four-family protocol

The standalone script
`experiments/certify_mixed_terminal_affine_family.py` uses the four saved
central rational proposals in
`repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json`.
It does not solve any new critical-point equation.

For each pair \((\beta,\epsilon)\in\{0,1\}^2\), it uses the entire
original incoming disk: center \(.35-.01i\), radius \(.09\) for
\(\beta=0\), and center \(.30-.052i\), radius \(.064\) for
\(\beta=1\). At 80 decimal digits it proposes

\[
 B\simeq J(q^0;b_0)^{-1},\qquad
 u\simeq-J(q^0;b_0)^{-1}L(q^0;b_0)\mathbf e_s,
\]

and saves each component as a 60-digit rational decimal. All proof
calculations use these exact rational numbers at 256-bit ball precision.
The Jacobian is differentiated explicitly from the original five
equations; no finite differences or numerical differentiation enter
the certificate.

There are exactly four prescribed radius vectors per family, with
multipliers \(1/4,1/2,1,2\) applied to

\[
 (\rho_e,\rho_\xi,\rho_t,\rho_a,\rho_s)
             =(1/500,1/1000,1/200,1/200,1/100).
\]

Every candidate is reported, whether or not an earlier candidate
succeeds. There is no subdivision, new root solve, alternate proposal,
precision increase, or retry. Each rectangle used in interval arithmetic
must contain the exact proposed polydisk: its half-width is an outward
upper bound for \(r|u_i|+\rho_i\). All comparisons in (1) use exact
rational upper bounds extracted from the ball arithmetic. Nonfinite
values and failures of domain containment are recorded as inconclusive.

Before the run, the proof and script are read separately. The source
record and proof dependencies are pinned by SHA-256, checked before
and after the run, and the output is created without overwriting a
previous file. The result retains the proposed affine coefficients,
the full enclosures of the preconditioned derivative and all contraction
rows, and the exact positive or negative margins.

A successful certificate controls critical coordinates on a full disk.
It still requires separate value and force estimates before it can
extend the terminal kernel bound. It asserts no finite-word realization
and no new knot-volume identity.

In particular, some old terminal source reserves require the smaller
actual input domains \(K_3,K_4\) of the
[boundary-chart construction](research_mixed_second_selected_external_boundary_charts.md).
Existence or enclosure of a critical point on the larger disks does not
extend those source reserves to their outer annuli.
