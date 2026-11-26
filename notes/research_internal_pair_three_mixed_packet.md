# A mixed-polarization packet for the original internal power-three pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The exact circle interpolation of an internal Newton wire permits a
local packet at the selected wire coordinate of the internal \(3,3\)
pair. Only one complete-meridian trace is taken in this packet. Its
other incident edge ends at an ordinary free boundary, retained near
the complete point. The proof uses the original full-Hermite source,
one remaining wire sum, and a trace-first contour with all endpoint
and higher-charge terms.

This is a local theorem in the internal wire coordinate. It does not
bound the remainder of its complete circle, and consequently does not
yet prove the asymptotic of the closed internal \(3,3\) pair.
Section 7 additionally controls the full central interval
\(7/100\le\Re x\le3/10\) at the selected height, including its
actual nonzero contribution to the circle integral.
The separate [full pair theorem](research_internal_pair_three_full_boundary_packet.md)
combines this local result with the other three portions of the
circle and proves the complete two-boundary asymptotic.

## 1. The exact mixed source

Use \(D=N-1\), \(\eta=(-1)^D\), the original Newton polynomials,
crossing \(R\), and full trace \(\phi_N\). Let
\[
 K_N(t,u)=\sum_{j=0}^D e_j(-2\cos t)e_j(-2\cos u),\qquad
 C_{N,3}=\exp\!\left(\frac{3\pi iD^2}{4N}\right).
 \tag{1}
\]
The quotient-valued interpolation of the
[exact circle-averaging theorem](research_internal_wire_exact_circle_averaging.md)
is
\[
 \mathbf B_N(x)=\frac1N\sum_{j=0}^D
   \sum_{\ell=-D/2}^{D/2}
       e_j e^{2\pi i\ell(x-j/N)}.
 \tag{2}
\]
The frequency increment in this sum is one. Define the original
mixed source
\[
 W_{3,N}(x,u)=
       \phi_N\!\left[R^3\mathbf B_N(x)K_N(\,\cdot\,,u)\right].
 \tag{3}
\]
It is entire and half-band in \(x\), and is the original boundary
polynomial in \(-2\cos u\). At \(x=j/N\), it is exactly
\(\phi_N[R^3e_jK_N(\cdot,u)]\).

At every physical spectral value and its required first normal,
\(\mathbf B_N(x)\) is represented by
\[
 B_N(x,t)=
 \frac{N}{
   G_N(N(1/2-x+t/(2\pi))-1/2)
   G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{4}
\]
Here \(G_N\) is the original canonical sine factorial. The numerator
is exactly \(N\), by its reflection identity. Formula (4) need not
equal the canonical polynomial away from the physical jets. This
causes no replacement error in (3): the trace depends on precisely
those full jets, which agree before any contour deformation.

The phase and its branches are
\[
 \begin{split}
 J'(z)&=\log(2\sin\pi z),\qquad J(0)=0,\\
 b(x,t)&=-J(1/2-x+t/(2\pi))
          -J(1/2-x-t/(2\pi))-2J(x),\\
 F_x(y,t;u)&=b(x,t)+b(y,t)+b(y,u)
                     +\frac{3it^2}{4\pi}-it.
 \end{split}
 \tag{5}
\]
On the positive factorial strip these are continued from
\(0<z<1\). At a negative real factorial argument the upper and
lower continuations are the prescribed ones in the
[uniform reciprocal-factorial bound](research_uniform_factorial_and_boundary_decay.md).
These branches are kept in every estimate below.

## 2. The original geometric critical point

Let \(c\) be the root selected below of
\[
                      4c^3-4ic^2-4c+i=0,
 \tag{6}
\]
and put
\[
 t_*=2\arccos c,\qquad
 x_*=\frac1\pi\arcsin(c/\sqrt2),\qquad
 y_*=\frac1\pi\arctan c.
 \tag{7}
\]
The specified branches give the approximate locations
\[
 \begin{split}
 t_*&\simeq1.502577-0.959764i,\\
 x_*&\simeq0.187162+0.090811i,\qquad
 y_*\simeq0.228938+0.064002i.
 \end{split}
 \tag{8}
\]
The decimals only identify the branch; the certificate described
in Section 6 encloses it by a rational Rouché disk.

It is the actual positive geometric point. Theorem 5 of the
[internal-pair geometry and gap proof](research_radical_path_sector_gap.md)
gives its existence and uniqueness. Reflection of the path exchanges
the selected vertices, so their angles agree. Its angle satisfies
\(0<\Re t<\pi\), \(\Im t<0\), hence \(\cos(t/2)\) lies in
the open first quadrant. The polynomial (6) has exactly one root
there: if \(\rho\) is the unique real root of
\(\rho^3-2\rho^2+4\rho-2=0\), then \(0<\rho<1\), and its
three roots are
\[
 \frac{i\rho}{2},\qquad
 \frac{\pm\sqrt{3\rho^2-4\rho+12}+i(2-\rho)}4.
 \]
The derivative \(3\rho^2-4\rho+4\) is everywhere positive,
which proves the stated real-root facts. The positive geometry
satisfies (6) by the exact algebra below, so it must be the
enclosed first-quadrant root.

Here is the algebra and logarithmic calibration. Put
\(v=e^{it/2}\), \(s=\sin(t/2)\), \(c=\cos(t/2)\). The filling
equation at either selected vertex of the symmetric internal pair is
\[
 3t+2i\{\operatorname{arsinh}s+
                   \operatorname{arsinh}(s/c)\}=2\pi.
 \tag{9}
\]
Its two incidences are the shared edge and the complete outside
edge. If \(E=-v^3c/(1+s)\), exponentiating (9) and using the
quadratic equation for \(e^{\operatorname{arsinh}s}\) gives
\[
 \begin{split}
 v^6c^2+2sv^3c(1+s)-(1+s)^2
  =\frac{(v-1)(v+1)(v+i)^2}{4v^2}
     (v^6-2iv^5-v^4-2iv^3-v^2-2iv+1).
 \end{split}
 \tag{10}
\]
Dividing the last polynomial by \(v^3\), with
\(v+v^{-1}=2c\), gives twice the polynomial (6).

Conversely, at the enclosed root the certificate proves
\(0<\Re t_*<\pi/2\), \(\Im t_*<0\), \(\Re c,\Im c>0\),
\(|c|<1\), and \(\Re E>0\). Equation (10) therefore selects
\(E=s+\sqrt{1+s^2}\), since the other root
\(-1/E\) has negative real part. Also
\(\exp(\operatorname{arsinh}(s/c))=(1+s)/c\) on this branch:
\(\Re(1/c)>0\) fixes its square root. It follows that the
difference between the two logarithms in (9) is in \(2\pi i\mathbb Z\).
The certificate bounds
\[
 \left|\operatorname{arsinh}s+\operatorname{arsinh}(s/c)
                        -i(3t_*/2-\pi)\right|<1/100,
 \tag{11}
\]
so that difference is exactly zero. Thus (9) holds
unexponentiated.

The wire equations in (7) are the original ones:
\(\tan(\pi y_*)=c\) and
\(\tan(\pi x_*)=c/\sqrt{2-c^2}\).
On the specified bulk branches these imply
\[
             F_{x_*,y}(y_*,t_*;0)=
             F_{x_*,t}(y_*,t_*;0)=0,\qquad
                         b_x(x_*,t_*)=0.
 \tag{12}
\]
Exponentiating the logarithmic wire equations restricts their
possible defects to integer multiples of \(2\pi i\); the
certified derivative bounds \(<1/100\) fix the zero lift.
The trace equation is (9).

These phases have the original absolute complete normalization.
Indeed along \(t=\lambda t_*\), \(0\le\lambda\le1\), one has
\[
             |\cos(\lambda t_*/2)|<1\quad(\lambda>0).
 \tag{13}
\]
To see this, write \(t_*/2=a-ih\). The inequality \(|c|<1\)
means \(\sin a>\sinh h\), while
\(\sin(\lambda a)\ge\lambda\sin a\) and
\(\sinh(\lambda h)\le\lambda\sinh h\).
Both selected wire branches then have real part less than \(1/4\):
this follows directly for \(\arctan c\) from \(|c|<1\), and
for \(\arcsin(c/\sqrt2)\) from
\(\Re\arcsin z\le\arcsin|z|<\pi/4\).
All shifted factorial arguments remain in the positive real strip,
since \(\Re t_*<\pi/2\). The stationary edge identities therefore
continue from \(t=0\), without a logarithmic reset:
\[
 b(x_*,t_*)=\tfrac12\psi(t_*,t_*),\qquad
 b(y_*,t_*)+b(y_*,0)=\psi(t_*,0).
 \tag{14}
\]
In particular \(2F_{x_*}(y_*,t_*;0)\) is the original full
three-edge, two-vertex geometric stationary action.

## 3. The local theorem and its nonzero coefficient

**Theorem 1.** There are fixed complex disks about \(x_*\) and
\(u=0\), on which the critical point
\((y(x,u),t(x,u))\) of \(F_x\) is holomorphic. Put
\[
 S(x,u)=F_x(y(x,u),t(x,u);u),\qquad
 H(x,u)=-\partial_{(y,t)}^2F_x(y(x,u),t(x,u);u).
 \tag{15}
\]
Then, uniformly on smaller disks and through all integer levels,
\[
 \boxed{\quad
 W_{3,N}(x,u)=C_{N,3}N^{-1}A(x,u)e^{NS(x,u)}
                                  (1+O(N^{-1})),\quad}
 \tag{16}
\]
where
\[
 A(x,u)=
 \frac{i\sin t(x,u)}
 {4\sin(\pi x)\sin^2(\pi y(x,u))\sqrt{\det H(x,u)}}\ne0.
 \tag{17}
\]
The square root is the convergent Gaussian branch at the base
point, continued holomorphically. The normalized error is
holomorphic and has the same bounds for every fixed derivative
on smaller disks. This includes ordinary free spectral derivatives:
the exact source and its expansion are even in \(u\), so they
descend holomorphically to \(-2\cos u\) near \(-2\).

At the base point,
\[
 \Re S(x_*,0)\simeq1.263782438,\qquad
                    S_x(x_*,0)=0,\quad \Re S_{xx}(x_*,0)<0.
 \tag{18}
\]
The value in (18) is supplied by a rigorous enclosure in the
record; the displayed decimal is not an input to the proof.

## 4. Removing original finite tails before the contour

Take
\[
 I=[\alpha,\beta]=[1/32,15/32],\qquad T=39/20.
 \tag{19}
\]
First split the outer kernel into its original wire indices
inside and outside \(I\), before taking the trace in (3).
The physical values and first normals of \(B_N(x_*,t)\) obey
a polynomial times \(e^{N\Re b(x_*,0)}\). This follows from
the global real-angle reciprocal-factorial estimate and its
derivative version on disks of radius \(O(1/N)\). It includes
moving reciprocal zeros. The complete Hermite bound for an
outer wire outside \(I\), including its high Newton part, has
rate at most \(2g(\alpha)\), where
\(g(y)=J(2y)-4J(y)\). Fixed crossing values and normals cost
only powers of \(N\). The certificate proves
\[
       \Re b(x_*,0)+2g(\alpha)
                    <\Re S(x_*,0)-1/5.
 \tag{20}
\]
Thus this entire original discarded sum has a strict gap.

Next remove real trace nodes with \(|t|\ge T_N\), where
\(T_N\ge T\) is an original angular midpoint and
\(T_N-T=O(N^{-1})\). The
[real outer-angle theorem](research_terminal_real_angle_tail.md),
Proposition (3), applies since \(\pi/2<T<2\pi/3\).
It bounds every retained outer-wire subset by
\(\operatorname{poly}(N)e^{N\psi(T,0)}\) on the whole
outer angular interval, including its first normal.
The exact factorial factor has real-angle rate at most
\(\Re b(x_*,T)\) there, by the monotonicity formula in
the uniform factorial note. Beyond the point where a shifted
argument has negative real part, this means its continued lower
branch, not a reset of the principal dilogarithm used inside the
positive strip. Explicitly,
\[
 \partial_t\Re b(x,t)=\frac1{2\pi}
    \log\frac{|\cos(\pi x+t/2)|}{|\cos(\pi x-t/2)|}<0
 \quad(0<t<\pi,\ 0<\Re x<1/2).
 \]
The difference of the squared numerator and denominator is
\(-\sin(2\pi\Re x)\sin t\); the primitive remains continuous
at any moving zero. The certificate proves
\[
             \Re b(x_*,T)+\psi(T,0)
                    <\Re S(x_*,0)-1/100.
 \tag{21}
\]
This removes the original outer trace rows, not a contour current.
The factorial derivative bound and the polynomial Markov bound
for the retained kernel keep all first normals.

Both estimates persist in small complex neighborhoods of \(x_*\)
and \(u=0\). For the free boundary this follows either from the
uniform factorial estimates or from the degree-\(D\) polynomial
strip bound, shrinking the disk to preserve the strict losses.
These are whole-source errors with the original crossing and trace.

## 5. Trace first, then the remaining wire

Write \(h=-\Im t_*>0\) and \(k=\Im y_*>0\). The certificate
verifies \(h>2\pi k\). On the retained source use the exact
full-Hermite trace contour with
\[
 f_N(t)=B_N(x,t)
       \sum_{j/N\in I}B_N(j/N,t)B_N(j/N,u).
 \tag{22}
\]
This is an even holomorphic representative of all retained
physical jets. It need not be periodic in \(t\) for the
[residue identity](research_exact_complete_trace_contour.md)
to apply: oddness of
\(\sin t\,f_N(t)e^{3iNt^2/(4\pi)}\) is sufficient.
The horizontal trace contour is \(t=\tau-ih\),
\(-T_N\le\tau\le T_N\), with prefactor \(iN^2C_{N,3}/\pi\)
and the full factor
\[
                  \frac{e^{-iNt}}
                         {(1-\eta e^{-iNt})^2}.
 \tag{23}
\]
Its vertical endpoint contribution is retained exactly.

Apply the one-sided wire identity to the outer \(j\)-sum on
this contour, at heights \(\pm k\). The upper main term
has coefficient \(N\), with no phase ambiguity or factor two.
The upper and lower corrections both have penalty \(2\pi k\);
the endpoint current at \(y=e+iv\) has penalty
\(2\pi\max(-v,0)\). On each folded trace endpoint
\(t=\sigma T_N-ihs\), \(0\le s\le1\), use wire height \(ks\).
Each nested wire endpoint has its independent fraction
\(v=\epsilon krs\), \(0\le r\le1\). Thus the complete list
of domains is the same nineteen-domain list in
[the trace-first lifting proof](research_scaled_wire_contour_lifting.md),
with phase \(F_{x_*}\), degree-one wire penalties, and cutoff
\(T\) from (19). There is no scaled-degree averaging in this
application: the fixed \(x_*\) factor remains in every domain.

The outward certificate proves the following complete bounds.

| Domain | Gap below \(\Re S(x_*,0)\) |
|---|---|
| Upper wire, positive trace, outside the local rectangle | \(10^{-7}\) |
| Upper wire, negative trace | \(1/1000\) |
| Lower wire, with its full penalty | \(1/1000\) |
| Four upper/lower wire terms on the two trace endpoints | \(1/1000\) |
| Four wire endpoints on the bottom trace | \(1/1000\) |
| Eight nested wire endpoints on the trace endpoints | \(1/1000\) |

The local rectangle is
\[
  225/1000\le\Re y\le233/1000,\qquad
  235/1000\le\Re t/(2\pi)\le243/1000.
 \tag{24}
\]
The real Hessian in \(y,t\) is strictly negative definite there.
Exact stationarity gives its unique maximum. Its complement is
covered by the recorded rational boxes. The bottom trace
certificate uses the larger interval
\(|\Re t|/(2\pi)\le311/1000>T/(2\pi)\), so it covers
all sufficiently large actual midpoint contours.

There is no hidden fixed-wire branch crossing in these surfaces:
the record verifies
\[
       \tfrac12-\Re x_*-311/1000>0.
 \tag{25}
\]
The two arguments belonging to \(B_N(x_*,t)\) remain in
the positive real strip throughout. The moving outer-wire
arguments can cross the negative real axis. Their sides are
exactly those of the original trace-first proof, since
\(h>2\pi k\); the reciprocal-factorial bounds retain both
reflection terms and every zero. All their real parts stay
strictly between \(-1\) and \(1\).

For endpoint depths \(s\ge1/N\), the rational wire denominators
are bounded away from zero. For \(0\le s\le1/N\), keep the
outer wire sum unexpanded. Its real endpoint bound (21),
polynomial strip continuation, and the small \(O(1/N)\)
factorial continuation preserve the strict gap. This avoids
estimating separate \(1/s\) terms at zero height.
The nested certificates retain the product \(rs\); they do
not replace this two-variable surface by its vertices.

Consequently every nonprincipal term in the exact contour
decomposition is exponentially smaller. On the remaining
horizontal term, (23) is
\(e^{-iNt}(1+O(e^{-Nh}))\); all higher trace charges are
included in that error. The product of the three exact
Newton factors near the saddle is
\[
 \frac{e^{N\{b(x,t)+b(y,t)+b(y,u)\}}}
        {8N^3\sin(\pi x)\sin^2(\pi y)}
                                      (1+O(N^{-1})).
 \tag{26}
\]
The two-dimensional Gaussian is nonzero by the certified real
Hessian. The total power is
\(N^2\cdot N\cdot N^{-3}\cdot N^{-1}=N^{-1}\);
the constants are
\((i/\pi)\cdot(2\pi)/8=i/4\), proving (16)--(17).
The nonzero sine factors and Hessian determinant persist under
small complex parameter perturbations. The implicit-function
theorem and a local holomorphic saddle deformation, with the
strict complement bounds unchanged, prove the full uniform
statement and derivative assertions.

For completeness the last assertion of (18) is also certified.
At the base point let \(H_0=F''_{(y,t)}\), and put
\(b_{xx}=\partial_x^2b(x_*,t_*)\),
\(b_{xt}=\partial_x\partial_tb(x_*,t_*)\).
The exact Schur complement is
\[
 S_{xx}=b_{xx}
       -b_{xt}^{\,2}\frac{(H_0)_{yy}}{\det H_0}.
 \tag{27}
\]
Its real part is enclosed strictly below zero.

## 6. Reproduction and the remaining period problem

The standalone
[certificate](../experiments/certify_internal_pair_three_mixed_packet.py)
imports the previously audited rational-box/Arb engine without
changing it. It records the cubic Rouché enclosure, the original
logarithmic lift, local bulk margins and Hessian, the two physical
tail gaps, and all nineteen full rational coverings:

~~~sh
python3 experiments/certify_internal_pair_three_mixed_packet.py
~~~

The [complete record](../repro/results/research-internal-pair-three-mixed-packet.json)
includes the script and engine hashes and arithmetic versions.
The subdivision inequalities are outward interval statements,
not tests at numerical sample points.

Finally, the full internal pair still has the exact identity
\[
 \mathcal P_{3,3,N}(-2\cos u,-2\cos v)
    =N\int_{a+ih_0}^{a+1+ih_0}
                   W_{3,N}(x,u)W_{3,N}(x,v)\,dx
 \tag{28}
\]
for every real \(a,h_0\). It retains all internal aliases and
all original normal directions by exact circle averaging.
The local theorem supplies a nonzero candidate contribution
near \(x_*\), with the correct original geometric action.
To turn (28) into a full pair theorem one must still control
the rest of a whole period, or give an exact grouped substitute
with a strict competing-rate bound. No such global assertion
is inferred from this local packet.

## 7. The entire central interval of the exact circle

Put \(Y=\Im x_*\) and
\[
 L=7/100,\qquad R=3/10,\qquad M=\Re S(x_*,0).
 \tag{29}
\]
The same trace-first decomposition controls \(W_{3,N}(a+iY,0)\)
for every \(L\le a\le R\), before integrating the shared wire.
This extension uses the
[three-variable certificate](../experiments/certify_internal_pair_three_central_period.py)
and its
[complete record](../repro/results/research-internal-pair-three-central-period.json).
The local packet record in Section 6 is unchanged.

**Theorem 2.** On the interval (29), the original mixed source
has a polynomial upper bound at rate \(M\). Outside
\([183/1000,191/1000]+iY\), its rate has a fixed strict gap
below \(M\). In particular,
\[
 \begin{split}
 &N\int_{L+iY}^{R+iY}W_{3,N}(x,0)^2\,dx\\
 &\qquad=C_{N,3}^2N^{-3/2}
       \frac{\sqrt{2\pi}\,A(x_*,0)^2}
                       {\sqrt{-2S_{xx}(x_*,0)}}
       e^{2NS(x_*,0)}(1+O(N^{-1})).
 \end{split}
 \tag{30}
\]
The coefficient is nonzero. The square root is fixed by the
one-dimensional horizontal Gaussian, whose real quadratic part
is positive. There is a uniform holomorphic version with both
original outside boundaries near their complete points.

*Proof.* Retain the outer interval and angular cutoff (19),
and the heights \(k=\Im y_*\), \(h=-\Im t_*\).
Let \(x=a+iY\). The bottom surfaces always use the lower
continuation for \(1/2-x+t/(2\pi)\) and the upper continuation
for \(1/2-x-t/(2\pi)\). Their imaginary parts are
\(-Y-h/(2\pi)\) and \(-Y+h/(2\pi)\), respectively.

One change from the fixed-\(x_*\) proof is essential on a trace
endpoint. At \(t=\sigma T-ihs\), the second argument has
imaginary part \(-Y+hs/(2\pi)\). For sufficiently large \(a\)
its real part can be negative. Split the depth interval exactly at
\[
                         s_0=\frac{2\pi Y}{h}\in(0,1).
 \tag{31}
\]
Below \(s_0\) use the lower factorial continuation for that
argument; above \(s_0\) use the upper one. At zero imaginary
part their real primitive values agree. These are bounds for
the two terms in the exact reciprocal reflection formula, not
a change to the interpolation or a discarded endpoint. The
other fixed-\(x\) argument stays on its lower side. All real
factorial arguments remain a fixed distance from \(-1,1\).

There are nineteen logical contour surfaces, as in Section 5.
Splitting each of the four trace-endpoint surfaces and eight
nested endpoint surfaces at (31) gives exactly thirty-one
cover domains. Every domain now has three real parameters,
including \(a\). The nested maps keep the product of the
trace depth and the independent outer-wire endpoint depth.
The certificate's Taylor bounds include its mixed second
derivative and the corresponding mixed derivative of the
wire penalty.

The record proves the same gaps as in Section 5, uniformly
over \(L\le a\le R\): \(10^{-7}\) on the principal complement
and \(1/1000\) on every other surface. The excluded local box is
\[
 \begin{split}
 183/1000&\le a\le191/1000,\\
 225/1000&\le\Re y\le233/1000,\\
 235/1000&\le\Re t/(2\pi)\le243/1000.
 \end{split}
 \tag{32}
\]
On this box the full real three-by-three Hessian of
\(F_x(y,t;0)\) is strictly negative definite. It is checked
by the positive leading minors of its negative; the
\(x,y\) cross entry is zero. All three complex derivatives
vanish at the enclosed point by (12). Thus this is the unique
maximum on the local box, with value \(M\).
The rational covers give strict bounds on its entire complement.
The complete source's two-vertex phase is the sum of two such
phases, sharing \(x\), so this comparison retains both original
vertex factors without any scalarization.

The discarded physical terms also remain controlled uniformly.
At the fixed height \(Y\),
\[
 \frac{d}{da}\Re b(a+iY,0)=2\log|\cot(\pi(a+iY))|.
 \tag{33}
\]
The modulus on the right is greater than one below \(a=1/4\)
and less than one above it. Hence the maximum on \([L,R]\)
occurs at \(1/4\). The certificate proves
\[
 \Re b(1/4+iY,0)+2g(1/32)<M-1/5.
 \tag{34}
\]
This bounds the original entire omitted outer-wire sum, with
its full physical normals.

For the outer trace rows, the real wire maximizer
\(y_T=\pi^{-1}\arctan\cos(T/2)\) lies in \(I\), as explicitly
checked. The trace-endpoint certificate at depth zero
therefore includes the rate
\(\Re b(a+iY,T)+\psi(T,0)\), uniformly in \(a\). Its bound
is \(<M-1/1000\). Real-angle monotonicity of the continued
factorial rate and the outer-angle theorem then control
every original removed trace row. First normals cost only
polynomial factors. The small-depth collar is treated
unexpanded, exactly as in Section 5; at a moving factorial
zero its \(O(1/N)\) shift changes the primitive exponent by
at most \(O(\log N)\).

Thus the full mixed source is bounded at rate \(M\), and
all \(a\) outside the first interval in (32) have a strict
gap. Within it, strict local concavity gives a unique maximum
at \(x_*\); away from a smaller neighborhood its gap persists.
Insert the proved local expansion (16) in the remaining
integral. The stationary derivative \(S_x(x_*,0)=0\) and
\(\Re S_{xx}(x_*,0)<0\) give its nonzero Gaussian.
The powers are \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\),
which proves (30).

For free outside parameters \(u,v\), replace \(2S(x,0)\)
by \(S(x,u)+S(x,v)\) and \(A(x,0)^2\) by
\(A(x,u)A(x,v)\). The simple critical point continues
holomorphically. All strict complement bounds persist on
a small fixed bidisk, with only a local deformation needed
near that point. Cauchy's formula and evenness retain every
fixed ordinary boundary derivative. \(\square\)

The covers are reproduced by

~~~sh
python3 experiments/certify_internal_pair_three_central_period.py
~~~

This controls only the central subinterval of (28).
The complementary portions of the original circle must still
be bounded before (30) can be promoted to a full pair
asymptotic; no estimate for them is assumed here.
