# An interior barrier for absolute wire-contour estimates

Private written proof, 16 November 2026.

There is an open family of original positive angle pairs for which
the exact factorial wire integrand has an interior vertical barrier
strictly above the selected saddle action. The barrier persists at
every wire height at the phase level. At finite level it contains a
vertical slab of width comparable to \(N^{-1}\) on which the actual
integrand has the corresponding exponential lower bound.

Any bounded-height path crossing that slab therefore has an excessive
absolute integral, irrespective of its varying height or tangent.
Moving a fixed cut to the other side of the barrier transfers it to
the reflected inverse tail. The sum of the two absolute integrals
still has the lower bound. This rejects a general contour argument
which seeks to bound these pieces separately by the selected edge
action. It gives no lower bound for their signed sum, an angular
trace, or an actual filled-network scalar.

## 1. Original functions and the real upper envelope

Put \(D=N-1\), \(\eta_N=(-1)^D\), \(h=N^{-1}\), and
\[
 a_N=-h/2,\qquad b_N=(1-h)/2,\qquad
 \mathcal R_Ny=D/N-y.
 \tag{1}
\]
Use the original factorial interpolation
\[
 B_N(y,v)=\frac{N}{
 G_N(D/2-Ny+Nv/(2\pi))
 G_N(D/2-Ny-Nv/(2\pi))G_N(Ny)^2},
 \qquad F_N(y;t,u)=B_N(y,t)B_N(y,u).
 \tag{2}
\]
With \(d_v(x)=\cos v+\cos(2\pi x+\pi h)\), the actual inverse is
\[
 \begin{split}
 I_N(x;t,u)
 &=\frac{(1-\cos2\pi Nx)^2}{N^4d_t(x)d_u(x)F_N(x;t,u)}\\
 &=\frac4{N^6}(1-\cos2\pi Nx)^2G_N(Nx)^4
 \prod_{\substack{v=t,u\\ \sigma=\pm1}}
 G_N(D/2-Nx+\sigma Nv/(2\pi)-1).
 \end{split}
 \tag{2a}
\]
These are the exact equivalent expressions from the additive
regularization. The second retains the actual factorial divisors;
no pole or zero is suppressed.

Let \(J'= \Log(2\sin\pi z)\), \(J(0)=0\), with the original
continuation from \(0<z<1\). Above or below the negative real axis
use its corresponding continued branch. Their real boundary values
agree. Write this continuous real function as \(\mathcal J\), and set
\[
 \mathcal B(y,v)=
 -\mathcal J(1/2-y+v/(2\pi))
 -\mathcal J(1/2-y-v/(2\pi))-2\mathcal J(y),
 \qquad
 \mathcal E(y;t,u)=\mathcal B(y,t)+\mathcal B(y,u).
 \tag{3}
\]
Thus \(\mathcal E\) is the actual side-defined factorial envelope.
It is not obtained by replacing the canonical factorial by a single
branch through its zeros.

On the original positive component put
\[
 q^2=1+\tan^2(t/2)+\tan^2(u/2),\qquad
 \cot(\pi x^*)=q,\qquad \Re q>0.
 \tag{4}
\]
The selected critical value of the original holomorphic wire phase
is \(\psi(t,u)\). The unsummed-phase source proves this identity,
including its constant, and the product-domain source fixes the
branch and the exact contour reachability. Neither source asserts
a bound on the complementary connectors.

**Lemma 1.** For real \(v\in(-\pi,\pi)\) and
\(0<\xi<1/2\), the function
\[
              H\longmapsto\mathcal B(\xi+iH,v)
 \tag{5}
\]
is even and strictly increasing for \(H>0\). In particular it is
minimized on the real wire.

**Proof.** Set \(A=\cos^2(v/2)>0\) and \(z=\sin^2\pi y\).
For \(y=\xi+iH\), \(H>0\),
\[
 \Im z=\tfrac12\sin(2\pi\xi)\sinh(2\pi H)>0,
 \qquad \Im(A/z-1)<0.
 \tag{6}
\]
Direct differentiation of the original phase gives
\[
 b_y(y,v)=\Log\frac{A-z}{z}.
 \tag{7}
\]
On the upper wire half-strip this is the logarithm with imaginary
part in \((-\pi,0)\). To fix the lift, first approach a sufficiently
small positive real \(y\), where \(A-z>0\) and both sides have
real boundary values. The quotient in (7) stays strictly in the
lower half-plane, so continuation determines this logarithm on the
whole upper half-strip. This is also the branch of (3), with the
shifted factorial arguments approaching their negative cuts from
the prescribed side. Therefore
\[
 \partial_H\mathcal B(\xi+iH,v)
       =-\Im b_y(\xi+iH,v)>0.
 \tag{8}
\]
Conjugation preserves the real parts of the original side primitives,
including their matching boundary values on a negative cut. It
proves evenness in \(H\). Continuity at \(H=0\) completes the proof,
also when a shifted real factorial argument is zero. \(\square\)

## 2. A positive family with a strict interior barrier

Fix once and for all a closed interval
\[
             I=[\xi_-,\xi_+]\Subset(0,1/2)
 \tag{9}
\]
containing \(1/4\) in its interior, for instance \([1/5,3/10]\).
The real-potential formula of the additive source gives
\(\mathcal B(\xi,v)\ge0\) for every real \(\xi\in[0,1/2]\)
and every complex \(v\) in the admitted angular strip. Moreover
\[
 \partial_\xi\mathcal B(\xi,0)=2\log\cot(\pi\xi),\qquad
 \mathcal B(0,0)=\mathcal B(1/2,0)=0.
 \tag{10}
\]
Thus \(\mathcal B(\xi,0)>0\) for \(0<\xi<1/2\). Define
\[
                  \beta=\min_{\xi\in I}\mathcal B(\xi,0)>0.
 \tag{11}
\]
The original complete-end calibration is
\[
 \psi(t,0)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)).
 \tag{12}
\]
Consequently \(\psi(t,0)\to0\) as real \(t\uparrow\pi\), since
\(J(0)=J(1/2)=0\). Also
\[
 x^*(t,0)=\pi^{-1}\arccot(\sec(t/2))\longrightarrow0.
 \tag{13}
\]
Choose one fixed \(t_0<\pi\), sufficiently close to \(\pi\), so that
\[
 \psi(t_0,0)<\beta/8,\qquad
 x^*(t_0,0)<\xi_-/2.
 \tag{14}
\]
This is an original strictly positive pair: its tangents are real
and \(q=\sqrt{1+\tan^2(t_0/2)}>\tan(t_0/2)\).

**Proposition 2, real case.** For every \(\xi\in I\) and every
real \(H\),
\[
          \mathcal E(\xi+iH;t_0,0)\ge\beta.
 \tag{15}
\]
The selected saddle is strictly to the left of this interval and
has action less than \(\beta/8\).

**Proof.** On the real wire,
\(\mathcal B(\xi,t_0)\ge0\) and
\(\mathcal B(\xi,0)\ge\beta\). Apply Lemma 1 separately to
the two incidences. The remaining assertions are (14).
\(\square\)

The real case already rules out a theorem over the full positive
domain. The following extension verifies that this is not confined
to real angular data.

**Proposition 3, complex stability.** There is a compact
neighborhood \(\mathcal U\) of \((t_0,0)\), with nonempty interior,
contained in the original positive domain and in
\(\{|\Re t|,|\Re u|<\pi\}\), such that uniformly on \(\mathcal U\),
\[
 \begin{split}
 \mathcal E(\xi+iH;t,u)&\ge3\beta/4
                     &&(\xi\in I,\ H\in\mathbb R),\\
 \Re\psi(t,u)&<\beta/4,\qquad
 |\Im t|+|\Im u|<\beta/8,\qquad
 \Re x^*(t,u)<\xi_-/2.
 \end{split}
 \tag{16}
\]
Its interior contains pairs with both \(\Im t<0\) and \(\Im u<0\).

**Proof.** First take a compact neighborhood in the positive domain
on which the original branches in (4) and \(\psi\) are holomorphic.
Strict positivity and regularity at the real base point supply it.
It may be chosen so that, for \(\xi\in I\), the limiting real
midpoint arguments
\(1/2-\xi\pm t/(2\pi)\) and
\(1/2-\xi\pm u/(2\pi)\) all stay a fixed distance from zero
and from the ends \(-1,1\). Exactly the minus-\(t\) argument
has negative real part; the other three have positive real part.

Here the control for all \(H\), rather than only a bounded range,
follows directly from the original side branches. Uniformly for
\(r\) in a compact subinterval of \((-1,1)\),
\[
 \begin{split}
 \Log(2\sin\pi(r+iY))
   &=-i\pi(r+iY)+i\pi/2+O(e^{-2\pi Y}) &&(Y\to+\infty),\\
 \Log(2\sin\pi(r-iY))
   &= i\pi(r-iY)-i\pi/2+O(e^{-2\pi Y}) &&(Y\to+\infty).
 \end{split}
 \tag{17}
\]
These follow from the exact factorizations
\(2\sin\pi z=i e^{-i\pi z}(1-e^{2\pi iz})\) above and
\(2\sin\pi z=-i e^{i\pi z}(1-e^{-2\pi iz})\) below.
The logarithms in (17) are their continued original lifts, not
principal arguments reset on the negative-real side. Integrating
vertically, with the original primitive constant, gives
\[
             \mathcal J(r+iY)=\pi|Y|(r-1/2)+O(1)
                       \qquad(|Y|\to\infty).
 \tag{18}
\]
The error is uniform on the stated real compact, because the
exponential remainder is integrable and the initial-height values
are continuous there.

Substitution in (3), with the bounded angular imaginary parts
retained, yields
\[
 \mathcal B(\xi+iH,v)=\pi|H|+O(1),\qquad
 \mathcal E(\xi+iH;t,u)=2\pi|H|+O(1),
 \tag{19}
\]
uniformly on the initially fixed parameter neighborhood and \(I\).
Choose \(M_0\) so that this is greater than \(\beta\) for
\(|H|>M_0\). On \(I\times[-M_0,M_0]\), the side real primitives
are jointly continuous, including their matching negative-cut
values. Shrinking the parameter neighborhood and using (15)
therefore gives the first line of (16) on this compact range,
while the already fixed large-height estimate covers the rest.
Continuity of the selected phase and saddle, followed by one more
shrink, gives the other inequalities. Take the closure of a
sufficiently small open bidisk. Such a bidisk contains pairs with
both angular imaginary parts strictly negative. \(\square\)

## 3. Actual finite factors on a polynomial-distance slab

**Lemma 4.** For every fixed height bound \(0\le M<\infty\) there are
\(c_M>0\), \(N_0\), and a fixed \(\gamma>0\), such that for
every \(N\ge N_0\) and \((t,u)\in\mathcal U\) there is an interval
\[
 J_N=[\xi_N-\ell_N/2,\xi_N+\ell_N/2]\subset I,\qquad
                         \ell_N=\frac1{20N},
 \tag{20}
\]
on whose entire vertical slab \(|\Im y|\le M\) both factors are
regular and satisfy
\[
 \begin{split}
 |F_N(y;t,u)|&\ge c_M N^{-2}
                      e^{N(\Re\psi(t,u)+\gamma)},\\
 |I_N(\mathcal R_Ny;t,u)|&\ge c_M N^{-2}
                      e^{N(\Re\psi(t,u)+\gamma)}.
 \end{split}
 \tag{21}
\]
One may take \(\gamma=\beta/4\). The constants are uniform on
\(\mathcal U\). The slab may depend on the parameters and on \(N\).

**Proof.** Exclude the at most five real arithmetic lattices
\[
 N^{-1}\mathbb Z,\qquad
 b_N\pm\Re v/(2\pi)+N^{-1}\mathbb Z
                    \quad(v=t,u).
 \tag{22}
\]
They include every real projection of a shifted factorial zero
of \(F_N(y)\), every shifted factorial pole of
\(I_N(\mathcal R_Ny)\) in the relevant wire range, and the
zeros of \(1-\cos2\pi Ny\). The unshifted factorials have no
zero or pole here: \(\Re y\in I\Subset(0,1/2)\) and
\(\Re\mathcal R_Ny\) stays in a compact subinterval of \((1/2,1)\).

Take a full period cell of length \(1/N\) in the interior of \(I\).
The at most five excluded points on its periodic circle leave a
gap of length at least \(1/(5N)\). Choose its midpoint, translating
the period cell if needed to stay inside \(I\), and take the
interval (20) about it. Every point of \(J_N\) has distance at
least \(1/(20N)\) from all the lattices (22). This choice is
uniform for sufficiently large \(N\); coincident lattices only
increase the available gap.

For nonnegative real midpoint arguments the exact two-sided estimate is
\[
 |G_N(Nz-1/2)|\asymp_M\sqrt N\,e^{N\mathcal J(z)}.
 \tag{23}
\]
For negative real part the exact reflection is
\[
 \frac1{G_N(Nz-1/2)}
       =\frac{2\cos(\pi Nz)}{N}G_N(-Nz-1/2).
 \tag{24}
\]
On the slab, (22) gives
\[
       |2\cos(\pi Nz)|\ge c e^{\pi N|\Im z|}
 \tag{25}
\]
for the negative midpoint arguments that occur. For bounded
\(N|\Im z|\), use the distance \(c/N\) from a cosine zero.
For larger \(N|\Im z|\), use the two elementary exponentials
in the cosine. The original side identity
\(\mathcal J(z)=-\mathcal J(-z)-\pi|\Im z|\)
then makes (23)--(25) a two-sided reciprocal estimate, with
fixed constants on the bounded-height argument compact.

All limiting real arguments are separated from zero by the choice
of \(\mathcal U\). The unshifted midpoint argument is \(y+h/2\);
the shifted ones are \(1/2-y\pm v/(2\pi)\). Their displacement
from the arguments in (3) costs only a bounded multiplicative
factor. The eight reciprocal-factorial occurrences in \(F_N\),
together with its numerator \(N^2\), consequently give
\[
             |F_N(y;t,u)|\ge c_M N^{-2}
                                      e^{N\mathcal E(y;t,u)}.
 \tag{26}
\]
No lower estimate at a factorial zero is asserted; the slab was
chosen specifically to exclude their real projections.

For the inverse use the exact meromorphic reflection ratio
\[
 \frac{I_N(\mathcal R_Ny;t,u)}{F_N(y;t,u)}
 =\frac{(1-\cos2\pi Ny)^2}
 {(\cos Nt-\eta_N\cos2\pi Ny)
  (\cos Nu-\eta_N\cos2\pi Ny)}.
 \tag{27}
\]
It follows directly by multiplying the two original halfwire
reflection identities; \(d_v(\mathcal R_Ny)=d_v(y)\) and
\(\cos(2\pi N\mathcal R_Ny)=\cos2\pi Ny\). Thus every phase
and parity in (27) is retained.

On (20), the first lattice in (22) and
\(1-\cos2z=2\sin^2z\) give
\[
 |1-\cos2\pi Ny|\ge c e^{2\pi N|\Im y|}.
 \tag{28}
\]
The denominator of (27) is at most
\[
 4\exp N\{\max(|\Im t|,2\pi|\Im y|)
                +\max(|\Im u|,2\pi|\Im y|)\}.
 \tag{29}
\]
It is nonzero on this slab: its zero projections are included
in (22). In particular
\[
 \left|\frac{I_N(\mathcal R_Ny;t,u)}{F_N(y;t,u)}\right|
    \ge c\,e^{-N(|\Im t|+|\Im u|)}.
 \tag{30}
\]
For real \(t,u\), the lower bound is a fixed positive constant.
Combining (16), (26), and (30) yields respectively the rates
\(3\beta/4\) and \(5\beta/8\). Each exceeds
\(\Re\psi+\beta/4\), since \(\Re\psi<\beta/4\).
This proves (21). \(\square\)

## 4. Crossing the slab uses total variation

For a rectifiable parameterized path \(\gamma\), define
\[
 \mathcal A_N(\gamma;f)
       =N\int_\gamma |f(y)|\,|dy|.
 \tag{31}
\]
This is the absolute integral with the original wire multiplier.
It is not the absolute value of the signed integral.

**Theorem 5.** Let \(\gamma\) lie in \(|\Im y|\le M\), with
one endpoint strictly to the left of \(J_N\) and the other
strictly to its right. Then
\[
 \mathcal A_N(\gamma;F_N)\ge
           c_M N^{-2}e^{N(\Re\psi+\gamma_0)},\qquad
 \mathcal A_N(\gamma;I_N\circ\mathcal R_N)\ge
           c_M N^{-2}e^{N(\Re\psi+\gamma_0)},
 \tag{32}
\]
where \(\gamma_0=\beta/4\). The paths must be admissible for the
factor being integrated; any extra poles remain excluded.

**Proof.** Parameterize a rectifiable path by arclength, so it
is Lipschitz. If \(J_N=[l_N,r_N]\), clamp its real projection:
\[
 p(s)=\min\{r_N,\max\{l_N,\Re\gamma(s)\}\}.
 \tag{33}
\]
Almost everywhere,
\[
 |p'(s)|\le
 \mathbf 1_{\{\Re\gamma(s)\in J_N\}}|\Re\gamma'(s)|
 \le\mathbf 1_{\{\Re\gamma(s)\in J_N\}}|\gamma'(s)|.
 \tag{34}
\]
The endpoint difference of \(p\) has modulus \(r_N-l_N=\ell_N\).
Hence the path's total variation inside the vertical slab is at
least \(\ell_N\), regardless of backtracking, vertical motion,
or changes in the argument of \(dy\). Apply (21) on that portion:
\[
 N\int_\gamma |f|\,|dy|
 \ge N c_M N^{-2}e^{N(\Re\psi+\gamma_0)}
                                    \ell_N.
 \tag{35}
\]
Since \(\ell_N=1/(20N)\), this is (32). An infinite absolute
integral satisfies the same assertion. No claim about cancellation
in the signed integral was used. \(\square\)

**Corollary 6, moving the fixed cut does not remove the barrier.**
Let \(\ell\) have real part below \(\xi_-\), and let \(r\) have
real part above \(\xi_+\). Choose any common cut point \(c\).
Let \(\gamma_F:\ell\to c\) and
\(\gamma_I:\mathcal R_N r\to\mathcal R_N c\) be admissible
rectifiable paths. Suppose both \(\gamma_F\) and the reflected
path \(\mathcal R_N\gamma_I\) stay in \(|\Im y|\le M\). Then
\[
 \mathcal A_N(\gamma_F;F_N)
       +\mathcal A_N(\gamma_I;I_N)
 \ge c_MN^{-2}e^{N(\Re\psi+\gamma_0)}.
 \tag{36}
\]
At least one of the two terms has at least half this bound.
The cut may depend on the parameter pair or on the level.

**Proof.** Concatenate \(\gamma_F\) with the reversal of
\(\mathcal R_N\gamma_I\). This is a path from \(\ell\) to \(r\).
Both integrands have the same lower bound (21) whenever their
respective path portions lie in the slab. Apply the projection
argument (33)--(35) to the concatenated path. Reflection preserves
\(|dy|\), so the absolute integral of its second portion is exactly
the second term of (36). This proof does not require either
individual path to cross the entire slab. \(\square\)

For the collar decomposition, take
\(r=\mathcal R_N(a_N-iH)=a_N+1+iH\), and let \(\ell\) be
its fixed left core cut, lying to the left of \(I\).
The main core ends at \(c\); the extended inverse path starts at
\(a_N-iH\) and ends at \(\mathcal R_Nc\). These are exactly
the endpoint arrangements in Corollary 6. Thus choosing a longer
reflected tail cannot make both pieces satisfy an absolute
own-\(\psi\) bound on this positive family. The obstruction is
interior, not an excessive value at an original wire endpoint.

## 5. Source scope

This concerns the same-index edge (2). All functions in (21), (27),
and (36) are the actual canonical
factorial functions with their original normalization. The estimates
hold for any fixed finite height bound \(M\), uniformly on the chosen
compact positive family. They do not treat wire heights increasing
without bound with \(N\). A pointwise phase bound already fails at
all heights by (16); the finite-factor constants are asserted only
on the stated bounded-height families.

The full original angular traces have not been taken. The prescribed
angles are held fixed along these wire paths. Shared angular motion,
signed interference between contour pieces, null representatives
under the complete Hermite traces, and the associated angular
boundary currents are all possible sources of cancellation. The
argument neither excludes nor estimates them.

In particular there is no lower bound for
\(\left|N\int F_N\,dy\right|\), for the coherent main-plus-inverse
sum, or for a filled-network scalar. Nor is this family asserted
to solve every original integer filling equation. It disproves
the proposed absolute wire-contour theorem on the general positive
domain and identifies why a coherent source argument is still
needed. It changes no proved filling theorem.

## Direct sources and author audit

The following complete direct texts were read in this author sequence,
their used implications checked, and their pins verified.

- [Positive wire product contour](research_positive_wire_product_contour.md):
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230;
  positive criterion, stationary branch, original factorial domain
  and fixed-endpoint contour reachability.
- [Unsummed network phase](research_unsummed_network_phase_coercivity.md):
  SHA256 b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e;
  original incidence phase, critical value \(\psi\), branch constants
  and the distinction between local Morse and whole-source bounds.
- [Mixed wire phase](research_mixed_wire_phase_concavity.md):
  SHA256 374211e9f7d6e96e1ef328423481ce92c999082fc90f889411be23de45c31283;
  complete-end calibration (12) in the original normalization.
- [Uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md):
  SHA256 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11;
  two-sided midpoint estimate, exact negative-side reflection and
  original side branches.
- [Additive half-wire source](research_additive_half_wire_source_regularization.md):
  SHA256 af8daf3eaa16303f8297b4a712ee9debe31cabc7326776fc34c9b185f0d216a0;
  actual inverse and reflection constants, real-potential positivity,
  full divisors and retained source scope.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
