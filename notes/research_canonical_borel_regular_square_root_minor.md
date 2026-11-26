# The regular square-root minor of the actual canonical source

Private written proof, 18 November 2026.

The exact moving-divisor theorem [W] leaves open an essential singularity
on its square-root cover. The actual finite-shift equation excludes that
possibility. The outer Laurent resolution supplies a vanishing-order
bound, and the first transport coefficient prevents the deeper polar
terms from satisfying the same source equation.

This gives a convergent square-root minor with a nonzero, explicitly
normalized leading amplitude. It also gives an exact finite Gaussian
formula for the original two canonical cutoff branches. No quantum
right factor, geometric character identification, infinite Laplace
continuation, or identification with the physical scalar is assumed.

## 1. Actual source and assertion

Use the original canonical source and actual node of [W]. Write
\[
 u=\log(Y/\alpha),\qquad z(u)=\alpha(e^u-1),\qquad
 \mathcal P_h=\sum_{i\in\mathcal I}p_i(h,u)T^i,\quad Tf(u)=f(u+h),
 \tag{1}
\]
where \(\mathcal I\subset\mathbb Z\) is finite and the coefficients are
holomorphic near \((h,u)=(0,0)\). The letter \(i\) in these formulas
is an integer shift index. The state gauge and all source factors
are retained. Put
\[
 P(u,L)=\sum_i p_i(0,u)L^i,\qquad
 P^{[1]}(u,L)=\sum_i\partial_hp_i(0,u)L^i.
 \tag{2}
\]
The actual hypotheses are
\[
 P(u,1)\equiv0,\quad P_L(0,1)=0,\quad
 b_*:=P_{uL}(0,1)\ne0,\quad P_{LL}(0,1)\ne0.
 \tag{3}
\]
Here \(\alpha\ne0,1\) is a simple Alexander root. The canonical
coefficient is \(W_0(Y)=1/\Delta(Y)\), and
\[
 r=\Delta'(\alpha)^{-1}\ne0.
 \tag{4}
\]
These are hypotheses on the displayed actual annihilator, not on a
classical or quantum factor substituted for it.

Let \(\ell(u)\) be the second classical root from [W], and let
\[
 S(0)=0,\qquad S'(u)=\log\ell(u),\qquad
 \kappa:=\ell'(0)=-\frac{2b_*}{P_{LL}(0,1)}\ne0.
 \tag{5}
\]
The logarithm equals zero at \(u=0\). Retain \(\eta_*\ne0\) from [L],
so \(S(u)=-\eta_*z(u)^2+O(u^3)\), and set
\[
 \rho=\xi+S(u),\qquad \tau^2=\rho.
 \tag{6}
\]
Write \(b(u,\xi)\) for the actual original Borel transform, also
regarded as a function of \((u,\tau)\) after (6). The theorem of [W]
supplies its joint holomorphy for small \(|u|\) and \(0<|\tau|\),
with the original sheets and continued histories.

**Theorem.** After shrinking the disks there are jointly holomorphic
functions \(E(u,\rho)\) and \(A(u,\rho)\), including at \((0,0)\), such that
\[
 \boxed{\quad b(u,\xi)=E(u,\rho)+\rho^{-1/2}A(u,\rho),
                  \qquad \rho=\xi+S(u).\quad}
 \tag{7}
\]
Choose the sign of \(\beta\), \(\beta^2=-1/\eta_*\), by the original
outer cover in [W]. Then
\[
 A(u,0)=\frac r\beta\,a(u),\qquad
 a(0)=1,\qquad \frac{a'}a=-\frac{e_g}{d_g},
 \tag{8}
\]
where
\[
 \begin{split}
 d_g(u)&=\ell(u)P_L(u,\ell(u)),\\
 e_g(u)&=P^{[1]}(u,\ell(u))
  +\frac{S''(u)}2
    \{\ell(u)P_L(u,\ell(u))+\ell(u)^2P_{LL}(u,\ell(u))\}.
 \end{split}
 \tag{9}
\]
The quotient in (8) is holomorphic at zero. In particular \(A(u,0)\)
is nonzero on a sufficiently small full complex \(u\)-disk.
The square root \(r/\beta=r\sqrt{-\eta_*}\) has its prescribed sign;
it is not a new phase choice.

## 2. The even part and the polar-order bound

The complete source [L] gives the convergent outer expression
\[
 b=\frac1wH(z,w,z^3/w^2),\qquad
 w^2=g(u)-\rho/\eta_*,\qquad
 g(u)=z(u)^2+S(u)/\eta_*=O(u^3).
 \tag{10}
\]
Here \(H\) is holomorphic on a fixed polydisk and \(H(0,0,0)=r\).
More precisely its original Laurent expansion is
\[
 b=
 \sum_{k\ge0}\sum_{j=0}^k c_{kj}z^{k+2j}w^{-2j-1}
 +\sum_{k\ge1}\sum_{m=0}^{k-1}d_{km}z^{k-m-1}w^m,
 \quad
 \sum_j|c_{kj}|+\sum_m|d_{km}|\le CD^k.
 \tag{11}
\]
To avoid confusion, the two-index \(c_{kj}\) in (11) will not denote
the polar coefficients in (14) below.

On \(|\rho|>C_H|u|^3\) the cover is
\[
 w=\beta\tau(1-\eta_*g(u)/\rho)^{1/2},
 \tag{12}
\]
where the unit square root is near one. The even part of (11) is
\[
 E(u,\rho)=
 \sum_{\substack{k\ge1,\ 0\le m<k\\m\ {\rm even}}}
 d_{km}z(u)^{k-m-1}
                     (g(u)-\rho/\eta_*)^{m/2}.
 \tag{13}
\]
All exponents are nonnegative. The coefficient bound in (11) proves
normal convergence on a sufficiently small full \((u,\rho)\)-polydisk.
Thus (13) is holomorphic through \(\rho=0\). It agrees with the deck-even
part of the actual source on the outer domain, and therefore on the
whole punctured cover of [W] by analytic uniqueness.

Let \(b_o=(b(u,\tau)-b(u,-\tau))/2\). Define
\[
 c_k(u)=[\tau^{-(2k+1)}]b_o
       =\frac1{2\pi i}\int_{|\tau|=t}
                      b_o(u,\tau)\tau^{2k}\,d\tau,\qquad k\ge0.
 \tag{14}
\]
For one fixed small \(t>0\), [W] makes these functions holomorphic
through \(u=0\). The contour is independent of \(u\), and uniform
holomorphy on a larger annulus justifies differentiation under it.
Their values are independent of the chosen radius in the punctured disk.

For \(u\ne0\), instead use \(|\tau|=K|u|^{3/2}\), with one sufficiently
large fixed \(K\). Equations (10)--(12) keep all arguments of \(H\)
in a smaller fixed polydisk and give \(|b_o|\le C/|\tau|\). Hence
\[
 |c_k(u)|\le C K^{2k}|u|^{3k},\qquad
                  \operatorname{ord}_{u=0}c_k\ge3k.
 \tag{15}
\]
This is a separate assertion for each \(k\); no uniform limit of
the moving circles at \(u=0\) is used.
At \(u=0\), (11) has only \(r/w\) as a negative power. Since
\(w=\beta\tau\) there,
\[
                             c_0(0)=r/\beta.
 \tag{16}
\]

## 3. The exact action-coordinate equation

We use the coordinate and history identities of [E], not its elliptic
inverse. Those identities hold also at a characteristic tilt.
The finite-shift coefficients after the action-coordinate change are
\[
 p_i^S(h,u)=p_i(h,u)
   \exp\!\left(\frac{S(u+ih)-S(u)}h\right).
 \tag{17}
\]
They are holomorphic at \(h=0\). Their differential expansion is
\[
 \mathcal A(h)=\sum_i p_i^S(h,u)e^{ih\partial_u}
                   =\sum_{n\ge0}h^nL_n.
 \tag{18}
\]
Every \(L_n\) has holomorphic \(u\)-coefficients and differential order
at most \(n\). The first two terms are
\[
 L_0=P(u,\ell(u))=0,\qquad L_1=d_g\partial_u+e_g,
 \tag{19}
\]
with (9). For example the order-\(h\) exponential correction in
(17) is \(i^2S''/2\), and
\(\sum_i i^2p_i(0,u)\ell^i=\ell P_L+\ell^2P_{LL}\).
This verifies all signs in (9).

Fix one nonzero local \(\rho\)-base and one lift of it, retaining its
actual earlier history. Let \(J\) be the primitive from that base
continued on the same cover. On every punctured \(u\)-chart the
identities of [E, Sections 5--6] give
\[
                         \sum_{n\ge1}J^nL_nb=F(u,\rho),
 \tag{20}
\]
where \(F\) is holomorphic in the base variable \(\rho\) through zero.
Its coefficients are determined by the earlier source histories.
In particular they are not chosen to vanish. All terms arising from
the nonlinear generator \(S'+J\partial_u\) are included in (17).

Continue (20) from that one base lift around the cover. Its right
side is the same holomorphic function of \(\rho\) on both sheets:
the history corrections in [E] are polynomials or normally convergent
holomorphic series in \(\rho-\rho_b\), with the fixed base values.
One does not independently reset those values on the second sheet.
The function \(F\) need not be regular at \(u=0\). We will only use
its zero odd deck projection on punctured \(u\)-charts.

On odd Laurent series define the odd primitive by
\[
 I_o(\rho^{j+1/2})
                     =\frac{\rho^{j+3/2}}{j+3/2},
                            \qquad j\in\mathbb Z.
 \tag{21}
\]
The denominators are nonzero. The series converges on every smaller
annulus where its input converges. It is the unique odd primitive.
An odd function times \(d\rho=2\tau\,d\tau\) has no \(\tau^{-1}\)
term, so this primitive is single-valued on the twofold annulus.
The even part (13) is holomorphic in \(\rho\); its primitives are even.
Local integration constants are also even. Consequently
\[
                  \pi_o J^n f=I_o^n\pi_o f
 \tag{22}
\]
for the functions and primitives in (20), where \(\pi_o\) is deck-odd
projection. The \(u\)-derivatives here hold \(\rho\) fixed, and commute
with this projection and with the fixed-base primitives.
Thus (20) implies the exact homogeneous odd identity
\[
 \sum_{n\ge1}I_o^nL_nb_o=0,\qquad
 (d_g\partial_u+e_g)b_o+
                  \sum_{n\ge1}I_o^nL_{n+1}b_o=0.
 \tag{23}
\]
The second identity differentiates the first once in \(\rho\).
It removes no quantum factor and assumes no first-order scalar equation.

Here are the analytic justifications for this infinite equation.
Take a fixed small \(\tau\)-annulus and buffered \(u\)-disks through
zero. The source of [W] is bounded on their compact subsets.
For small fixed \(|h|\), each
\(p_i^S(h,u)b(u+ih,\tau)\) is bounded on a smaller product.
Cauchy's formula in \(h\), applied to the finite sum, therefore gives
\[
                           \|L_nb\|\le M C_1^n.
 \tag{24}
\]
Use fixed compact lifted paths in a slightly larger annulus from the
base to both lifts of the contour. Their projected lengths are at
most some \(L_0<\infty\). The repeated primitive formula bounds
\(J^nf\) on them by \(L_0^n\|f\|/n!\). Equation (22) gives the same
bound, up to a fixed factor, for the odd projection. Thus the first
series in (23) converges normally; its \(\rho\)-derivative converges
normally on a smaller annulus. Laurent extraction and \(u\)-Taylor
extraction commute with these sums. These estimates use disks through
\(u=0\), even if the global history values in \(F\) are singular there.
The odd identity, initially proved for \(u\ne0\), extends across zero
by this normal convergence and the identity theorem.

Extracting the coefficient in (14) from (23) yields, for every \(k\ge0\),
\[
 d_gc_k'+e_gc_k+
 \sum_{n\ge1}\frac{(-1)^n}{(k+\tfrac12)_n}
                              L_{n+1}c_{k+n}=0.
 \tag{25}
\]
Indeed \(n\) odd primitives take
\(\rho^{-k-n-1/2}\) to
\((-1)^n\rho^{-k-1/2}/(k+1/2)_n\).
Positive odd Laurent powers do not contribute to (25).

## 4. The source residue forces regular first transport

For completeness the required cancellation follows directly from the
unshifted source. In the logarithmic coordinate its first coefficient is
\[
              W_0(\alpha e^u)=\frac r{\alpha u}+O(1).
 \tag{26}
\]
The order-\(h\) part of its actual annihilating equation is
\[
 P_L(u,1)\frac d{du}W_0(\alpha e^u)
                        +P^{[1]}(u,1)W_0(\alpha e^u)=0.
 \tag{27}
\]
The order-zero multiplier is identically zero by (3).
Comparing the coefficient of \(u^{-1}\), using
\(P_L(u,1)=b_*u+O(u^2)\), gives
\[
                             P^{[1]}(0,1)=b_*.
 \tag{28}
\]
Expansion along the partner in (5) now gives
\[
 d_g(u)=-b_*u+O(u^2),\qquad
 e_g(0)=b_*+\tfrac12\kappa P_{LL}(0,1)=0.
 \tag{29}
\]
Thus \(e_g=O(u)\) and \(e_g/d_g\) is holomorphic near zero.
This uses the residue of the actual source; it is not a normalization
chosen for a homogeneous WKB mode.

## 5. Exclusion of every deeper odd pole

Suppose at least one \(c_k\), \(k\ge1\), is nonzero. Among those indices
choose one minimizing the nonnegative integer
\[
              \delta_k=\operatorname{ord}c_k-3k.
 \tag{30}
\]
A minimum exists because these are nonnegative integers by (15).
Write \(m=\operatorname{ord}c_k\), so \(m\ge3\). For every \(n\ge1\),
either \(c_{k+n}=0\), or minimality gives
\[
                   \operatorname{ord}c_{k+n}\ge m+3n.
 \tag{31}
\]
The analytic differential operator \(L_{n+1}\) has order at most
\(n+1\). Hence
\[
 \operatorname{ord}(L_{n+1}c_{k+n})
                           \ge m+2n-1\ge m+1.
 \tag{32}
\]
The sum in (25) is normal by Section 3. It is also \(u\)-adically
convergent by the increasing lower bound in (32); thus its total
order is at least \(m+1\). The term \(e_gc_k\) has the same lower
bound by (29).

In contrast \(d_gc_k'\) has order exactly \(m\). Its leading coefficient
is \(-b_*m\) times the nonzero leading coefficient of \(c_k\).
This contradicts (25). Therefore
\[
                            c_k\equiv0\quad(k\ge1).
 \tag{33}
\]
The contradiction treats a possible infinite essential principal part
at once. It does not truncate it or suppose a largest pole order.

Equation (25) for \(k=0\) consequently reduces to
\[
                         d_gc_0'+e_gc_0=0.
 \tag{34}
\]
Together with (16) and (29), this gives exactly (8).

On a fixed outer \(\tau\)-circle all Laurent coefficients are
holomorphic in \(u\), with uniform Cauchy bounds on smaller disks.
By (33), \(\tau b_o\) has no negative powers and is even in \(\tau\).
Its Cauchy series therefore extends jointly through \(\tau=0\), and
has the form \(A(u,\tau^2)\) with \(A\) jointly holomorphic.
Combining this with (13) proves (7) and its normalization.
In particular the essential singularity left open in [W] is excluded
for this actual source.

## 6. Exact finite Gaussian cutoff and uniform fixed-meridian amplitude

We now retain the original two finite cutoffs of [C]. Choose one small
fixed \(R\ne0\) inside the new minor disk. Their common starting lift
at \(\xi=0\) is the original canonical lift. At \(\xi=R\) their
endpoints on the cover (6) are
\[
                  \tau_{R,\pm}(u)=\pm T(u),\qquad
                         T(u)^2=R+S(u).
 \tag{35}
\]
At \(u=0\) take \(T(0)=\sqrt R\). Match \(\beta^{-1}\) to the
square root called \(\beta\) in [C], so that the \(+\) endpoint and
the difference \(D_R=U_{R,+}-U_{R,-}\) have precisely its orientation.
For initially nonzero \(u\), subtract the two actual continued
integrals with their common lower lift. Equation (7) and
\(d\xi=2\tau\,d\tau\) give
\[
 \boxed{\quad
 D_R(h,u)=\frac2h e^{S(u)/h}
       \int_{-T(u)}^{T(u)}e^{-t^2/h}A(u,t^2)\,dt .\quad}
 \tag{36}
\]
The deck-even term contributes \(tE(u,t^2)\); its integrand is odd
and has an even holomorphic primitive, so its endpoint values cancel.
The full differential in the \(\tau\)-coordinate is holomorphic at
zero. Thus the path in (36) can be any path in the small full
\(\tau\)-disk with these endpoints. There is no residual winding
choice. Equality extends to \(u=0\) by the cutoff regularization in
[C], or directly by the holomorphic endpoint formula.

Fix a closed \(h\)-sector with
\[
                 \operatorname{Re}(R/h)
                              \ge\kappa_0|R|/|h|,\qquad \kappa_0>0,
 \tag{37}
\]
and choose the continuous square root of \(h\) matching (35).
Shrink a fixed complex \(u\)-disk so that
\[
                            |S(u)|\le\kappa_0|R|/2.
 \tag{38}
\]
Then the two rays through \(\pm T(u)\) are strict Gaussian decay
rays, uniformly in \(u\) and the sector. Since \(A(u,0)\) is bounded
away from zero on a smaller closed disk, (36) gives
\[
 D_R(h,u)=2\sqrt\pi\,h^{-1/2}A(u,0)e^{S(u)/h}
                                      \{1+O(|h|)\}.
 \tag{39}
\]
This holds uniformly on that full fixed meridian disk. Neither
\(u\) parallel to \(h\) nor a shrinking overlap condition is required.
At \(u=0\) the leading coefficient is
\(2\sqrt\pi\,r/\beta\), exactly the constant in [C].

For precision, write \(A(u,\rho)=\sum_{n\ge0}A_n(u)\rho^n\).
For each fixed integer \(M\ge1\), the expansion in (39) has bracket
\[
 \sum_{n=0}^{M-1}(\tfrac12)_n A_n(u)h^n
  +O_M(|h|^M)
  +O_M\!\left(|h|^{1/2}
             e^{-\operatorname{Re}((R+S(u))/h)}\right),
 \tag{40}
\]
after replacing the factor \(A(u,0)\{1+O(|h|)\}\) there by this
bracket. To prove it, integrate the Taylor polynomial along the
straight segment \([-T,T]\), and extend each polynomial Gaussian
moment along the same two rays to infinity. Its value is
\(\sqrt\pi h^{n+1/2}(1/2)_n\).
The Taylor remainder on the finite segment is bounded by
\(C_M|t|^{2M}\); its Gaussian integral is
\(O_M(|h|^{M+1/2})\), uniformly by (37)--(38).
Each polynomial tail beyond \(T\) is
\(O_M(|h|e^{-\operatorname{Re}((R+S)/h)})\).
These estimates prove (40).
Only polynomial moments are integrated to infinity; no continuation
or growth assertion for the actual Borel source at infinity is used.
The absolute endpoint scale in (36) is \(e^{-R/h}\), as required
by the original finite-cutoff current.

In particular (39) gives, for this canonical difference on these local
sectors, the uniform two-sided size
\[
 c|h|^{-1/2}|e^{S(u)/h}|
       \le |D_R(h,u)|\le C|h|^{-1/2}|e^{S(u)/h}|
 \tag{41}
\]
for sufficiently small \(h\). It is not a lower bound for the closed
finite-color invariant, which still contains its separate endpoint
and global continuation data.

## 7. Complete proof sources and remaining scope

| Label | Complete proof direct | SHA256 |
|---|---|---|
| W | notes/research_canonical_borel_exact_moving_divisor.md | 629771b050742821571794576c53515d1c0fbcf07028599cad42047bb9218bfe |
| E | notes/research_actual_borel_analytic_elliptic_inverse.md | d84ffc6794bd05917168595ec909fcb739e693b7c7574dea7471a404fa328e55 |
| L | notes/research_classical_verma_borel_laurent_resolution.md | 6a65d3f47544255c46e6cc5450d822b5b38cfccce591e5ad59e21d4c569be341 |
| C | notes/research_canonical_cutoff_node_regularization_and_profile.md | 8c28a3d3a7b11085c8e2b5966221501b632ea99600aae4db57e8bdf8cd4a9631 |

W supplies the exact punctured action cover and actual companions.
E supplies the nonlinear coordinate/history identity; its inverse is
not used in this proof. L supplies the convergent outer Laurent
resolution, coefficient bounds and original residue. C is used only
for the original cutoff branches, their common lower lift, extension
through the node and oriented normalization. The exclusion of deeper
poles, regular amplitude and finite Gaussian formula are proved here.

This is a local theorem at the specified simple actual operator node.
It does not identify that branch with a hyperbolic representation,
construct a global physical summation, control all original endpoint
currents, or prove the arbitrary-short-filling scalar lower bound.
The latter target includes sources without this simple Alexander seed.
Only written mathematics and complete source-text reads were used.
No mathematical programs, tests or builds were run; frozen notes and
public manuscripts are unchanged.
