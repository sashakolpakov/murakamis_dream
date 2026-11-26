# Incoming angular decay on the complete inner-three rectangle

Private finite-source deduction, 10 November 2026. The complete
inner-three function has strict decay over its entire real incoming
color interval, at its original selected action, on the taller
outgoing rectangle. The estimate is obtained by inserting the
zero-safe factorial boundary inequality into an already controlled
complete shortened-edge contour. It is not inferred from a local
packet, from interpolation of isolated node values, or from a lower
bound for a signed Gram coefficient.

The resulting two-color estimate for the actual local outer
contribution is also proved. Passing from that contribution to the
whole \(343\) kernel requires the separately stated all-real
complement bound in Section 4. No whole closing assembly is asserted
here. No mathematical numerical evaluation is used.

## 1. Original sources and the claim

Put
\[
\begin{gathered}
 D=N-1,\qquad U=\lfloor N/2\rfloor-1,\qquad
 c_j=2\cos((2j+1)\pi/N),\\
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(x)=S_j^{-2}\prod_{\nu<j}(c_\nu-x),\\
 K_N(w,x)=\sum_{j=0}^D e_j(w)e_j(x),\qquad
 K_N^<(w,x)=\sum_{j=0}^U e_j(w)e_j(x),\\
 Q_N(w,u)=\phi_N^{(x)}
       [R_N(x)^3K_N(w,x)K_N(x,-2\cos u)] .
\end{gathered}                                                       \tag{1}
\]
The full Hermite functional, original crossing and all scalar
normalizations are unchanged. In particular neither edge in
\(Q_N\) is shortened. Write
\[
 \mathcal V_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le7/10\},
 \quad t_*(u)=a_*(u)-iH(u),\quad
 s(u)=\Re S_3(0,u),\quad D(\theta)=1-\cos\theta .
 \tag{2}
\]
The selected branch and its phase are those of the adopted
[incoming-neighborhood theorem](research_mixed_symmetric_closing_incoming_neighborhood.md).
Its preceding cubic and complete-inner inputs give, uniformly
on this compact set,
\(0<a_*(u)<\pi/2\) and \(0<H(u)<1\).

**Theorem 1.** There are \(c>0,C,A\) such that, through both
level parities,
\[
 \boxed{\quad
 |Q_N(-2\cos\theta,u)|
       \le CN^A e^{N\{s(u)-cD(\theta)\}},
 \qquad -\pi\le\theta\le\pi,\quad u\in\mathcal V_+ .
 \quad}                                                            \tag{3}
\]
Every fixed ordinary incoming derivative has the same angular
exponent at polynomial cost, including both real spectral
endpoints. This is an upper estimate for the full finite function.
It does not assert a relative packet at arbitrary real incoming
color.

## 2. A first-edge estimate with its incoming loss retained

Fix any compact family of first angles
\[
                 t=a+iS,\qquad
                 0<a_L\le a\le\pi/2,\quad |S|\le1 .
 \tag{4}
\]
One may also use any sufficiently small fixed neighborhood of a
compact subset in its interior. There are \(c_e>0,C_e,A_e\)
such that
\[
 |K_N^<(-2\cos\theta,-2\cos t)|
       \le C_eN^{A_e}
           e^{N\{\Re\psi(t,0)-c_eD(\theta)\}},
       \qquad -\pi\le\theta\le\pi .
 \tag{5}
\]
Here \(\psi\) is the original complete-end edge phase. We prove
(5) using the finite source, not a quotient by its value at
\(\theta=0\).

Specialize Sections 5--6 of the
[taller mixed-edge theorem](research_mixed_symmetric_closing_taller_mixed_edge.md)
to its parameters \((t,0)\). Its exact wire interpolation is
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2}.
 \tag{6}
\]
For the complete-end source the interpolated product is
\(B_N(y,t)B_N(y,0)\). At \(y=j/N\), (6) is exactly
\(e_j(-2\cos z)\), with the original scalar. It is holomorphic
on the whole open wire strip at every finite height.

Keep the main path, both deep alias paths, all additional and
external caps, both rounded cuts, and both physical endpoint sums
from that complete-end proof. Its endpoint-action margin is
\[
                    \Re\psi(t,0)>|S|/2+1/400 .
 \tag{7}
\]
Its cuts, connected side traces and continued critical point
give a main contour at rate at most \(\Re\psi(t,0)\), with
strict remote gaps. Its two full alias currents have their
proved strict gaps with the original depth-two paths. By the
finite parameter cover in that proof, all retained wire paths
lie in a common compact set
\[
       0<\alpha\le\Re y\le\gamma<1/2,\qquad |\Im y|\le H_0,
 \tag{8}
\]
with bounded lengths. The physical endpoint intervals have a
common positive rate gap \(\delta_e\).

Now replace only \(B_N(y,0)\) by \(B_N(y,\theta)\), with
\(\theta\) real. Sections 3--4 of the
[uniform factorial boundary theorem](research_uniform_factorial_and_boundary_decay.md)
give on (8)
\[
 |B_N(y,\theta)|
 \le \frac C N
       e^{N\{\mathfrak b(y,0)-c_0D(\theta)\}},\qquad
 c_0=
 \min_{\alpha\le x\le\gamma,\ |h|\le H_0}
          \frac{\sin(2\pi x)}{4\pi\cosh^2(\pi h)}>0 .
 \tag{9}
\]
This is the exact reflected-factorial upper bound through all
moving zeros. Both reciprocal reflection terms are retained.
Since \(0<\Re y<1/2\), the complete-angle-zero exponent
\(\mathfrak b(y,0)\) is the real part of the same branch
used in the original complete-end contour.

The other factor \(B_N(y,t)\), the residue multipliers and
all scalar coefficients are independent of \(\theta\).
Hence every retained contour in the exact finite identity
acquires the loss in (9) at its former complete-end rate.
No new contour or branch is selected. In particular the
additional caps retain exactly
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}
       B_N(y,t)B_N(y,\theta)\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}
       B_N(y,t)B_N(y,\theta)\,dy ,
 \tag{10}
\]
and the full upper and lower aliases retain, respectively,
\(\zeta/(1-\zeta)\) and \(1/(\zeta-1)\), where
\(\zeta=e^{2\pi iNy}\). The latter are not truncated.
Holomorphy of (6) means that the changed real outside color
introduces no finite pole into these contour identities.

It remains to check the physical endpoint sums, which are not
in (8). Every one of their actual rows satisfies
\(0\le j\le U<N/2\). The
[zero-safe real Newton theorem](research_mixed_newton_color_tubes.md),
equations (4)--(5), gives
\[
 |e_j(-2\cos\theta)|
       \le CN^A e^{NV_\theta(j/N)},\qquad
                         V_\theta(x)\le V_0(x)\quad(0\le x\le1/2).
 \tag{11}
\]
Thus their former complete-end upper profiles and their
strict gap \(\delta_e\) are unchanged, with polynomial cost.
This includes the zero row, the exact last retained row,
all numerator zeros and both parity cutoffs. The odd middle
row is not inserted into the shortened sum.

Choose \(c_e\le c_0\) and \(2c_e\le\delta_e\), using
\(D(\theta)\le2\). The endpoint sums as well as every
retained contour are then bounded by the right side of (5).
The complete finite identity proves (5).

## 3. The full inner trace

Use the exact decomposition (12) of the
[incoming-neighborhood theorem](research_mixed_symmetric_closing_incoming_neighborhood.md):
\[
 Q_N^{<<}(w,u)=I_N(w,u)+\mathcal R_N(w,u),\qquad
 \sup_{w\in[-2,2]}|\mathcal R_N(w,u)|
                            \le Ce^{N(s(u)-g)} ,
 \tag{12}
\]
with fixed \(g>0\). Here \(I_N\) is its literal local
current over
\[
       I(u)=[t_*(u)-\varepsilon,\ t_*(u)+\varepsilon],
 \tag{13}
\]
and both shortened edges occur in its integrand. That proof
already bounds every remote current uniformly for real \(w\):
signed horizontals, the central polynomial interval, the left
connection, the diagonal/right paths, low and far paths,
removed physical values and first normals, and both midpoint
columns. No such term is discarded in (12).

The same source's full edge restoration gives a fixed \(g'>0\)
with
\[
 \sup_{w\in[-2,2]}|Q_N(w,u)-Q_N^{<<}(w,u)|
                         \le CN^B e^{N(s(u)-g')}.
 \tag{14}
\]
It includes all revived odd radical rows, the odd middle
functional and the simple-node term. These remainders need no
new angular estimate: their fixed gaps can pay a sufficiently
small angular loss.

Choose the common \(\varepsilon\) in (13) small enough that
all its first angles lie in a compact subfamily of (4).
On (13), use (5) for the first shortened edge and the actual
second-edge packet from the taller mixed theorem. Its phase
is
\[
 \Phi_0(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it .
 \tag{15}
\]
The original calibrated horizontal concavity gives
\(\Re\Phi_0(t_*(u)+x,u)\le s(u)-x^2/(8\pi)\).
The exact multiplier
\[
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^D e^{-iNt})^2}
 \tag{16}
\]
has a denominator uniformly bounded away from zero there,
since \(H(u)>0\) uniformly. Therefore the literal local
integral, with its prefactor \(-N^2C_{N,3}/(\pi i)\), satisfies
\[
 |I_N(-2\cos\theta,u)|
                    \le CN^A e^{N(s(u)-c_eD(\theta))}.
 \tag{17}
\]
No pointwise asymptotic error is summed with a new sign.
This is an absolute bound on the intact local current.
Combining (12),(14),(17) proves (3), for example with
\(0<c\le\min\{c_e,g/2,g'/2\}\).

For fixed ordinary incoming derivatives, \(Q_N(w,u)\) has
degree at most \(D\) in \(w\). The weighted Laurent maximum
principle used in the endpoint real-color theorem extends (3)
by a cost at most \((1+c)|\Im\theta|\) in rate. An ordinary
circle of radius \(N^{-2}\) changes an inverse-cosine angle
by \(O(N^{-1})\), uniformly through both quadratic branch
points. Cauchy's formula therefore costs only a polynomial
factor for each fixed derivative, while preserving the
exponent in (3). This proves the derivative assertion.

## 4. The actual local outer contribution and the remaining global gate

Keep \(u_g=\beta_g-iK_g\), \(M_g=\Re\Xi(u_g)\), and the fixed
small increasing interval \(J_g\) from the
[local outer theorem](research_mixed_symmetric_closing_local_outer_packet.md).
Its original local observation is
\[
 \mathcal L_N(w_L,w_R)
 =-\frac{N^2C_{N,4}}{\pi i}
  \int_{J_g}\sin u\,Q_N(w_L,u)Q_N(w_R,u)
       e^{iNu^2/\pi}W_N(u)\,du .
 \tag{18}
\]
The interval lies in the interior of \(\mathcal V_+\).
The phase
\(\Xi(u)=2S_3(0,u)+iu^2/\pi-iu\) has its strict horizontal
maximum \(M_g\) there. Applying (3) to both full inner
factors in (18) consequently gives
\[
 |\mathcal L_N(-2\cos\theta_L,-2\cos\theta_R)|
 \le CN^A e^{N\{M_g-cD(\theta_L)-cD(\theta_R)\}} .
 \tag{19}
\]
All original scalars and the full outer sampling denominator
remain. Both incoming variables are independent real colors.

This identifies a sufficient final global hypothesis exactly.
If the entire complement in the original ordinary closing
identity obeys
\[
 \sup_{w_L,w_R\in[-2,2]}
 |Z_{343,N}(w_L,w_R)-\mathcal L_N(w_L,w_R)|
                           \le CN^A e^{N(M_g-\delta)},
                  \qquad\delta>0 ,
 \tag{20}
\]
then (19), \(D(\theta_L)+D(\theta_R)\le4\), and (20)
give a whole-real two-boundary angular bound for \(Z_{343,N}\)
with coefficient \(\min\{c,\delta/4\}>0\).
Its nonzero full bidisk packet and negative boundary Hessian,
once independently assembled, then give the quadratic strip
estimate by the adopted local-packet/real-gap lemma.

Equation (20) concerns the entire original complement and all
real colors. A small ordinary bidisk version of (20) is not
sufficient. In particular, any low/far estimate proved only
for incoming colors near \(-2\) must have its real-color scope
checked before using this implication. The present note
discharges the main contribution's angular-loss requirement;
it does not certify that remaining all-real audit or assert a
knot interpretation.

## Source bindings

- Complete taller mixed-edge paths, identity and endpoint gaps:
  research_mixed_symmetric_closing_taller_mixed_edge.md,
  SHA-256 01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Exact reflected factorial and whole-real boundary inequality:
  research_uniform_factorial_and_boundary_decay.md,
  SHA-256 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Recorded application and ordinary derivative continuation:
  research_mixed_endpoint_real_color_decay.md,
  SHA-256 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb.
- All-row zero-safe real entropy:
  research_mixed_newton_color_tubes.md,
  SHA-256 61f5d6ffe8571bf309c75cd3c74d8ffefedf997095aac7347cbbcc64e0a8c57d.
- Exact all-real inner current decomposition and both restorations:
  research_mixed_symmetric_closing_incoming_neighborhood.md,
  SHA-256 fedd23ea3d5d8aea8132af828f358bb0b0884e1e599a5dc31f457b33dd261aae.
- Full positive outer horizontal phase:
  research_mixed_symmetric_closing_horizontal_concavity.md,
  SHA-256 f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Literal local outer contribution:
  research_mixed_symmetric_closing_local_outer_packet.md,
  SHA-256 0ff2c66243a8cc67744d23c4ba51cc87c5d317ebbed6868b2b4127077e2edc8c.
