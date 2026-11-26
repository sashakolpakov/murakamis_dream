# The exact symmetric 343 closing trace and its missing saddle domain

Private source and phase deduction, 9 November 2026. The ordinary
closing of the symmetric word has an exact single Hermite trace
whose insertion is the product of two complete three-kernels. Its
stationary equation differs from the radical Fourier observation
used in the recent 343 transfer theorem. The required stationary
point is absent from the whole lower rectangle considered below.
This is a source-domain restriction, not a vanishing or a competing
action assertion. No mathematical numerical evaluation is used.

## 1. A complete boundary functional

Keep the original Newton basis, crossing matrix, and bilinear trace:
\[
 D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
 v(w)=(e_0(w),\ldots,e_D(w))^T,\quad A_n=JM^n .
\tag{1}
\]
Here \(M\) is multiplication by the original crossing \(R_N\),
\(\phi_N(e_i e_j)=J_{ij}\), and
\[
 (A_n)_{ij}=\phi_N(e_iR_N^ne_j),\qquad A_n^T=A_n .
\tag{2}
\]
These are the conventions of the
[complete high-coefficient identity](research_mixed_next_high_coefficients_terminal_insertion.md),
equations (1)--(3). Define the unreduced ordinary polynomial
\[
 Q_N(w,z)=v(w)^TA_3v(z)
 =\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N(z,x)],
 \qquad K_N(w,z)=\sum_{j=0}^{D}e_j(w)e_j(z).
\tag{3}
\]
Its degree in each free variable is at most \(D\).

**Proposition 1.** The original ordinary closing of the word 343
is exactly
\[
 \boxed{\quad
 Z_{343,N}(w_L,w_R):=v(w_L)^TA_3A_4A_3v(w_R)
   =\phi_N^{(z)}[R_N(z)^4Q_N(w_L,z)Q_N(w_R,z)] .
 \quad}
\tag{4}
\]
The equality is an ordinary polynomial identity in the two free
colors, at both parities, with every fixed ordinary derivative.

Indeed the coefficient column of \(Q_N(w,z)\) in the basis \(e_j(z)\)
is \(A_3v(w)\). Applying (2) to the product of the two columns gives
\((A_3v(w_L))^TA_4(A_3v(w_R))\), which is (4).
Only the traced variable is reduced. In particular the product in
(4), whose ordinary degree can be \(2D\), is not shortened or
identified with its values at the distinct spectral nodes. The
double-root normals and the odd simple node remain in \(\phi_N\).
No radical insertion is present to consume a normal.

For comparison, the exact reversed-cap formula sums the ordinary
right boundary first and gives
\[
 Z_{343,N}
 =\kappa_N^4N^2\operatorname{CT}_Y
    [F_{34,N}(w_L,Y)d_N(Y)(1+Y^{-N})V_{0,N}(w_R,Y)] .
\tag{5}
\]
Here \(\kappa_N=q^{D^2/2}\), and all factors are the literal
ones in equation (13) of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md),
with its first retained coordinate integrated into \(F_{34,N}\).
Equations (4) and (5) are two exact representations of the same
boundary functional. No estimate for a signed factor has been
divided in obtaining either representation.

## 2. Its exact finite contour and original principal phase

Set
\[
 \mathscr Q_N(w,u)=Q_N(w,-2\cos u),\quad
 F_N(u)=\mathscr Q_N(w_L,u)\mathscr Q_N(w_R,u),\quad
 C_{N,n}=q^{nD^2/4},
\]
\[
 G_N(u)=\sin u\,F_N(u)e^{iNu^2/\pi},\qquad
 W_N(u)=\frac{e^{-iNu}}{(1-\eta e^{-iNu})^2},\qquad
 \tau_j=\frac{2\pi}{N}(D/2-j).
\tag{6}
\]
The insertion \(F_N\) is even and entire. The
[complete trace theorem](research_exact_complete_trace_contour.md)
allows arbitrary polynomial degree, so it gives, without a cutoff,
\[
 Z_{343,N}=\eta C_{N,4}\sum_{j=0}^{D}G_N'(\tau_j)
\tag{7}
\]
and, for every fixed \(h>0\),
\[
\begin{split}
 Z_{343,N}
 ={}&-\frac{N^2C_{N,4}}{\pi i}
      \int_{-\pi-ih}^{\pi-ih}G_N(u)W_N(u)\,du\\
 &+\frac{\eta N^2C_{N,4}}{\pi}
      \int_{-h}^{h}
       \frac{G_N(\pi+iv)}{4\cosh^2(Nv/2)}\,dv .
\end{split}
\tag{8}
\]
Both integrals have their displayed original orientations. All
positive charges occur in
\[
 W_N(u)=\sum_{\ell\ge1}\ell\eta^{\ell-1}e^{-i\ell Nu}
 \quad(\Im u<0).
\tag{9}
\]
The vertical term is not yet an error estimate. At odd levels the
central sample in (7) is exactly \(G_N'(0)=F_N(0)\); it is not
deleted by folding.

At complete ordinary colors write \(S(u)=S_3(0,u)\), with the
original calibrated constant and selected cubic sheet of
[the inner-three continuation](research_mixed_next_inner_three_cubic_continuation.md).
Where the full three-kernel has its proved packet, its normalization
is
\[
 \mathscr Q_N(-2,u)
 =C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
        (1+O_{\rm hol}(N^{-1})),\qquad \mathcal A(u)\ne0 .
\tag{10}
\]
The original complete small disk and
[the independent positive rectangle](research_mixed_next_positive_rectangle_inner_packet.md)
supply actual instances of (10). The latter rectangle has
\(0\le\Re u\le8/7\), \(0\le-\Im u\le2/5\).

The unit-charge principal phase for (8) is therefore
\[
 \Xi(u)=2S(u)+\frac{iu^2}{\pi}-iu,\qquad
 \Xi'(u)=-\frac2\pi\,\mathfrak F(u),
\]
\[
 \mathfrak F(u)=f(u)-iu+\frac{i\pi}{2},\qquad
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\},\qquad
 c(u)=\cos(t_*(u)/2).
\tag{11}
\]
Thus its stationary equation is
\[
                    f(u)-iu=-i\pi/2 .
\tag{12}
\]
The coefficient of \(u\) in (12) is one. Replacing it by \(3/2\)
would give the different radical-observation problem and would not
preserve (4).

## 3. A quantitative exclusion on the available lower rectangle

Consider the closed rectangle
\[
 \mathcal R=\{u=\beta-iK:0\le\beta\le4/3,\ 0\le K\le2/5\}.
\tag{13}
\]
It lies inside the phase domain of the cubic continuation and
contains the full positive rectangle just cited. Its cubic sheet
satisfies, writing \(2c=x+ib\),
\[
 \frac32<x<\frac{15}{8},\qquad \frac13<b<\frac23,\qquad
 4c^3-3c-i(4c^2-1)=\cos(u/2).
\tag{14}
\]
In fact \(b>1/2\) on (13). The imaginary part of the cubic is
\[
 2\Im\cos(u/2)
 =(3b-2)x^2-b^3+2b^2-3b+2=:F_x(b).
\tag{15}
\]
Here the left side is nonnegative. On \(1/3\le b\le2/3\),
\[
 F_x'(b)=3x^2-3b^2+4b-3>0,\qquad
 F_x(1/2)=-x^2/2+7/8<-1/4 .
\tag{16}
\]
For example the derivative exceeds \(27/4-3>0\), since
\(-3b^2+4b\ge0\) on this interval. Equations (15)--(16)
prove the assertion. Consequently, with \(c=p+iq\),
\[
                0<p<15/16,\qquad q>1/4 .
\tag{17}
\]

**Proposition 2.** On every point of (13),
\[
                 \Im\mathfrak F(u)>1/16 .
\tag{18}
\]
In particular (12) has no solution there. The principal closing
rate decreases down each vertical segment of this rectangle:
\[
             \frac{\partial}{\partial K}\Re\Xi(\beta-iK)
                   <-\frac1{8\pi}.
\tag{19}
\]

Put \(w=c\tan(u/2)\). Except at zero it is in the right
half-plane, since \(p,q>0\) and
\[
 \tan(u/2)=\frac{\sin\beta-i\sinh K}{\cos\beta+\cosh K}.
\tag{20}
\]
The principal inverse hyperbolic sine is therefore the original
one. If \(f=A+i\nu\), then \(A\ge0\), \(|\nu|<\pi/2\), and
\(\Im w=\cosh A\sin\nu\). In particular, when \(\Im w\ge-d\)
with \(0<d<1\), one has \(\nu\ge-\arcsin d\). The same
conclusion at \(w=0\) is direct.

The elementary bounds needed below are
\[
 \sinh(2/5)<5/12,\quad \cos(4/3)>7/30,\quad \pi>25/8.
\tag{21}
\]
For the first, the positive series from its cubic term onward
has successive ratio at most \(1/125\), giving
\[
 \sinh(2/5)
 \le\frac25+\frac{4/375}{1-1/125}
 =\frac{191}{465}<\frac5{12}.
\]
For the second, the alternating series gives
\(\cos(4/3)\ge7709/32805>7/30\).
All numbers here are exact rational witnesses.

If \(0\le\beta\le\pi/3\), (17),(20),(21) give
\[
 \Im w=\frac{q\sin\beta-p\sinh K}{\cos\beta+\cosh K}
 >-\frac{(15/16)(5/12)}{3/2}=-\frac{25}{96}
 >-\frac3{10}.
\tag{22}
\]
Since \(\sin(1/3)>1/3-(1/3)^3/6=53/162>3/10\),
we obtain \(\nu>-1/3\). Hence
\[
 \Im\mathfrak F=\nu-\beta+\pi/2
 >-1/3+\pi/6>1/6.
\tag{23}
\]
If instead \(\pi/3\le\beta\le4/3\), then
\(\sin\beta\ge\sqrt3/2>6/7\). Thus
\[
 \Im w>
 \frac{3/14-25/64}{37/30}
 =-\frac{1185}{8288}>-\frac3{20}.
\tag{24}
\]
To justify division by the lower bound \(37/30\), first note
that the numerator is bounded below by the displayed negative
number; if the actual numerator is positive, the conclusion is
immediate. Now
\(\sin(1/6)>1/6-(1/6)^3/6=215/1296>3/20\),
so \(\nu>-1/6\). Finally
\[
 \Im\mathfrak F>-1/6+\pi/2-4/3
 >-1/6+11/48=1/16 .
\tag{25}
\]
This proves (18). Differentiating (11) at \(u=\beta-iK\)
gives (19), with the indicated sign.

There is also a direct algebraic check of exclusion. If (12)
held, then
\[
 c\tan(u/2)=\sinh(i(u-\pi/2))=-i\cos u .
\tag{26}
\]
For \(\beta>0\), putting \(L=\cosh K\) and solving (26) for
the imaginary part of \(c\) gives
\[
 \Im c=\sin\beta\left(L-\frac1{L-\cos\beta}\right).
\tag{27}
\]
But \(L^2-1=\sinh^2K<25/144<7/30<L\cos\beta\)
on (13). The right side of (27) is therefore negative,
contradicting (17). At \(\beta=0\), the required \(c\) in
(26) is real when \(K>0\), and \(u=0\) plainly does not
satisfy (12). This independently explains the domain mismatch.

## 4. Relation to the original symmetric geometric reference

The [positive fractional-charge theorem](research_positive_path_fractional_charge_cube.md)
gives a unique positive solution for the path 343 with complete
outside angles. Reversal uniqueness makes its two end angles equal:
write them \(t_g,t_g\), and the middle angle \(u_g\). Their
original, unsquared equations are
\[
\begin{split}
 \operatorname{arsinh}(\tan(t_g/2))
 +\operatorname{arsinh}(\cos(u_g/2)\tan(t_g/2))
       &=i(3t_g/2-\pi),\\
 \operatorname{arsinh}(\cos(t_g/2)\tan(u_g/2))
       &=i(u_g-\pi/2).
\end{split}
\tag{28}
\]
The branches in (28) are the original positive returns, not a
choice made from squared polynomial equations. In particular
\(0<\Re t_g,\Re u_g<\pi\), both heights are negative, and
\(c_g=\cos(t_g/2)\) has positive real part.

The [Chebyshev elimination](research_two_edge_stationary_chebyshev_trace.md)
applies to the first equation with its original sign
\(\cosh(\operatorname{arsinh}(\tan(t_g/2)))=\sec(t_g/2)\):
both sides have positive real part and the same square when
\(0<\Re t_g<\pi\), \(\Im t_g<0\). Its other divisors are
nonzero on that angle domain. It gives
\[
       4c_g^3-3c_g-i(4c_g^2-1)=\cos(u_g/2).
\tag{29}
\]
If \(u_g\) belonged to (13), this is precisely the selected root
in (14). To check the sheet, the cubic identity with
\(v=2c_g=x+ib\) has
\[
 \Re\cos(u_g/2)
 =\frac{x}{2}\{x^2-3(b-2/3)^2-5/3\}.
\tag{30}
\]
For \(0<x\le3/2\) this is at most \(7/16\), whereas
\(\Re\cos(u_g/2)\ge\cos(2/3)>7/9\).
Thus \(x>3/2\). The cubic continuation theorem proves that
there is exactly one such root over \(\Re C>1/2\).
The middle return in (28) is also the principal one on (13),
by (20). Proposition 2 would contradict its second equation.
Therefore the actual geometric middle angle obeys
\[
            u_g\notin\mathcal R .
\tag{31}
\]
This is not merely failure to certify a root inside a chosen box.

The existing
[geometric action calibration](research_mixed_geometric_action_calibration.md),
equation (23), and
[geometric/source identification](research_mixed_geometric_source_identification.md)
retain the original action at this reference:
\[
\begin{split}
 \mathcal F_{343}(z_*)={}&
 2\psi(0,t_g)+2\psi(t_g,u_g)
 +\frac{3it_g^2}{2\pi}-2it_g
 +\frac{iu_g^2}{\pi}-iu_g+2i\gamma .
\end{split}
\tag{32}
\]
Here \(\gamma\) is exactly the fixed real vertex constant in
that calibration. Where the original end branch can be eliminated
as \(t_g=t_*(u_g)\), the part before \(2i\gamma\) is (11).
Equation (32) gives the geometric meaning of the required
stationary system, but does not extend the full finite packet to
the unlocated point \(u_g\).

## 5. The conditional local multiplier and the remaining task

Suppose a fixed lower-half-plane point \(u_*\) has a neighborhood
on which the full packet (10) is actually proved, with
\(\Xi'(u_*)=0\), \(\Xi''(u_*)\ne0\), and an eligible
left-to-right local Gaussian contour through it. These are
explicit additional hypotheses, not assertions about (13).
Keep the exact normalized holomorphic amplitudes from (10) on
that neighborhood before integrating. The unit-charge local
part of (8) then has
\[
 C_{N,4}C_{N,3}^{\,2}N^{-3/2}
 \,i\sqrt{\frac2\pi}\,
 \frac{\sin u_*\,\mathcal A(u_*)^2}
      {\sqrt{-\Xi''(u_*)}}\,
 e^{N\Xi(u_*)}(1+O(N^{-1})).
\tag{33}
\]
The square root has the orientation of this actual Gaussian
contour. Its coefficient is nonzero if \(\sin u_*\ne0\).
The level power is \(N^2N^{-3}N^{-1/2}=N^{-3/2}\);
the exact scalars \(C_{N,4}C_{N,3}^2\) have not been replaced
by a different crossing convention.

The original derivative sampling also checks the leading
multiplier directly. Before the unit-charge factor is inserted,
the logarithmic derivative of its exponential is
\[
        N\{2S'(u)+2iu/\pi\}.
\]
At a critical point of (11), the bracket equals \(i\), not
zero. Thus the leading part of \(G_N'\) is
\(iN\sin u_*\) times the full product symbol. The source
derivative and the crossing derivative do not cancel there.
This observation does not justify a saddle approximation to the
undeformed discrete samples; formula (33) uses the exact contour.
Higher charges in (9), the vertical current in (8), and the
remaining horizontal contour still require full-source bounds.

Consequently the recent ordinary-third transfer theorem cannot
close 343 merely by using its existing positive lower rectangle:
the original closing stationary point is outside even the larger
rectangle (13). The exact functional (4) reduces the next task to
continuing the complete inner source to the geometric solution of
(28), and paying the other pieces of (8) on that same action.
Neither a positive norm, a local germ at zero, nor the pointwise
geometric identity (32) supplies those estimates.

## Source versions

- Exact kernel/Frobenius conventions:
  eac17dec814ff750bd1845fd84b935058f4f10206eefd281e5124bd19efc5c09.
- Exact reversed-cap closing:
  79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c.
- Complete Hermite contour:
  a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8.
- Original full single-three packet and scalar:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Selected cubic, phase constant, and root count:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Complete independent positive rectangle:
  a1520474da2d389cb9cf67e92618f6ca9c552d499f35a039e842f9fc4e5075eb.
- Original positive charge solution:
  d3806cebb427d94b795e85c5c089592c4646b49ffc01238673f4f9d04f7f3bac.
- Unsquared Chebyshev elimination:
  2f4ce35d1729af574c8d482f63ee3a6304c9573f400c146fe2296ce7030be4d3.
- Original action calibration:
  7fd7032d085cb9055904673a7c3d9dd978a0fa19639670d5ece67ba8093e09d9.
- Geometric/source identification:
  ac2b6c8993eeae51eb27a449a23f0524dc10a6f1e10b3b816446178754ea5f4b.
