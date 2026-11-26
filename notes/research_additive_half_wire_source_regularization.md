# Additive regularization of the reflected half of an original wire

Private written proof, 16 November 2026.

The exact factorial reflection gives a two-variable representative of
the original same-index kernel in which the reflected half has no
large angular Chebyshev carriers. The change is additive and belongs
to the full two-endpoint Hermite ideal. The replacement has explicit
moving poles; they are retained. Grouped residues of these poles are
source-null on their stated parameter neighborhoods.

On any compact angular set a finite choice of thin horizontal contours
bounds the inverse half by an arbitrarily small exponential rate.
Every compact positive edge set has a strictly positive original
action reserve against that rate. This does not bound the main half,
glue the local meromorphic representatives into one bounded holomorphic
representative, or discard their connecting currents.

## 1. Original normalization and an exact reflection

Let
\[
 N\ge2,\quad h=N^{-1},\quad D=N-1,\quad\eta=(-1)^D,
 \qquad P_N(z)=2T_N(z/2)+2,
\]
\[
 a_N=-h/2,\qquad b_N=(1-h)/2,\qquad
 \mathcal R x=D/N-x,\qquad w_t=-2\cos t.
 \tag{1}
\]
Thus \(\mathcal R a_N=a_N+1\) and \(\mathcal R b_N=b_N\).
Use the original factorial halfwire
\[
 B_N(x,t)=\frac{N}{G_N(A_t)G_N(B_t)G_N(Nx)^2},
 \quad A_t=D/2-Nx+Nt/(2\pi),\quad
 B_t=D/2-Nx-Nt/(2\pi).
 \tag{2}
\]
The symbol \(B_t\) in a factorial argument is distinguished from
the function \(B_N\). Put
\[
 F_N(x;t,u)=B_N(x,t)B_N(x,u),\quad
 d_t(x)=\cos t+\cos(2\pi x+\pi h),\quad
 c_N(x)=\cos(2\pi Nx).
 \tag{3}
\]
All formulas below retain the original unmarked sine factorial;
no crossing carrier is changed.

The pinned factorial identities are
\[
 G_N(z+1)=2\sin(\pi(z+1)/N)G_N(z),\qquad
 G_N(z)G_N(D-z)=N.
 \tag{4}
\]
Multiplying the first identity through a full period gives
\(G_N(z+N)=-2\sin(\pi z)G_N(z)\). Applying this at \(-z\)
and then (4) proves, meromorphically,
\[
 G_N(z)G_N(-z)=N\frac{\sin(\pi z/N)}{\sin(\pi z)}.
 \tag{5}
\]
Consequently
\[
 \boxed{\quad
 B_N(x,t)B_N(\mathcal R x,t)
       =\frac{\cos(Nt)-\eta c_N(x)}{N^2d_t(x)}.
 \quad}
 \tag{6}
\]
For completeness, the factorial arguments at \(\mathcal R x\)
are \(-B_t,-A_t\), and \(G_N(D-Nx)=N/G_N(Nx)\).
Equation (5) therefore reduces the product to
\(N^{-2}\sin(\pi A_t)\sin(\pi B_t) /
 [\sin(\pi A_t/N)\sin(\pi B_t/N)]\).
The two sine products are respectively
\((\cos Nt-\eta c_N(x))/2\) and \(d_t(x)/2\).
This proves the normalization and sign in (6).

Define the meromorphic inverse half
\[
 I_N(x;t,u)=
 \frac{(1-c_N(x))^2}{N^4d_t(x)d_u(x)F_N(x;t,u)}.
 \tag{7}
\]
Writing \(P_t=P_N(w_t)\), the exact identity
\(\cos Nt=\eta(1-P_t/2)\) gives
\[
 \boxed{\quad
 F_N(\mathcal R x;t,u)-I_N(x;t,u)
 =\frac{-(1-c_N(x))(P_t+P_u)/2+P_tP_u/4}
        {N^4d_t(x)d_u(x)F_N(x;t,u)}.
 \quad}
 \tag{8}
\]
This is an additive identity. It has no logarithm of a period
multiplier and does not change the main halfwire phase.

The apparent rational denominators in (7) have a useful exact
factorial form. The first identity in (4) gives
\[
 \frac{1}{d_t(x)B_N(x,t)}
   =\frac2N G_N(A_t-1)G_N(B_t-1)G_N(Nx)^2,
 \tag{9}
\]
and hence
\[
 I_N(x;t,u)=\frac4{N^6}(1-c_N(x))^2G_N(Nx)^4
       \prod_{v\in\{t,u\}}G_N(A_v-1)G_N(B_v-1).
 \tag{10}
\]
In particular one must use its actual divisors, rather than treating
the denominator of (7) as a nonvanishing formal symbol.

## 2. A full two-endpoint source identity

For \(H>0\), orient
\[
 \gamma_{N,H}^{\pm}=[a_N,b_N]\pm iH
\]
from left to right. Define, whenever these integrals are holomorphic
in their parameters,
\[
 \widehat K_{N,H}(t,u)
       =N\int_{a_N+iH}^{a_N+1+iH}F_N(x;t,u)\,dx,
 \tag{11}
\]
\[
 \boxed{\quad
 K^{\rm reg}_{N,H}(t,u)
       =N\int_{\gamma^+_{N,H}}F_N(x;t,u)\,dx
        +N\int_{\gamma^-_{N,H}}I_N(x;t,u)\,dx.
 \quad}
 \tag{12}
\]
Splitting (11) at \(b_N+iH\) and substituting
\(x\mapsto\mathcal R x\) in its right half gives exactly
\[
 \widehat K_{N,H}
   =N\int_{\gamma^+_{N,H}}F_N
       +N\int_{\gamma^-_{N,H}}F_N(\mathcal R x).
 \tag{13}
\]
Both orientations in this formula are compulsory.

**Theorem 1.** The function (12) is even in each angle. It is
holomorphic on
\[
 |\Re t|,|\Re u|<\pi,\qquad
 |\Im t|,|\Im u|<2\pi H.
 \tag{14}
\]
Its full Hermite class at both endpoints is exactly
\[
 K_T(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w).
 \tag{15}
\]
This includes every mixed first spectral normal, both parities,
and the simple-node convention at odd levels. Thus it may replace
an internal same-index edge before any original traces are taken.
It is not asserted to equal the ordinary free-boundary polynomial.

**Proof.** On the original period strip, (2) is holomorphic for
\(|\Re t|<\pi\). This is the pinned reciprocal-factorial divisor
check, which applies at every fixed finite height. The full Hermite
class of each halfwire is its original half-band cardinal function.
The product has integer frequencies in \([-D,D]\). Its period
integral is therefore exactly \(1/N\) times the original sum (15),
including both endpoint jets. This proves the assertion for (11).

On the lower halfwire, all four shifted factors in (10) have
nonzero imaginary part in (14). The unshifted factor also stays
off its real poles. The divisor theorem proves holomorphy there.
The same argument makes the coefficients of \(P_t,P_u\) in (8)
holomorphic near the full physical parameter grid. Integrating
(8) and using (13) proves that the difference of (11) and (12)
belongs to the ideal \((P_t,P_u)\) on such a neighborhood.
This preserves the full tensor Hermite class, not just values.
Evenness is immediate from the paired arguments in (2) and (10).

At an odd simple spectral node only its value is required. Its
angular pullback is a double zero of \(P_N(-2\cos t)\), and the
even functions in question descend through \(t=0\). No extra
spectral normal is imposed there. This also proves the statement
at \(N=2\). \(\square\)

It is essential that the split uses the two nonreal half paths.
A substitution at the real odd fold can produce a spurious
\(0/0\): at \(x=b_N\), \(N\) odd, and \(t=u=0\), simply
declaring the numerator in (7) to be zero would lose the actual
simple-node value. The holomorphic source proof above makes no
such declaration.

## 3. Actual poles, grouped residues, and retained transitions

The complete factorial divisor is
\[
 \operatorname{ord}_{z=k}G_N(z)=\lfloor k/N\rfloor
       \quad(k\in\mathbb Z),
\]
with no other zeros or poles. In the half strip
\(a_N\le\Re x\le b_N\), and for \(|\Re t|,|\Re u|<\pi\),
the possible new poles of (10) lie at
\[
 x=b_N\pm t/(2\pi)+r/N,
 \qquad x=b_N\pm u/(2\pi)+r/N,
 \qquad r=0,1,2,\ldots .
 \tag{16}
\]
Only \(O(N)\) of these lie in this strip on any bounded angular
set. In fact each eligible shifted factorial pole here is simple:
its index has absolute value less than \(N\). Coincident factors
can give order at most four, before zeros of the numerator are
taken into account. The factor \(G_N(Nx)^4\) has no pole in this
half strip. Some of the listed poles can be removable; (16) is a
complete possible divisor list, not a claim that every pole survives.

At a \(t\)-wall in (16),
\[
 c_N(x)=\eta\cos Nt,
             \qquad 1-c_N(x)=P_t/2.
 \tag{17}
\]
The analogous statement holds at a \(u\)-wall. Individual residue
formulas at colliding walls need not have holomorphic separate
denominators. The following grouped formulation avoids that error.

**Proposition 2.** Fix a small closed wire contour enclosing a
cluster of the poles (16), with no pole on the contour for parameters
in an open neighborhood. Require that the original reflected
integrand is holomorphic inside this contour and that the
coefficients in (8) are holomorphic on it. Then the sum of the
enclosed residues of \(I_N\) is holomorphic in the parameters and
has the form
\[
                    P_t A_N(t,u)+P_u B_N^{\rm res}(t,u)
 \tag{18}
\]
with holomorphic coefficients on that neighborhood.

**Proof.** Integrate (8) on the fixed contour. The integral of
the original reflected term is zero. The coefficients of its
explicit \(P_t,P_u\) factors are contour integrals of functions
holomorphic on the contour, so are holomorphic in the parameters.
The residue theorem proves (18), including collisions. Derivatives
in either parameter commute with this fixed integral. Thus, on a
neighborhood of physical parameters, all required mixed physical
jets of (18) vanish. \(\square\)

This is a local source statement. A grouped residue can be deleted
inside a subsequent complete original trace only where its stated
holomorphic representative is valid at the physical parameters
being used. No global analytic continuation of an individual
residue formula through every collision is assumed.

All height transitions also retain their boundary pieces. Put
\[
 C_{N,H}=N\int_{\gamma^-_{N,H}}
                   [F_N(\mathcal R x)-I_N(x)]\,dx,
 \qquad K^{\rm reg}_{N,H}=\widehat K_{N,H}-C_{N,H}.
 \tag{19}
\]
For \(0<H_1<H_2\), Cauchy's theorem on the original full wire
rectangle gives
\[
 \widehat K_{N,H_2}-\widehat K_{N,H_1}
  =N\int_{a_N+iH_1}^{a_N+iH_2}
             [F_N(x+1)-F_N(x)]\,dx .
 \tag{20}
\]
The exact halfwire period multiplier is
\[
 B_N(x+1,t)=
 \left(\eta+\frac{(-1)^NP_t}{4\sin^2(\pi Nx)}\right)B_N(x,t).
 \tag{21}
\]
Thus (20) is explicitly in \((P_t,P_u)\); its seam denominator
does not vanish on the displayed midpoint segment. Combining
(19)--(20) gives the exact transition for (12). If a deformation
of the two \(C\)-integrals crosses poles, its clustered residues
and both endpoint segments remain in that formula. The inverse
halves alone are not asserted to have source-null height differences.

## 4. Nonnegative real-wire logarithmic potential

Let \(J'(z)=\Log(2\sin\pi z)\), with \(J(0)=0\) and the
original continuation from \((0,1)\). For negative real part use
the upper or lower continuation according to the side of the
argument; their real boundary values on the negative axis agree.
Write this continuous real function as \(\mathcal J(z)\).
Near zero it has the usual continuous \(z\log z\) behavior.

For real \(0\le x\le1/2\), define
\[
 \mathcal B(x,t)=
 -\mathcal J(1/2-x+t/(2\pi))
 -\mathcal J(1/2-x-t/(2\pi))-2J(x).
 \tag{22}
\]
The expression is continuous, including the moving real zeros.
It is the real part of the original halfwire phase on each
regular side chart; no branch-dependent real carrier is reset.

**Lemma 3.** For every \(|\Re t|<\pi\) and real
\(0\le x\le1/2\),
\[
 \mathcal B(x,t)
   =\int_0^x\log|2\cos(2\pi r)-w_t|\,dr-2J(x)\ge0.
 \tag{23}
\]

**Proof.** At \(x=0\), the reflected arguments sum to one,
so (22) is zero, with the normalization fixed by the exact
factorial reflection. Away from its integrable logarithmic zeros,
its derivative is
\[
 \partial_x\mathcal B
 =\log\left|\frac{\cos(2\pi x)+\cos t}
                         {1-\cos(2\pi x)}\right|.
 \tag{24}
\]
This proves the equality in (23), also across zeros by continuity.

First take a real angle \(t\). The derivative is positive until
its unique maximum point before the numerator zero. It is negative
thereafter: after that zero, its numerator has magnitude
\(-\cos(2\pi x)-\cos t<1-\cos(2\pi x)\), unless the phase
is the identically zero endpoint case. Both endpoint values are
zero. To check the right endpoint directly, factor
\(2\cos\phi-2\cos\theta
=-4\sin((\phi+\theta)/2)\sin((\phi-\theta)/2)\).
The integral of its logarithmic absolute value on \([0,\pi]\)
is independent of \(0<\theta<\pi\), by reflection of the two
sine integrals; at \(\theta=0\) it is
\(4\int_0^{\pi/2}\log(2\sin v)\,dv=0\).
Also \(J(1/2)=0\). Continuity includes both endpoint colors.
Hence (23) is nonnegative
for \(w_t\in[-2,2]\), including the limiting endpoints.

For an arbitrary complex \(w\), clamp its real part to
\(v\in[-2,2]\). For every \(y\in[-2,2]\),
\(|y-w|\ge|y-v|\). Applying this pointwise in the integral
proves the inequality for every complex \(w\), and in particular
for the stated angular parameters. \(\square\)

## 5. A finite thin-height atlas for the inverse half

Fix a compact set \(\mathcal K\) in
\(\{|\Re t|,|\Re u|<\pi\}\), with bounded heights. Work first
on one fixed slightly larger compact set in that domain. Its
constants and real-continuity modulus are chosen before the thin
height. For sufficiently small \(\epsilon>0\), take the five levels
\[
 H_\ell=\epsilon(1+\ell/4),\qquad 0\le\ell\le4.
 \tag{25}
\]
For any parameter pair, at least one level has distance at least
\(\epsilon/16\) from both \(|\Im t|/(2\pi)\) and
\(|\Im u|/(2\pi)\): each forbidden interval excludes at most
one of the five levels. The open sets where these distances exceed
\(\epsilon/32\) form a finite cover, with the larger margin
available for uniform estimates on smaller closed pieces.

**Theorem 4.** There is a function \(\omega_{\mathcal K}(s)\to0\)
as \(s\downarrow0\) such that, on those closed chart pieces,
\[
 \left|N\int_{\gamma^-_{N,H_\ell}}I_N(x;t,u)\,dx\right|
 \le C_{\mathcal K,\epsilon}N^{-1}
       \exp\{N[8\pi\epsilon+\omega_{\mathcal K}(2\epsilon)]\}.
 \tag{26}
\]
Every fixed number of parameter derivatives has the same exponential
rate with a polynomial factor. Each local integral is holomorphic
on its parameter chart. Its source interpretation remains Theorem 1
and the explicitly retained meromorphic continuation and transitions
of Section 3.

**Proof.** All shifted factorial arguments in (10), divided by
\(N\) and put into midpoint form, have imaginary parts separated
from zero by \(c\epsilon\). Their real parts lie in a fixed interval
\([-1+\delta,1-\delta]\), for \(\delta>0\) depending only on
the larger angular compact set. The unshifted midpoint argument is
\(x+h/2\), with real part in \([0,1/2]\) and imaginary part
\(-H_\ell\).

The pinned midpoint estimate bounds \(G_N(Nz-1/2)\) by
\(C\sqrt N e^{N\mathcal J(z)}\) for nonnegative real part.
For negative real part use the exact identity
\[
 G_N(Nz-1/2)=
       \frac{N}{2\cos(\pi Nz)G_N(-Nz-1/2)}.
 \tag{27}
\]
The lower midpoint bound for the last factorial and
\(|1+e^{\pm2\pi iNz}|\ge1-e^{-2\pi N|\Im z|}\)
give the same upper bound on the appropriate side. The required
denominator is uniformly bounded below here because
\(|\Im z|\ge c\epsilon\). Thus no proximity to a factorial
pole is hidden in the estimate.

In (10), the four shifted factors give \(O(N^2)\), and
\(G_N(Nx)^4\) gives \(O(N^2)\), in addition to their phases.
After the outside factor \(N\), the remaining power is \(N^{-1}\).
The shifts by \(h\) or \(h/2\) in the midpoint arguments cost
a bounded factor: their imaginary parts have the fixed separation
just obtained. Consequently the integrand, including this outside
\(N\), is bounded by
\[
 C N^{-1}\exp N\{4\pi H_\ell
              -\mathcal B(x,t)-\mathcal B(x,u)\},
 \tag{28}
\]
where (22) is continued by its side-defined real expression to
the thin complex wire strip. We used
\(|1-\cos(2\pi Nx)|^2\le4e^{4\pi N H_\ell}\).

The side-defined real primitive is uniformly continuous on the
fixed compact argument sets, including their real turning cuts.
Move the real coordinate into \([0,1/2]\), at a cost \(O(h)\)
near the left endpoint. Lemma 3 then bounds the last two terms
in (28) above by a modulus tending to zero with the wire height.
At the displaced left endpoint the unshifted imaginary part is
at least \(\epsilon\), so its \(O(h)\) change also costs only
a bounded factor. Increasing one fixed continuity modulus absorbs
both halfwires. Since \(H_\ell\le2\epsilon\) and the path length
is \(1/2\), this proves (26).

For derivatives use slightly smaller parameter chart pieces and
Cauchy on disks of radius \(c/N\). The pole-line separation
persists. The side phases have bounded derivatives on these
fixed separated charts, so the change of exponent is bounded;
Cauchy costs only a fixed power of \(N\). \(\square\)

These contours have a fixed scaled distance from their poles,
which is stronger than a distance \(N^{-C}\). The estimate does
not assert a globally chosen height or globally holomorphic
representative when the local chart changes.

## 6. The positive action reserve and the remaining problem

On the original positive edge domain, the proved global monotonicity
applied to \((t,u)\) and \((\bar t,\bar u)\) gives
\[
 \Im t\,\Im r_t+\Im u\,\Im r_u\ge0.
 \tag{29}
\]
Indeed conjugation preserves that domain and the original branches;
the monotonicity expression is four times the left side. It is
strict when the two configurations differ. The original absolute
volume identity therefore implies
\[
 \Re\psi(t,u)=\frac{V_e(t,u)}{2\pi}
       +\frac{\Im t\,\Im r_t+\Im u\,\Im r_u}{\pi}>0.
 \tag{30}
\]
Every original tetrahedron is positive, so \(V_e>0\). A compact
positive edge set has a positive minimum of \(\Re\psi\).
Choosing \(\epsilon\) after this compact set makes the inverse-half
rate in (26) strictly smaller than that minimum.

This is a reserve for the local inverse terms, not a whole edge
asymptotic. The main half in (12) still has to be put on a contour
with its own \(\psi\) bound, including both of its endpoints.
The local thin-height representatives have explicit pole transitions
and connecting segments; only the grouped residue statements proved
above are source-null. No subexponential analytic gluing theorem has
been invoked. In particular ordinary sheaf existence or a formal
periodicization does not supply the missing bounds.

The result is a representation change for an internal original
same-index edge. It gives neither a physical-turn closure theorem,
a free-boundary polynomial replacement, a nonzero whole-source
coefficient, nor a volume theorem for an additional filling class.

## Direct sources and author audit

The following complete source texts were read in this author sequence
or retained from its immediately preceding full reads; their directly
used identities were rechecked at the displayed versions.

- `exact_factorial_interpolation_and_complex_contours.md`:
  `1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72`;
  exact sine recurrence, normalization, and reflection.
- `research_factorial_rectangle_divisor_criterion.md`:
  `462b8c22c73f73b12152bca96cf6636708dcf153c2cbc2751458454827b3ddf8`;
  the complete factorial divisor and reciprocal holomorphy.
- `research_joint_factorial_lens_relative_source.md`:
  `a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54`;
  original halfwire, full Hermite cardinal class, paired period
  averaging, period defect, and free-boundary restriction.
- `research_uniform_factorial_and_boundary_decay.md`:
  `4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11`;
  two-sided midpoint estimate, exact negative-side reflection, and
  the original side branches.
- `research_positive_edge_global_monotonicity.md`:
  `da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500`;
  positive domain, conjugation, original branches, global monotonicity.
- `research_positive_edge_volume_identity.md`:
  `669722d49e292bf64d839901b350226b9d878c1b240d148193b09a927ef7b88e`;
  original eight-cell volume and its absolute boundary-work identity.

Only written mathematics, source reads, and metadata hashes were used.
No mathematical program, numerical calculation, test, or compilation
was run. Adopted notes and public manuscripts were not edited.
