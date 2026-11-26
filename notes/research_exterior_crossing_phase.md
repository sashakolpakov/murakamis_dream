# An exterior product chart for the power-four phase

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The intermediate parameter required by the crossing-residue calculation
has modulus greater than one. The previous product interpolation was
defined inside the unit disk, so its local three-crossing theorem could
not be used there. Inverting the finite product gives an exact
interpolation on the other side of the circle. It retains a local
stationary phase for the proposed three-to-four composition, with a
strictly negative real Hessian.

This is a statement about the exact interpolated summands and their
local phase. It does not prove that the original finite integration
cycle contains this stationary contribution. The remaining part of
the crossing contour, the complementary index regions and all Fourier
aliases still have to be estimated.

The finite product identity used below is standard; see
[DLMF 17.2.7](https://dlmf.nist.gov/17.2.E7). We prove the interpolation,
its normalization and the local phase calculations directly.

## 1. Exact interpolation outside the unit disk

Fix \(N\ge2\), let \(Q=e^{2\pi i/N}\), and put \(r=Q^{-1}\).
The notation \((A;r)_l=\prod_{j=0}^{l-1}(1-Ar^j)\) includes the
empty product at \(l=0\). The
[interior interpolation](research_root_pochhammer_interpolation.md)
will be denoted by \(\mathcal P_N^-(s,A)\). Its lattice values are
\((A;r)_l\) at \(s=l/N\).

Define the opposite-root interpolation by
\[
 \mathcal P_N^+(s,A)
       =\overline{\mathcal P_N^-(\bar s,\bar A)}.
 \tag{1}
\]
This is a holomorphic function, not an antiholomorphic substitution
in the variables. Its domain is
\[
                    |A|<1,\qquad |Ae^{2\pi is}|<1.
 \tag{2}
\]
Conjugating the proved series and recurrence gives
\(\mathcal P_N^+(s+1/N,A)/\mathcal P_N^+(s,A)
=1-Ae^{2\pi is}\) and
\(\mathcal P_N^+(l/N,A)=(A;Q)_l\).

On a marked domain with
\[
                  |A|>1,\qquad |Ae^{-2\pi is}|>1,
 \tag{3}
\]
choose a holomorphic logarithm \(\ell_A=\Log(-A)\), and set
\[
 \mathcal P_N^{\rm out}(s,A)
    =e^{Ns\ell_A-\pi iNs^2+\pi is}
                          \mathcal P_N^+(s,A^{-1}).
 \tag{4}
\]

**Proposition 1.** Formula (4) is holomorphic and nonzero on (3).
It satisfies the exact recurrence and lattice identities
\[
 \begin{split}
 \mathcal P_N^{\rm out}(s+1/N,A)
      &=(1-Ae^{-2\pi is})\mathcal P_N^{\rm out}(s,A),\\
 \mathcal P_N^{\rm out}(l/N,A)&=(A;r)_l.
 \end{split}
 \tag{5}
\]
They hold at both level parities.

*Proof.* The quotient of the exponential in (4) at successive
arguments is \((-A)e^{-2\pi is}\). Multiplying by the quotient
in (1) gives \(1-Ae^{-2\pi is}\). At zero the value is one,
so iteration proves every lattice identity. Equivalently, factor
each term in the original finite product:
\[
 (A;r)_l=(-A)^l r^{l(l-1)/2}(A^{-1};Q)_l.
 \tag{6}
\]
Changing \(\ell_A\) by \(2\pi i k\) multiplies (4) by
\(e^{2\pi i kNs}\), which is one on the lattice. That change
does alter the continuous phase, so its choice must be recorded.
\(\square\)

Write \(B=Ae^{-2\pi is}\). All logarithms and dilogarithms with
arguments \(A^{-1},B^{-1}\) below use their disk series. Define
\[
 I_A^{\rm out}(s)
   =s\ell_A-\pi is^2+
       \frac{\operatorname{Li}_2(A^{-1})
                     -\operatorname{Li}_2(B^{-1})}{2\pi i}.
 \tag{7}
\]
Uniformly on marked compact subsets of (3),
\[
 \begin{split}
 \mathcal P_N^{\rm out}(s+1/N,A)
   &=D_A^{\rm out}(s)e^{NI_A^{\rm out}(s)}
                                       (1+O(N^{-1})),\\
 D_A^{\rm out}(s)
   &=e^{\ell_A-\pi is}
               \sqrt{(1-A^{-1})(1-B^{-1})}.
 \end{split}
 \tag{8}
\]
The square root is the exponential of half the sum of the two
disk logarithms. It is nonzero. Every fixed derivative of the
normalized error has the same order on smaller compact sets.

To prove (8), conjugate the expansion for \(\mathcal P_N^-\)
and substitute in (4). Its leading term is (7). The constant
term before shifting by \(1/N\) is
\(\pi is+\frac12[\log(1-A^{-1})-\log(1-B^{-1})]\).
The shift adds
\[
             (I_A^{\rm out})'(s)
                =\ell_A-2\pi is+\log(1-B^{-1}),
 \tag{9}
\]
which gives the displayed density. The derivative assertion
follows from the proved uniform expansion and Cauchy's formula.

These formulas specify an exterior interpolation with the correct
lattice values. We do not assert equality with an analytic
continuation of the previously chosen interior interpolation:
exact difference equations and lattice values permit periodic
multipliers. In particular one cannot join contours from the two
charts without checking their transition.

## 2. The phase with one exterior parameter

Keep the original cardinal vector, crossing matrix and scalar
\(\kappa\) of the
[three-crossing calculation](research_traced_three_vertex_endpoint.md).
Let \(x,y\) be the exterior wire variables of the proposed
composition, and \(z\) its intermediate variable. Put
\[
             X=e^{2\pi ix},\quad Y=e^{2\pi iy},
                         Z=e^{2\pi iz}.
 \tag{10}
\]
We work near the reference specified below, where \(X,Y\) lie
inside the unit disk and \(Z\) lies outside it. The two index
variables of the three-crossing summand are \(s,t\).
Choose in the exterior product the specific logarithm
\[
                         \ell_Z=2\pi iz+\pi i.
 \tag{11}
\]
Let \(\mathcal J'(w)=\Log(2\sin\pi w)\), continued from the
real interval \(0<w<1\), and set
\[
 I_X(s)=\frac{\operatorname{Li}_2(Xe^{-2\pi is})
                         -\operatorname{Li}_2(X)}{2\pi i}.
 \tag{12}
\]
The phase of the exact summand, using (4) for its second
denominator, is
\[
 F(s,t;x,z)=\mathcal J(s+t)
    +\frac{i\pi}{2}\{s+t-(s+t)^2\}
    +s(2\pi ix)+t(2\pi iz)-I_X(s)-I_Z^{\rm out}(t).
 \tag{13}
\]
The factorial and the two products have nonzero local densities
whenever their displayed charts hold.

There is a second change that cannot be omitted. The original
cardinal prefactor at \(z\) is now
\[
 c_z=\frac{e^{-\pi i(N-1)z}(1-Z^N)}N
     =-\frac{e^{\pi i(N+1)z}(1-Z^{-N})}N.
 \tag{14}
\]
Thus the phase of the corresponding three-crossing expression is
\(F-\pi ix+\pi iz\). Using \(-\pi iz\), as in the interior
chart, would lose an actual exponential factor.

The exact moving-pole term from the
[forced transport calculation](research_crossing_cauchy_transport.md)
has phase
\[
 \chi(z,y)=\mathcal J(z)+\frac{i\pi}{2}(z-z^2)
             +z(2\pi iy)-I_Y(z)-\pi i(z+y).
 \tag{15}
\]
Consequently the local phase for its composition with (13) is
\[
             \Psi(s,t,z;x,y)
                  =F(s,t;x,z)-\pi ix+\pi iz+\chi(z,y).
 \tag{16}
\]
It comes from exact finite-product interpolations and the exact
residue, with nonzero local densities. Equation (16) alone
does not select this residue from the full crossing kernel.

## 3. A nondegenerate local stationary point

Let \(x_0=x_{34}\) be the validated positive alternating
reference in the
[three/four interface proof](research_three_four_source_interface.md),
and put \(K=e^{2\pi ix_0}\). Define
\[
 Z_0=\frac{2K}{1-K},\qquad
 z_0=\frac{\Log Z_0}{2\pi i},\qquad
             (s_0,t_0)=(z_0,1/2),
 \tag{17}
\]
using the logarithm with \(0<\Im\Log Z_0<\pi\).
In particular
\[
 \begin{split}
 .284&<\Re z_0<.285,& -.043&<\Im z_0<-.042,\\
 1.30&<|Z_0|<1.31,& |K/Z_0|&<.468.
 \end{split}
 \tag{18}
\]
The first index product is inside its disk; the second has
\(Z_0e^{-2\pi it_0}=-Z_0\) and is outside it. Also
\(0<\Re(s_0+t_0)<1\), so the sine factorial is regular.

**Proposition 2.** The three derivatives
\(\Psi_s,\Psi_t,\Psi_z\) vanish at (17), with \(x=y=x_0\)
and exactly the logarithms (11)--(15). The Hessian in
\((s,t,z)\) is
\[
 H=c
  \begin{pmatrix}
       -2&-1&0\\
       -1&Z_0-1&1\\
       0&1&-2
  \end{pmatrix},
             \qquad c=\frac{2\pi i}{Z_0+1}.
 \tag{19}
\]
It obeys
\[
 -\Re H=(\Re c)
  \begin{pmatrix}2&1&0\\1&2&-1\\0&-1&2\end{pmatrix}
       \succ 2 I_3.
 \tag{20}
\]
Thus these stationary variables continue holomorphically for
\((x,y)\) near \((x_0,x_0)\), and their Gaussian density is nonzero.

*Proof.* Write \(U=e^{-2\pi is}\), \(V=e^{-2\pi it}\).
The exact exponentiated stationary equations are
\[
 \begin{split}
 U(1-V)&=X^{-1}-1,\\
 V(1-U)&=Z^{-1}-1,\\
 V&=\frac{Y}{Z(Y-1)+Y}.
 \end{split}
 \tag{21}
\]
At (17) they hold with \(U=Z_0^{-1},V=-1\).
These algebraic identities prove that the three derivatives
are in \(2\pi i\mathbb Z\), rather than proving their logarithmic
lifts. The outward enclosures in the accompanying checker place
their imaginary parts strictly between \(-\pi\) and \(\pi\).
The actual lifts therefore vanish. In particular the choice
\(\ell_Z=2\pi iz-\pi i\) instead would shift the index derivative
\(\Psi_t\) by \(2\pi i\); it is not the same phase chart.

Differentiating (13)--(16) gives (19). One can simplify it using
\(\pi\cot\pi(s_0+t_0)-\pi i=-2\pi i/(Z_0+1)\) and
\(Z_0-K=K(Z_0+1)\). Since \(c(Z_0-1)=2\pi i-2c\),
its real part is exactly (20). The real symmetric matrix there
has eigenvalues \(2-\sqrt2,2,2+\sqrt2\). Moreover
\(\Re c=2\pi\Im Z_0/|1+Z_0|^2>0\), and the certified
lower bound for \((2-\sqrt2)\Re c\) is greater than \(2.19\).
This proves (20), invertibility and the holomorphic
implicit-function assertion. The convergent local Gaussian is
\[
 \int_{\mathbb R^3}e^{v^THv/2}\,dv
             =\frac{(2\pi)^{3/2}}{\sqrt{\det(-H)}}\ne0,
 \tag{22}
\]
with its square root continued in the accretive matrix domain.
All original local densities are nonzero, by their product
formulas. \(\square\)

## 4. Its characteristic equation is the power-four equation

This local construction recovers the expected angular phase.
First we check its derivatives; the next section fixes the constant.
To see the precise scope, define on the critical branch
\[
                  W=-1-Y^{-1}-(1-Y^{-1})Z.
 \tag{23}
\]
Eliminating \(U,V,Z\) in (21) gives
\[
                  XYW^2+(X+Y)W+1-XY=0.
 \tag{24}
\]
All denominators in the elimination are nonzero near the
reference. At \(X=Y=K\), (23) is \(W=1-K^{-1}\).
This is the simple selected root \(W=2\cos\tau_4\) of the
original power-four angular equation, as proved in the
interface note.

For completeness, substitution in the other direction gives
\[
 Z=\frac{1+Y(W+1)}{1-Y},\quad
 V=-\frac{Y}{1+YW},\quad
 U=\frac{1-X}{1+X(W+1)}.
 \tag{25}
\]
The first equation of (21) reduces to (24); the second follows
by the same substitution. These rational identities also give,
for the critical value \(\Psi_{\rm crit}(x,y)\),
\[
 \begin{split}
 e^{\partial_x\Psi_{\rm crit}}
       &=\frac{XU-1}{U(1-X)}
         =-\frac{X^2+WX+1}{(X-1)^2},\\
 e^{\partial_y\Psi_{\rm crit}}
       &=\frac{Y-Z}{1-Y}
         =-\frac{Y^2+WY+1}{(Y-1)^2}.
 \end{split}
 \tag{26}
\]
They are exactly the exponentials of the two wire derivatives
of the angular phase
\[
 \Xi_4(x,y)=b(x,\tau_4)+b(y,\tau_4)
                         +i\tau_4^2/\pi-i\tau_4
 \tag{27}
\]
defined in the interface proof. At the reference, the checker
uses the original cosine logarithms to place the difference
between each pair of derivatives in the strip
\(-\pi<\Im w<\pi\). Thus the derivatives themselves agree,
not just their exponentials. Continuity gives
\[
                d\Psi_{\rm crit}=d\Xi_4
 \tag{28}
\]
on a small connected neighborhood. Their difference is constant.

## 5. The phase constant is zero

The constant can be evaluated by a continuation on the diagonal.
Consider the connected region
\[
 \mathcal D=\{K:\Im K>0,\ |K|<1,\ |2K/(1-K)|>1\}.
 \tag{29}
\]
For \(K=re^{i\theta}\), this means \(0<\theta<\pi\) and
\[
 \frac{-\cos\theta+\sqrt{\cos^2\theta+3}}3<r<1.
 \tag{30}
\]
In particular it is connected and contains the validated reference.
Use throughout
\[
 x=\frac{\Log K}{2\pi i},\quad
 Z=\frac{2K}{1-K},\quad z=s=\frac{\Log Z}{2\pi i},\quad t=\frac12,
 \qquad \tau=\arccos\frac{1-K^{-1}}2.
 \tag{31}
\]
The logarithms have arguments in \((0,\pi)\);
\(0<\Re\tau<\pi\) and \(\Im\tau<0\).

All terms of \(\Psi\) are holomorphic on this region.
Indeed \(Z\) is in the upper half-plane, \(|Z|>1\), and
\(|K/Z|=|1-K|/2<1\). The factorial arguments \(z,z+1/2\)
stay in their original strips. The stationary equations and
their zero logarithmic lifts continue throughout \(\mathcal D\).

We must also justify the angular primitive along this continuation.
Use the explicit branch
\[
 \mathcal J(a)=-\frac{i\pi}{2}(a^2-a)
        +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi ia})
        -\frac{i\pi}{12},
 \tag{32}
\]
with the dilogarithm cut \([1,\infty)\). The argument
\(a_+=1/2-x+\tau/(2\pi)\) has real part in \((0,1)\).
The other argument \(a_-=1/2-x-\tau/(2\pi)\) has real
part in \((-1/2,1/2)\); its only possible cut crossing is
\(\Re a_-=0,\Im a_-\le0\).

Such a crossing cannot occur. Set \(w=Ke^{i\tau}\). The angular
equation gives
\[
                   w^2-(K-1)w+K^2=0.
 \tag{33}
\]
If \(\Re a_-=0\), then \(w=-\rho\), with \(\rho>0\).
Writing \(K=\alpha+i\beta\), \(\beta>0\), the imaginary and
real parts of (33) imply
\[
 \rho=-2\alpha,\qquad
 \beta^2=3\alpha^2+2\alpha,\qquad
 |K|^2=2\alpha(2\alpha+1).
 \tag{34}
\]
Since \(\alpha<0\) and \(|K|^2>0\), necessarily
\(\alpha<-1/2\), hence \(\rho>1\). But
\(\Im a_-=\log\rho/(2\pi)>0\), which is on the regular
side of the cut. Therefore (32), and hence the angular
critical value, are holomorphic on all of \(\mathcal D\).
This also fixes their primitive branches without an unrecorded
dilogarithm continuation.

The rational derivative identities (26) hold throughout
\(\mathcal D\). Their actual logarithmic lifts agree at the
reference, and thus throughout this connected region.
The original angular stationary equation also keeps its zero
logarithmic lift: its exponential relation holds everywhere,
and its holomorphic lift is zero at the reference. Thus
differentiating the angular critical value introduces no
additional term from \(\tau(K)\).
Consequently \(\Psi_{\rm crit}(x,x)-\Xi_4(x,x)\) is constant.
Approach \(K=-1\) along
\[
                   K_\epsilon=-1+\frac35\epsilon^2+i\epsilon,
                         \qquad \epsilon\downarrow0.
 \tag{35}
\]
For small positive \(\epsilon\), this lies in \(\mathcal D\):
\[
 |K_\epsilon|^2=1-\epsilon^2/5+9\epsilon^4/25<1,\quad
 3|K_\epsilon|^2+2\Re K_\epsilon-1
                   =3\epsilon^2/5+27\epsilon^4/25>0.
 \tag{36}
\]
In this limit \(x,z,s,t\to1/2\), \(\tau\to0\), and
the above branches give
\[
 \mathcal J(0)=\mathcal J(1/2)=\mathcal J(1)=0,\qquad
 I_{-1}(1/2)=-i\pi/8,\qquad
 I_{-1}^{\rm out}(1/2)=7i\pi/8.
 \tag{37}
\]
These follow directly from
\(\operatorname{Li}_2(1)=\pi^2/6\),
\(\operatorname{Li}_2(-1)=-\pi^2/12\), and
\(\ell_Z\to2\pi i\). In particular \(F\to i\pi/4\),
\(\chi\to-i\pi/4\), so \(\Psi_{\rm crit}\to0\).
The two angular factorial arguments tend to zero on the
specified branches, so (27) also tends to zero.
The constant is therefore zero. Combining this with (28) proves
\[
                  \boxed{\Psi_{\rm crit}(x,y)=\Xi_4(x,y)}
 \tag{38}
\]
near the original alternating reference.

Thus the local phase has the power-four angular normalization,
and its Gaussian density is nonzero. The remaining
analytic problem is to compare this local contribution with the
rest of the exact contour and its index endpoints, retaining all
root-of-unity alias factors. Equation (38) does not give the
coefficient of this contribution in the original finite cycle.

## 6. An exact starting contour for the full finite sum

There is a way to use the exterior chart without a transition
between two different off-lattice interpolations. Fix \(h<0\).
The original cardinal identity gives
\[
 V_{4,N}(x,y)
     =N\int_{[0,1]+ih}V_{3,N}(x,z)C_N(z,y)\,dz.
 \tag{39}
\]
Indeed the integrand is entire in \(z\). Its two half-band
signs cancel, so it is periodic with period one at both level
parities. The two vertical sides of the rectangle between
heights zero and \(h\) cancel exactly. Cauchy's theorem and
the original real-period identity prove (39).

On this entire contour \(|Z|=e^{-2\pi h}>1\). For every
original real-index pair \(i,j\ge0,\ i+j<N\), use
\[
 \begin{split}
 \mathcal T_N^{\rm out}(s,t;x,z)
   ={}&
 \frac{e^{Ns(2\pi ix)+Nt(2\pi iz)
       +i\pi N\{s+t-(s+t)^2\}/2-i\pi(s+t)/2}
               \mathcal G_N(N(s+t))}
      {\mathcal P_N^-(s+1/N,X)
                \mathcal P_N^{\rm out}(t+1/N,Z)},\\
 &(s,t)=(i/N,j/N).
 \end{split}
 \tag{40}
\]
Here \(\mathcal G_N\) is the exact sine-factorial interpolant.
The lattice value in (40) is exactly the original summand
in the three-crossing double sum, including its endpoint
values. In particular
\[
 V_{3,N}(x,z)=\kappa c_xc_z
       \sum_{\substack{i,j\ge0\\i+j<N}}
             \mathcal T_N^{\rm out}(i/N,j/N;x,z).
 \tag{41}
\]
For \(|X|<1\), the two denominator charts hold uniformly on
the full real index triangle: the first endpoint radius is
\(|X|\), the second is \(|Z|>1\). Thus (39)--(41) express
the whole finite source using one exterior chart, before any
asymptotic approximation or corner deletion.

The marked logarithm in (11) is used along the entire wire
period. In fact its multiplier cancels from the full summand,
even off the index lattice. Substituting (4) into (40) gives
\[
 \mathcal T_N^{\rm out}
   =-\frac1Z
    \frac{
     e^{Ns(2\pi ix)+
        i\pi N(s-t-s^2-2st+t^2)/2+i\pi(t-s)/2}
                  \mathcal G_N(N(s+t))}
     {\mathcal P_N^-(s+1/N,X)
                    \mathcal P_N^+(t+1/N,Z^{-1})}.
 \tag{42}
\]
This is exactly periodic in \(z\). The factor \(c_z\) has
the original half-band sign under \(z\mapsto z+1\), which
cancels the sign of \(C_N(z,y)\). Thus the complete
interpolated integrand has no extra wire-period multiplier.
The root-product inversion does not create a wire-end current.
Index aliases, the factorial endpoints, and the arc-end
currents introduced by a later partial extraction of the
moving residue still require estimates. Equations (39)--(42)
justify the starting contour; they do not prove that the
local contribution (38) dominates.
