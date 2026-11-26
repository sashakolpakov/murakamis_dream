# Original boundary responses for the second-selection comparison

Research specification, 6 November 2026. This evaluates the response cost
in the [stationary boundary extension](research_mixed_stationary_reference_boundary_extension.md)
from already certified canonical coordinates and their derivatives.
It makes no root proposal, proves no scalar gap and does not certify a
new reference. The first flag is fixed at \(\alpha=1\); the third
flag is \(\beta\in\{0,1\}\).

## 1. Original derivatives and marginals

Use the order and original unscaled gradient from
[residual localization](research_mixed_prefix_residual_localization.md):
\[
 q=(e,\xi,a,u,z,v,b),\qquad f(q_*(c);c)=0,
 \qquad k(w)=\pi\cot\pi w=J''(w).
 \tag{1}
\]
Let \(H=f_q\). Its diagonal entries are
\[
\begin{aligned}
 H_{ee}&=-k(e-\xi)+k(e+a)-k(e)+i\pi,\\
 H_{\xi\xi}&=-2k(1/2-\xi)-3k(\xi)-k(e-\xi),\\
 H_{aa}&=k(e+a)+k(a+u)-3k(a)+i\pi,\\
 H_{uu}&=k(u+z)+k(a+u)-3k(u)+i\pi,\\
 H_{zz}&=k(u+z)+k(z+v)-3k(z)+i\pi,\\
 H_{vv}&=k(v+b)+k(z+v)-(2+\beta)k(v)+i\pi\beta,\\
 H_{bb}&=k(v+b)+k(b+c)-(2+\beta)k(b)+i\pi\beta.
\end{aligned}
 \tag{2}
\]
Its only nonzero off-diagonal entries, together with their symmetric
partners, are
\[
\begin{array}{c|cccccc}
 (i,j)&(e,\xi)&(e,a)&(a,u)&(u,z)&(z,v)&(v,b)\\ \hline
 H_{ij}&k(e-\xi)+i\pi&k(e+a)-i\pi&k(a+u)+i\pi&
 k(u+z)-i\pi&k(z+v)+i\pi&k(v+b)-i\pi .
\end{array}
 \tag{3}
\]
Only the last gradient component depends on \(c\), so
\[
 f_c=e_b\{k(b+c)+i\pi\},\qquad
 q_*'=-H^{-1}f_c.
 \tag{4}
\]
These identities follow by differentiating the seven displayed original
gradients, with no exponentiation or change of logarithmic lift.
The uniform bound \(-\Re H\succ(6\pi/49)I\) makes the
inverse legitimate at each canonical root. For example, an arbitrary
trial column \(T\) also satisfies the rigorous error estimate
\[
 \|q_*'-T\|_2\le\frac{49}{6\pi}\|HT+f_c\|_2.
 \tag{5}
\]
Either a validated inverse or a validated version of (5) can supply
the derivative input. The response module does neither.

The original allocated incoming and outgoing marginals are
\[
 p_L=g'(a+u)-\tfrac32g'(a)+2\pi iu,
 \qquad p_R=g'(v+b)-(1+\beta/2)g'(b).
 \tag{6}
\]
Using \(g''=k-i\pi\), their derivatives are exactly
\[
\begin{split}
 p_L'&=\{k(a+u)-\tfrac32k(a)+i\pi/2\}a'
                       +\{k(a+u)+i\pi\}u',\\
 p_R'&=\{k(v+b)-i\pi\}v'
       +\{k(v+b)-(1+\beta/2)k(b)+i\pi\beta/2\}b',\\
 \mathcal B&=|p_L'a'|+|p_R'b'|.
\end{split}
 \tag{7}
\]
In particular both the incoming chirp and the outgoing halfweight are
retained. The signed Laplacian identity has products with
\(\overline{a'}\) and \(\overline{b'}\); their moduli equal
those in (7). No conjugation is inserted into the holomorphic products
whose moduli define the subharmonic function \(\mathcal B\).

## 2. Certified-image premises

The caller supplies interval enclosures of the same canonical reference
and \(dq_*/dc\) for every actual parameter in its cell. The next
external leg may be attached or ordinary. A chart's enclosing rectangle
\(C\) may extend outside the typed domain: the claim is then only
for \(c\in C\cap K_j\), where
\[
\begin{split}
 K_3&=\{|c-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4&=\{|c-(.30-.052i)|\le.060\}
       \cap\{-.108\le\Im c\le-.001\}.
\end{split}
 \tag{8}
\]
Existence on the actual subset comes from the original canonical-prefix
theorem, not from a retained interval or a successful response calculation.
The affine residual provider must check its entire affine image and all
connecting arguments before using its Taylor estimate. In contrast,
\(H(q_*;c)\) and (7) may be evaluated on certified pointwise root
enclosures. Intersecting such enclosures with independently proved
canonical bounds is legitimate; intersecting them merely to obtain a
desired response sign or height condition is not.

The module requires its supplied coordinate boxes to lie in
\[
 E\times U\times Q^5,
 \quad E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10],\quad Q=[.23,.45]+i[-.12,.12],
 \tag{9}
\]
and verifies the strict whole-image conditions
\[
\begin{gathered}
 -.102<\Im u<-.001,\qquad -.078<\Im a<.021,\\
 (\Im v,\Im b)\in
 \begin{cases}(-.065,.068)^2,&\beta=0,\\
               (-.102,-.001)^2,&\beta=1.
 \end{cases}
\end{gathered}
 \tag{10}
\]
These are precisely the height hypotheses (11) of the boundary-extension
theorem. They justify the original full target product with selected
height \(0\le H_{\rm sel}\le.014\); a scalar provider may use the
proved index and Fourier-branch restrictions afterwards. The response
module records additional endpoint rectangles, ordinary typed disks and
external typed-domain tests for inspection. Those reports are not a
complete admissibility test: the scalar caller retains all original
reference, regularity and pair-sum premises of the
[reference curve](research_mixed_second_selected_reference_curve.md).

## 3. Module contract and outward enclosure

The new [module](../experiments/mixed_second_selected_external_response.py)
exports `evaluate_response(coordinates, qprime, beta, *, pi=None)`, also
named `evaluate`. The coordinate inventory is exactly
`e,xi,a,u,z,v,b,c`; the derivative inventory is exactly the first seven
names, with derivatives taken with respect to this same complex \(c\).
The caller supplies outward complex balls. An optional `pi` is an already
certified enclosure of \(\pi\); otherwise the module obtains one.

The four original cotangent arguments are \(a,a+u,b,v+b\).
The module checks their entire real intervals are in \((0,1)\),
then encloses \(k(w)=\pi\cos(\pi w)/\sin(\pi w)\).
A denominator not separated from zero is inconclusive. It saves every
argument, sine, cosine, cotangent, coefficient in (7), marginal derivative
and complex product. No input is clipped or replaced, and no other
reference, root, inverse or scalar evaluator is called.

If \([l_L,h_L]\) and \([l_R,h_R]\) are the saved outward
modulus intervals of the two products, its returned rational interval is
\[
 \max(0,l_L)+\max(0,l_R)\le\mathcal B\le h_L+h_R.
 \tag{11}
\]
The output key `B` stores these exact rational endpoints;
`B_upper_rational` and its two components are redundant audit witnesses.
Status is `enclosed` only when this interval is finite and both (9) and
(10) are verified for the full supplied boxes. Otherwise status is
`inconclusive`. The flags remain explicit. Even successful status is
conditional on the caller's existence and derivative certifications.

## 4. A complete boundary criterion

Cover every circular arc and clipping segment of (8), including their
junctions, using the [exact boundary charts](research_mixed_second_selected_external_boundary_charts.md).
For each fixed \((\beta,j)\), let the completed comparison cells give
\(D_\nu\le-\gamma_i\) for both Fourier alternatives and all their
fixed target domains, and \(\mathcal B\le B_i\). Put
\[
 \gamma=\min_i\gamma_i>0,\qquad B_0=\max_i B_i,
 \qquad \eta_j=\gamma-\frac{r_j^2 B_0}{2}.
 \tag{12}
\]
If \(\eta_j>0\), the original phase defect is at most
\(-\eta_j\) throughout \(K_j\), with disk-loss coefficients
\(6889/2000000\) and \(9/5000\), respectively. The global minimum
and maximum are independent: a positive pointwise comparison
\(\gamma_i-r_j^2B_i/2\) alone does not prove (12).

Boundary scalar majorants may certify the upper bound on \(D_\nu\),
but the maximum principle applies to the original defect with its
complex affine tangents, not to a clipped conjugate or its numerical
upper bound. Width-based resolution conditions may guide refinement;
they add no mathematical premise and failure to meet them is not an
adverse source sign. A stopped cover retains its full unresolved
frontier and proves no whole-domain conclusion.
