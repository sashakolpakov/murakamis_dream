# The exact translation law at the lower end of the adjacent-pair integrand

Research proposition, 2 November 2026. The lower lattice correction for
two adjacent power-two fillings cannot be bounded by taking its absolute
value on the first proposed horizontal contour. Its apparent maximum
at an infinite end needs a different treatment. This note determines
that end from the original factorial interpolation, at each integer
level. After an explicit change of normalization, the integration
form is holomorphic at the missing point. In particular, its residue
there is zero.

This is a local contour statement. It does not by itself transfer the
entire finite double sum to its geometric stationary point. The
connecting faces and the other lattice corrections still belong to
that separate argument.

## 1. The exact interpolant

Fix an integer \(N\ge2\), put \(D=N-1\), and let \(G_N\)
be the normalized sine factorial. Thus
\[
 G_N(0)=1,\qquad
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z).
 \tag{1}
\]
Its normalization, continuation and finite cyclic formula are proved
directly from its Gamma product in
[the exact factorial note](research_exact_cyclotomic_factorial.md).
At integers \(0\le j<N\), its value is
\(S_j=\prod_{k=1}^j2\sin(\pi k/N)\).

For a boundary angle \(u\), put \(s=u/(2\pi)\) and define
\[
 \mathcal B_N(y,u)=
 \frac{G_N(D/2+Ns)G_N(D/2-Ns)}
 {G_N(D/2-Ny+Ns)G_N(D/2-Ny-Ns)G_N(Ny)^2}.
 \tag{2}
\]
On the regular low-index chart this is the exact interpolation of
the original Newton polynomial \(e_j(-2\cos u)\) at \(y=j/N\).
The \(-1\) in \(D=N-1\) has been retained.

The exact summand for the adjacent pair is interpolated by
\[
 \begin{split}
 f_N(x,y;u)={}&N^2
 \exp\left\{i\pi N\left(x^2-xy+\frac{y^2}{2}+x+\frac y2\right)
                    -i\pi\left(x+\frac y2\right)\right\}\\
 &\quad\times
 \frac{G_N(N(x+y))}{G_N(Nx)^3G_N(Ny)^2}\,
                         \mathcal B_N(y,u).
 \end{split}
 \tag{3}
\]
At \((x,y)=(i/N,j/N)\), with \(i,j\ge0\) and \(i+j<N\),
this equals
\[
 N^2 q^{i^2+(i-j)^2}
       \frac{(q^2;q^2)_{i+j}}
            {(q^2;q^2)_i^3(q^2;q^2)_j^2}
       e_j(-2\cos u),\qquad q=e^{\pi i/N}.
\]
Thus no new state sum has been introduced. The exact equality follows
by substituting the phase relating the sine factorial to the
\(q\)-factorial, as in
[the adjacent-pair calculation](research_adjacent_two_crossing_pair.md).

In the following, take \(0<\Re y<1/2\), \(\Im y>0\),
and a sufficiently small neighborhood of \(u=0\) on which the
factors in (2) are regular and nonzero. Put
\[
 w=e^{-2\pi i x},\qquad Y=e^{2\pi i y},\qquad
 Q=e^{2\pi i/N}.
 \tag{4}
\]
For \(\Im x<-\Im y\), one has \(|w|<|Y|<1\).
Both \(Nx\) and \(N(x+y)\) lie in the lower half-plane.

## 2. Translation by one in the normalized summation coordinate

Iterating (1) exactly \(N\) times gives
\[
 G_N(z+N)=-2\sin(\pi z)G_N(z).
 \tag{5}
\]
Indeed the product of its \(N\) sine factors is
\(2\sin(\pi(z+1))=-2\sin(\pi z)\). The identity continues
meromorphically; it is not an asymptotic assertion.

Apply (5) to the numerator and the three \(x\)-dependent
denominator factors of (3). Its exponential factor changes by
\(-e^{i\pi N(2x-y)}\). Writing
\(U=e^{2\pi iNx}=w^{-N}\) and \(V=e^{2\pi iNy}=Y^N\)
therefore gives
\[
 \frac{f_N(x+1,y;u)}{f_N(x,y;u)}
  =\frac{U^2(UV-1)}{V(U-1)^3}
  =\frac{1-(w/Y)^N}{(1-w^N)^3}
  =:R_N(w,Y).
 \tag{6}
\]
This retains the full peripheral dependence \(Y^N\).

The lower first lattice correction involves
\[
 h_N(x,y;u)=e^{-2\pi iNx}f_N(x,y;u).
 \tag{7}
\]
Since \(N\) is an integer, it has the same multiplier (6).
On \(|w|<|Y|\), fix the logarithm
\[
 \log R_N=\log(1-(w/Y)^N)-3\log(1-w^N),
 \tag{8}
\]
using power series at zero. The expression
\[
 \mathcal H_N(w,y;u)
   =h_N(x,y;u)\exp[-x\log R_N(w,Y)]
 \tag{9}
\]
is unchanged when \(x\) is replaced by \(x+1\). It therefore
defines a single-valued holomorphic function on the punctured disk
\(0<|w|<|Y|\). The next calculation determines its behavior at
zero, rather than assuming that a periodic function has no essential
singularity there.

## 3. The function extends across zero

Put
\[
 c_N=\frac12\log N
       +i\pi\left(\frac N{12}-\frac14+\frac1{12N}\right).
 \tag{10}
\]
The exact lower-half-plane factorial formula is
\[
 \log G_N(Nx)
  =\frac{i\pi N}{2}x^2-\frac{i\pi(N-1)}2x+c_N+E_N(x),
 \tag{11}
\]
where
\[
 E_N(x)=x\log(1-w^N)
       -\frac1N\sum_{k=0}^{N-1}k\log(1-wQ^k)
       +\frac{i}{2\pi N}\operatorname{Li}_2(w^N).
 \tag{12}
\]
All logarithms and dilogarithms in (12) use their convergent series
for \(|w|<1\). Formula (11) includes its exact constant.

Substitution of (11) into (3) gives
\[
 h_N(x,y;u)=C_N(y,u)w\,
                 \exp[x\log R_N(w,Y)+\Phi_N(w,Y)],
 \tag{13}
\]
with
\[
 C_N(y,u)=iN e^{-i\pi/(6N)}
        e^{N(i\pi y^2-i\pi/6)}
        \frac{\mathcal B_N(y,u)}{G_N(Ny)^2},
 \tag{14}
\]
and
\[
 \begin{split}
 \Phi_N(w,Y)={}&y\log(1-(w/Y)^N)\\
 &-\frac1N\sum_{k=0}^{N-1}k
       [\log(1-wQ^k/Y)-3\log(1-wQ^k)]\\
 &+\frac{i}{2\pi N}
       [\operatorname{Li}_2((w/Y)^N)
                         -3\operatorname{Li}_2(w^N)].
 \end{split}
 \tag{15}
\]
The \(y\) in the first term denotes the chosen local logarithm
\(y=\log Y/(2\pi i)\); no quotient in the \(y\)-variable is
being taken.

For completeness, the quadratic terms in the factorial ratio and
the exponential in (3) add to
\(2\pi i(N-1)x+i\pi Ny^2-2c_N\). Multiplication by
\(e^{-2\pi iNx}\) leaves the factor \(w\).
The remaining factorial terms are
\(E_N(x+y)-3E_N(x)\). Their coefficient of \(x\) is
exactly (8); their other terms are (15). This proves (13), including
its phase and power of \(N\).

**Proposition.** The function (9) has the explicit extension
\[
       \mathcal H_N(w,y;u)=C_N(y,u)w e^{\Phi_N(w,Y)}
                       \qquad(|w|<|Y|).
 \tag{16}
\]
It has a simple zero at \(w=0\), with derivative \(C_N(y,u)\).
In particular,
\[
 \frac{\mathcal H_N(w,y;u)}{w(1-w^N)}\,dw
 \tag{17}
\]
is a holomorphic one-form throughout that disk.

**Proof.** Every term in (15) is holomorphic on the disk and vanishes
at zero. The constant (14) is nonzero on the chosen regular parameter
neighborhood. Formula (16) follows from (9) and (13). The apparent
singularity in (17) is consequently removable, and \(1-w^N\)
does not vanish there. QED.

The denominator in (17) is the original sum of all lower geometric
lattice modes: in the lower half-plane,
\[
 \frac{f_N(x,y;u)}{e^{2\pi iNx}-1}
                =\frac{h_N(x,y;u)}{1-w^N},
 \qquad dx=-\frac{dw}{2\pi i w}.
 \tag{18}
\]
Thus the regularity assertion concerns the actual correction kernel,
after the explicit normalization (9). It is not obtained by keeping
only its first Fourier mode.

## 4. What the normalization changes

Let \(y\) range over a fixed compact neighborhood with \(|Y|\ge r_*>0\).
For a fixed \(0<\rho<\min(1,r_*)\), (8) gives
\[
 |\log R_N(w,Y)|\le
 \frac{(\rho/r_*)^N}{1-(\rho/r_*)^N}
       +\frac{3\rho^N}{1-\rho^N}
                         \qquad(|w|\le\rho).
 \tag{19}
\]
On a fixed circular arc and a bounded angular lift of \(x\),
the factor \(\exp(x\log R_N)\) therefore differs from one
by an exponentially small quantity as \(N\) increases. This is
a relative estimate. To compare the resulting integral error with
the geometric contribution, one must also bound the size of (16)
on the chosen arc. The
[complementary-arc estimate](research_adjacent_pair_lower_arc_cancellation.md)
performs that comparison at a fixed radius.

The unnormalized expression still contains \(x\log R_N\),
which becomes a multiple of \(\log w\). It must not be declared
single-valued at zero. Equations (9) and (19) identify precisely the
change made and the error incurred when returning to the original
kernel.

## 5. The action in the first coefficient

On any fixed regular compact set of \(y\) and sufficiently small
complex \(u\), the normalized factorial asymptotics give
\[
 C_N(y,u)=\frac{i}{4N\sin^2\pi y}
       e^{NV(y,u)}(1+O(N^{-1})),
 \tag{20}
\]
where
\[
 V(y,u)=b(y,u)-2J(y)+i\pi y^2-\frac{i\pi}{6},
 \quad
 b(y,u)=\int_0^y\log(2\cos2\pi t+2\cos u)\,dt-2J(y).
 \tag{21}
\]
The branches start from the original regular factorial strip.
At \(u=0\), this is
\[
 V(y,0)=-6J(y)+J(2y)+i\pi y^2-\frac{i\pi}{6}.
\]
It is exactly the limiting phase of the troublesome lower correction.
Its appearance in (20) does not create a residue at infinity:
the one-form (17) is holomorphic there. The contour must still be
transported using (18)--(19); equality of critical actions alone
would not justify dropping a lattice correction.

The finite cyclic formula used here applies to the same canonical
factorial in every short-filling source. The specific multiplier
and simple zero in (6) and (16), however, were calculated for this
adjacent pair. Their counterparts for a general partially filled
source must be calculated, not assumed.
