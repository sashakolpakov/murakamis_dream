# A quantified diagonal obstruction to the raw paired Schur majorant

Research deduction, 7 November 2026. The completed original paired
kernel is coherent near its alternating boundary parameter. Its
absolute physical-row majorant is strictly larger there. This note
shows that the discrepancy persists on an explicit boundary interval
and cannot be repaired by a scalar weight. It concerns the proposed
raw exterior-rate test, not the actual kernel or the desired volume
statement. No new analytic value, source evaluation or numerical
proposal is used.

## 1. The original rate and the saved strict excess

Use the notation of the
[whole-message Schur criterion](research_mixed_paired_whole_message_schur_criterion.md).
Thus the actual boundary parameter is \(x_0\),

\[
 K=e^{2\pi i x_0},\qquad \rho=|K|<5/8,\qquad
 M=\Re\mathcal F(z_*;x_0,x_0),
 \qquad \Gamma=[-1/2,1/2].
 \tag{1}
\]

The bound on \(\rho\) is an original reference bound used in
[enlarged-rectangle accretivity](research_mixed_contracted_pair_enlarged_rectangle.md).
For real \(\theta\), set \(X_\theta=K e^{2\pi i\theta}\).
For fixed physical indices \(v=(s,t,p,q)\in\Omega\), let
\(E_v(\theta)\) be the original physical-row upper rate with
both external exponentials equal to \(X_\theta\). Explicitly,

\[
\begin{split}
 E_v(\theta)={}&-\log\rho+J(s+t)+J(t+p)+J(p+q)
                    -2J(t)-3J(p)-J(q)\\
 &+(s+q)\log\rho-I_\theta(s)-I_\theta(q),\\
 I_\theta(u)={}&\int_0^u
       \log|1-Ke^{2\pi i\theta-2\pi i r}|\,dr.
\end{split}
 \tag{2}
\]

Every cardinal and factorial term is retained. The row has the same
three support inequalities as the original contracted source; the
external shift does not change them. Write

\[
 \mathcal B_{\rm phys}(\theta,\theta)
                  =\max_{v\in\Omega}E_v(\theta).
 \tag{3}
\]

The immutable
[nine-face diagnosis](research_mixed_contracted_pair_nine_faces_diagnosis.md),
equations (1)--(3), proves for the single fixed supported row

\[
 v_0=(.45,.305175316565,.281506716344,.307605897026)
 \tag{4}
\]

that

\[
 E_{v_0}(0)>\frac{761517}{500000},\qquad
 M<\frac{756257}{500000},\qquad
 E_{v_0}(0)-M>\frac{263}{25000}.
 \tag{5}
\]

These are saved lower and upper enclosures, respectively. They do
not use the larger affine tangent upper bound. The relevant original
record remains
`repro/results/research-mixed-contracted-pair-nine-faces.json`, SHA-256
`174752c3b6f5c026dc4153287e153515d7f94e12959a0188f188d4cbf4d42cbc`.

## 2. An explicit interval of raw diagonal excess

**Proposition 1.** For every real \(|\theta|\le1/300\),

\[
 \mathcal B_{\rm phys}(\theta,\theta)
              >M+\frac{13}{25000}>M+\frac1{2000}.
 \tag{6}
\]

*Proof.* Put
\(f_\theta(r)=\log|1-Ke^{2\pi i\theta-2\pi i r}|\).
Since \(\rho<1\), it is smooth and periodic, and
\(\partial_\theta f_\theta=-\partial_r f_\theta\).
Consequently

\[
 \frac{d}{d\theta}I_\theta(u)
                       =f_\theta(0)-f_\theta(u),\qquad
 E_v'(\theta)=f_\theta(s)+f_\theta(q)-2f_\theta(0).
 \tag{7}
\]

For every real argument,
\(1-\rho\le|1-Ke^{i\alpha}|\le1+\rho\). Thus

\[
 |E_v'(\theta)|
 \le2\log\frac{1+\rho}{1-\rho}
 <2\log\frac{13}{3}<3.
 \tag{8}
\]

The final inequality is elementary and requires no logarithm
evaluation: the exponential series gives

\[
 e^{3/2}>
 1+\frac32+\frac{(3/2)^2}{2}
       +\frac{(3/2)^3}{6}+\frac{(3/2)^4}{24}
 =\frac{563}{128}>\frac{13}{3}.
 \tag{9}
\]

Integrating (8) for the same row (4) and using (5) yields
\(E_{v_0}(\theta)-M>263/25000-1/100=13/25000\).
Taking the maximum in (3) proves (6). No index is optimized or
changed in this argument. \(\square\)

## 3. Consequence for weights, phase choices and closed cycles

At the invariant local phase, the normalized gradient perturbation
is \(h=0\). The
[local basin identities](research_mixed_alternating_interface_local_entrance_basin.md),
equations (2), (6)--(7), give
\(\mathcal G0=0\), \(\chi_0(0)=0\), and
\(\Re C(0)=\Re\psi(0,0)=M\). Therefore the exterior
rate condition in the Schur criterion specializes to

\[
 W_0(x)+\mathcal B(x,y)\le M+W_0(y)-\eta_0.
 \tag{10}
\]

Whenever the original horizontal input point \(x=y=\theta\)
is in this exterior test, its weight cancels exactly. Equation
(10) would require \(\mathcal B(\theta,\theta)\le M-\eta_0\).
By (6), this is impossible if the chosen containing rate at that
point is \(\mathcal B_{\rm phys}\), even with zero loss.

In particular, suppose the coherent input/output chart is \(D_R\)
with \(R<1/300\), the contour is unchanged outside that disk,
and the raw physical rate is used when the output lies outside it.
The diagonal point \(\theta=1/300\) belongs to the unchanged
input period and to the exterior output set. It contradicts (10).
This is a necessary limitation of that hybrid choice. It does not
assert that \(R\ge1/300\) is sufficient, or that the proved
local kernel chart already has that radius.

Allowing a whole ball of local phase perturbations does not remove
the obstruction: the uniform criterion includes its invariant member
\(h=0\). A criterion only along a different prescribed message
orbit is a different assertion and requires its own estimates.

More generally, for a finite cycle of transitions to which (10)
applies, summation gives

\[
 \sum_{j=0}^{m-1}\mathcal B(u_j,u_{j+1})
                        \le m(M-\eta_0),\qquad u_m=u_0.
 \tag{11}
\]

The weights telescope. A phase or amplitude gauge acting by
similarity changes a rate only by a coboundary
\(a(x)-a(y)\), whose cycle sum is zero; a unit-modulus gauge
does not even change the pointwise modulus. Independently changing
input and output factors without their compensating intermediate
factors changes the original operator and is not a gauge shortcut.

## 4. What the original cyclic theorem does and does not supply

Let \(T_N=A_{3,N}A_{4,N}\). The original cardinal identity
gives, with increasing orientation on each full horizontal period,

\[
 \operatorname{tr}(T_N^m)
 =N^m\int_{\Gamma^m}
    \prod_{j=0}^{m-1}
       \mathcal K_{34,N}(x_0+u_j,x_0+u_{j+1})
                       \,du_0\cdots du_{m-1},\qquad u_m=u_0.
 \tag{12}
\]

Here \(u_0,\ldots,u_{m-1}\) are independent real period
coordinates and \(x_0\) remains the fixed reference; only
\(u_m=u_0\) is the cyclic identification. The bilinear cardinal
contractions introduce no complex
conjugation. Antiperiodic factors occur in pairs at even levels, so
the same identity holds at both parities.

The [complete cyclic theorem](research_mixed_full_cyclic_period.md)
proves a nonzero geometric asymptotic for this signed integral for
each fixed \(m\). Uniqueness of the original cyclic reference
identifies the repeated alternating critical action with \(m\)
times the original two-letter action. Neither that result nor the
exact finite identity (12) provides an upper bound for an individual
absolute cycle product or its raw physical-row majorant. Taking
absolute values before integration is precisely the additional
step in the Schur test. No coefficient nonnegativity is available
from a bilinear trace identity.

The older anchored-potential constructions in
[the nonlow open-chain theorem](research_mixed_nonlow_open_chain_boundary.md)
already start from a pointwise cyclic inequality for their own
retained-leg symbols. They are not new constructions needed here.
Their symbols and hybrid contours have not been identified with
the full Fourier-message kernel or its exterior rate in (10).
The cyclic integral theorem cannot supply that missing pointwise
identification.

The useful next requirement is therefore a coherent kernel bound
covering every diagonal point in the explicit interval (6), or a
different justified contour/rate construction there, before applying
the raw physical bound farther out. The completed local kernel
theorem is consistent with this: it retains the cancellations that
the offending physical row does not. No failure of the actual
Schur integral estimate, arbitrary mixed source, or knot-volume
statement is inferred.
