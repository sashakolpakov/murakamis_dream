# The two-angle bare kernel on its upper first-quarter contour

Private written source reduction, 8 November 2026. No mathematical
numerical evaluation or frozen-source edit is used.

On the positive half of the actual outer rectangle, the selected
wire saddle lies strictly inside the upper first quarter. The
original wire phase is horizontally strictly concave throughout
that quarter, at every nonnegative height. Both horizontal aliases,
all four weighted cut sides, and the unweighted joins can therefore
be reduced to the two real cuts. The left real cut and its entire
omitted physical interval are paid below. The right real cut and
the remaining physical right interval are not assigned a gap.

This is an exact finite-source reduction, not a full two-angle
packet theorem or an estimate for the inner three-kernel.

## 1. Actual parameters and original finite source

Use the selected critical branch \(t=t(u)\) of
[the inner cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
on the closed positive outer half rectangle
\[
 \mathcal U_+=\{u=a-ih:\ 0\le a\le\pi/2,\quad 0\le h\le1/2\}.
 \tag{1}
\]
The critical branch has its original logarithmic charge and
complete additive phase constant. Write
\[
 t=a_t-iH_t,\qquad
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=\frac{AB}{D_0},\quad C=\sqrt W .
 \tag{2}
\]
The letter \(D_0\) is unrelated to the finite level \(D=N-1\).
The square root will have positive real and imaginary parts.
The cubic theorem proves, with \(v=2\cos(t/2)\),
\[
 \frac32<\Re v<\frac{15}{8},\quad
 \frac13<\Im v<\frac23,\quad
 |v|^2<\frac{127}{36},\quad
 (\Re v)^2-(\Im v)^2>2,
 \qquad 0<H_t<1.
 \tag{3}
\]
Consequently
\[
 \frac12<\Re A<1,\quad
 \frac14<\Im A<\frac58,\quad
 \frac{85}{144}<|A|<\frac{127}{144}<1.
 \tag{4}
\]
All strict guards are uniform on this compact actual family.
No independence between \(t\) and \(u\) is assumed in identifying
the family, although the estimates below use the displayed guards.

Keep the original entire Newton sum and factorial phase:
\[
 \begin{gathered}
 q=e^{\pi i/N},\quad D=N-1,\quad M=\lceil N/2\rceil,\\
 s_k=2\sin(\pi k/N),\quad S_k=\prod_{\nu=1}^k s_\nu,\quad
 c_\nu=2\cos((2\nu+1)\pi/N),\\
 e_k(\xi)=S_k^{-2}\prod_{\nu<k}(c_\nu-\xi),\qquad
 K_N(t,u)=\sum_{k=0}^{D}e_k(-2\cos t)e_k(-2\cos u),\\
 b(y,t)=-J(1/2-y+t/(2\pi))-J(1/2-y-t/(2\pi))-2J(y),\\
 F(y;t,u)=b(y,t)+b(y,u),\qquad J'(y)=\Log(2\sin\pi y).
 \end{gathered}
 \tag{5}
\]
These are the original branches of
[the bare-kernel theorem](research_bare_kernel_thin_rectangle.md)
and [the free-boundary ray theorem](research_pair_free_boundary_kernel.md).
On \(0<\Re y<1/4\), every factorial argument in (5) has
real part strictly between zero and one, for both angles in
the actual family. Thus this entire first-quarter region uses
the ordinary bulk branch; no sidewise factorial reset is needed.

## 2. The selected wire saddle is in the upper first quarter

Put \(c=\cos a\) and \(C_h=\cosh h\) for (1). Directly,
\[
 \Re B=\frac{1+cC_h}{2}\ge\frac12,\qquad
 \Im B=\frac{\sin a\,\sinh h}{2}\ge0,\qquad
 |B|=\frac{C_h+c}{2}<\frac{15}{14},
 \tag{6}
\]
where the elementary series bound
\(\cosh(1/2)<8/7\) is already used in the fixed-ellipse
theorem. Also
\[
 \Re\frac1B=\frac{2(1+cC_h)}{(C_h+c)^2}>\frac{14}{15},
 \qquad
 \left|\frac1B-1\right|
     =\frac{C_h-c}{C_h+c}\le1.
 \tag{7}
\]
For the first inequality, its derivative in \(c\) has the
sign of \(C_h^2-2-cC_h<0\); its minimum is therefore
\(2/(1+C_h)>14/15\). Moreover \(\Im(1/B)\le0\).
Equations (4),(7) give
\[
 \Re\frac1W=\Re\left(\frac1A+\frac1B-1\right)
  >\frac{10368}{16129}-\frac1{15}>\frac8{15},
 \qquad
 \Im\frac1W<0.
 \tag{8}
\]
Here \(10368/16129>3/5\). In particular \(W\) is in
the first quadrant.

There are also strict modulus bounds
\[
                    \frac13<|W|<1.
 \tag{9}
\]
For the lower bound,
\[
 |1/W|\le |1/A|+|1/B-1|<\frac{144}{85}+1=\frac{229}{85}<3.
\]
For the upper bound, write \(1/A=x-iy\), where \(x>3/5\)
and \(y>0\), and \(1/B-1=d-ie\), where \(d>-1/15\)
and \(e\ge0\). Then
\[
 |1/W|\ge\sqrt{(x-1/15)^2+y^2}
       \ge |1/A|-\frac1{15}
       >\frac{144}{127}-\frac1{15}>1 .
 \tag{10}
\]

In the tangent coordinate \(z=\tan(\pi y)\), exact
differentiation gives
\[
 e^{F_y}
   =\frac{[A-(1-A)z^2][B-(1-B)z^2]}{z^4},
 \tag{11}
\]
and subtracting one factors its numerator as
\[
 [A-(1-A)z^2][B-(1-B)z^2]-z^4
                 =-(z^2+1)(D_0z^2-AB).
 \tag{12}
\]
The selected solution is therefore
\[
             y_*=\pi^{-1}\arctan C,\qquad
             0<\Re y_*<\frac14,\quad \Im y_*>0.
 \tag{13}
\]
Indeed \(C\) is in the first quadrant and \(|C|<1\).
The map \(\arctan\) sends this sector inside the stated
first-quarter strip. The zero logarithmic lift follows by
continuation from \(u=0\): every factorial argument remains
in its regular bulk strip at (13), the exponential in (11)
equals one, and the original free-boundary saddle has
\(F_y=0\). The family (1) is connected. Thus
\[
                 F_y(y_*;t,u)=0,\qquad
                 \psi(t,u)=F(y_*;t,u)
 \tag{14}
\]
uses the original critical branch and constant.

Compactness gives fixed cuts \(0<\alpha<\beta<1/4\)
with \(\alpha<\Re y_*<\beta\), uniformly separated from
both cuts. The left cut will be decreased further below.
Write \(h_*=\Im y_*\). Both \(h_*\) and its reciprocal
are uniformly bounded on (1).

## 3. A joint ray identity pays the left physical endpoint

The two numerator factors in (11) need not have the same
argument. The following joint calculation avoids assuming
that they do.

Set \(z=Cr\), \(r>0\), and \(v=r^{-2}\). Define
\[
 E=\frac{D_0}{C},\qquad
 R(v)=e^{F_y}
       =1+\frac{D_0}{W}(v-1)(v+W).
 \tag{15}
\]
One has \(\Re E>0\) throughout the actual family. Here is
an elementary argument bound sufficient to check that claim.
By (4), \(0<\arg A<\pi/3\). By (6),
\(\Im B<2/7\), since
\(\sinh(1/2)<\frac12\cosh(1/2)<4/7\); hence
\(0\le\arg B<\pi/6\), using \(4/7<1/\sqrt3\).
Writing \(A=a+ib\), \(B=c+id\),
\[
 \Re D_0=a+c-ac+bd\ge\frac34,\qquad
 -\frac5{112}<\Im D_0=b(1-c)+d(1-a)<\frac{51}{112}.
 \tag{16}
\]
For the real part, \(a,c\ge1/2\), \(a<1\); if \(c>1\)
its first three terms are at least one. Thus
\[
              -\frac{\pi}{12}<\arg D_0<\frac\pi4.
\]
The lower bound follows already from
\(5/84<1/4<\pi/12\).
The first-quadrant guard for \(W\) ensures the compatible
argument identity
\[
 \arg E=\frac32\arg D_0-\frac12(\arg A+\arg B).
 \tag{17}
\]
There is no \(2\pi\) ambiguity in these displayed ranges.
They give \(-3\pi/8<\arg E<3\pi/8\), as required.

A direct algebraic identity is
\[
 \Re\{E\overline{R(v)}\}
 =\Re E+
   \frac{|D_0|^2\Re C}{|W|^2}(v-1)(v+|W|).
 \tag{18}
\]
For \(v>1\), this is positive. The entire segment from
one to \(R(v)\) stays in the half-plane
\(\Re(E\overline{\zeta})>0\), which excludes the
nonpositive real axis. Consequently the original logarithm
satisfies
\[
 \frac{\Log R(v)}{R(v)-1}
       =\int_0^1\frac{ds}{1+s(R(v)-1)},\qquad
 \Re\left\{E\frac{\Log R(v)}{R(v)-1}\right\}>0 .
 \tag{19}
\]
On the ray,
\[
 F_r=\frac{C}{\pi(1+Wr^2)}\Log R(v)
     =\frac{v(v-1)}{\pi}\,
             E\,\frac{\Log R(v)}{R(v)-1}.
 \tag{20}
\]
It follows that \(\Re F_r>0\) for \(0<r<1\).
All those points are in the regular first-quarter strip.
Since \(F(0;t,u)=0\), this proves
\[
                           \Re\psi(t,u)>0 .
 \tag{21}
\]
This argument proves only the increasing part of the ray;
it makes no claim about its portion after \(r=1\).

By uniform continuity of the integrated logarithms and
compactness, the cut \(\alpha>0\) may now be chosen so
small that a fixed \(c_0>0\) satisfies
\[
 \Re F(x;t,u)\le\Re\psi(t,u)-c_0
                 \qquad(0\le x\le2\alpha).
 \tag{22}
\]
The original zero-safe finite factorial estimate then pays
every physical row in this interval, including \(k=0\):
\[
 \sum_{0\le k\le\lfloor N\alpha\rfloor}
 |e_k(-2\cos t)e_k(-2\cos u)|
       \le C N^A e^{N(\Re\psi-c_0)}.
 \tag{23}
\]
The proof uses the midpoint upper estimate with its
\(O(\log N)\) one-sided error and the exact sine factorial
at zero. It does not analytically continue a relative
error across the endpoint.

## 4. All-height first-quarter curvature and the two aliases

For \(y=x+i\sigma\), \(0<x<1/4\), \(\sigma\ge0\),
write \(X=2\pi x\), \(Y=2\pi\sigma\). If
\(\cos t=c_t+id_t\), then \(c_t>0,d_t>0\). The other
angle has \(\cos u=c_u+id_u\), with \(c_u,d_u\ge0\).
The real numerator in
\(\sin(2\pi y)/(\cos(2\pi y)+c_t+id_t)\) is exactly
\[
 \sin X\cos X
  +c_t\sin X\cosh Y+d_t\cos X\sinh Y>0.
 \tag{24}
\]
The same calculation for \(u\) is nonnegative. Also
\(\Re\cot(\pi y)>0\). Since
\[
 F_{yy}=-\pi\left\{
  \frac{2\sin(2\pi y)}{\cos(2\pi y)+\cos t}
 +\frac{2\sin(2\pi y)}{\cos(2\pi y)+\cos u}
 +4\cot(\pi y)\right\},
 \tag{25}
\]
one obtains
\[
             \Re F_{yy}(x+i\sigma;t,u)<0
                    \quad(0<x<1/4,\ \sigma\ge0).
 \tag{26}
\]
In particular the horizontal through \(y_*\) has its
unique strict maximum at the selected point. On the fixed
cuts chosen above there are uniform constants \(c_1,c_2>0\)
such that
\[
 \Re F(x+ih_*;t,u)
   \le\Re\psi-c_1(x-\Re y_*)^2,\qquad
 \max_{x=\alpha,\beta}\Re F(x+ih_*;t,u)
   \le\Re\psi-c_2 .
 \tag{27}
\]

For the lower reflected horizontal put
\[
 D_x(v)=\Re F(x-iv;t,u)-\Re F(x+iv;t,u).
 \tag{28}
\]
For one angle with cosine \(a+ib\), \(a,b\ge0\), its
contribution to \(D_x'(v)\) is
\[
 \Arg\{R_v+i(b+B_v)\}+\Arg\{R_v+i(b-B_v)\},
 \quad
 R_v=\cos(2\pi x)\cosh(2\pi v)+a>0,\quad
 B_v=\sin(2\pi x)\sinh(2\pi v).
 \tag{29}
\]
The sine-denominator arguments cancel exactly.
The two arguments in (29) lie in \((-\pi/2,\pi/2)\);
their sum lies in \([0,\pi)\), since \(b\ge0\).
Both angles together therefore give
\[
                 0\le D_x'(v)<2\pi .
 \tag{30}
\]
There is no zero or winding ambiguity: \(R_v>0\) on
the entire first-quarter region. Uniformly on the compact
cut rectangle \(x\in[\alpha,\beta]\), \(0\le v\le\max h_*\),
some \(\delta>0\) consequently satisfies
\[
 D_x(v)\le(2\pi-\delta)v .
 \tag{31}
\]
It follows that both original nonconstant horizontal
cotangent terms are strictly below the selected main:
\[
 \begin{split}
 \Re F(x+ih_*;t,u)-2\pi h_*&\le\Re\psi-2\pi h_*,\\
 \Re F(x-ih_*;t,u)-2\pi h_*&\le\Re\psi-\delta h_* .
 \end{split}
 \tag{32}
\]
All higher integer frequencies have a larger penalty.
The full rational cotangent denominators cost only a
uniform factor on these fixed positive-height contours.

## 5. Both cut sides, both joins, and the exact retained sum

Use the original canonical interpolation
\[
 B_N(y,t)=
 \frac{N}{
 G_N(N(1/2-y+t/(2\pi))-1/2)
 G_N(N(1/2-y-t/(2\pi))-1/2)G_N(Ny)^2},
 \qquad T_N(y)=B_N(y,t)B_N(y,u).
 \tag{33}
\]
Its exact sampling identity is
\(T_N(k/N)=e_k(-2\cos t)e_k(-2\cos u)\).
On a fixed neighborhood of the full retained rectangle,
all scaled factorial real parts have a uniform margin in
\((0,1)\). Hence the original full factorial theorem gives
\[
 T_N(y)=
       \frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                      (1+O(N^{-1})),
 \tag{34}
\]
uniformly there, with its further fixed orders.
No replacement interpolation is chosen by its lattice values.

Put
\[
 \alpha_N=\frac{\lfloor N\alpha\rfloor+1/2}{N},\qquad
 \beta_N=\frac{\lfloor N\beta\rfloor+1/2}{N}.
 \tag{35}
\]
All strict compact inequalities persist under these
\(O(N^{-1})\) shifts, with slightly smaller constants.
The exact cotangent rectangle encloses precisely the rows
\[
       \lfloor N\alpha\rfloor+1\le k\le\lfloor N\beta\rfloor.
 \tag{36}
\]
More explicitly, let \(\Gamma_-\) be its lower boundary
path from \(\alpha_N\) to \(\beta_N\), including both
lower half-sides, and let \(\Gamma_+\) be its upper
boundary path from \(\beta_N\) to \(\alpha_N\).
Their union is counterclockwise. The exact identity is
\[
 \begin{split}
 \sum_{\text{rows in }(36)}T_N(k/N)
   &=N\int_{\alpha_N}^{\beta_N}T_N(y)\,dy
                         +\mathscr W_N,\\
 \mathscr W_N
   &=\frac{N}{2i}\left\{
       \int_{\Gamma_-}(\cot(\pi Ny)-i)T_N(y)\,dy
       +\int_{\Gamma_+}(\cot(\pi Ny)+i)T_N(y)\,dy
                    \right\}.
 \end{split}
 \tag{36a}
\]
This follows from the residues \(1/(\pi N)\) of the
cotangent. The constant parts include the constant
vertical pieces: by holomorphy they combine to the
displayed \(+N\) real integral.
At either half-grid vertical, the nonconstant factors on
the upper and lower halves are bounded by
\(2e^{-2\pi N|v|}\). Thus (31) bounds each lower
weighted side by its corresponding upper unweighted
profile; the upper weighted side has its own additional
nonnegative penalty. These are all four weighted vertical
currents, not just their difference.

By (26), each function
\(\sigma\mapsto\Re F(x+i\sigma;t,u)\) is convex.
For \(x=\alpha_N,\beta_N\) and \(0\le\sigma\le h_*\),
its maximum is therefore at the real cut or at the
horizontal endpoint. This controls both complete
unweighted joining segments as well. With
\[
                         E_R(t,u)=\Re F(\beta;t,u),
 \tag{37}
\]
the left real cut is paid by (22), while (27) pays
both horizontal endpoints. The complete cut and joining
inventory consequently has upper rate
\[
                    \max\{\Re\psi-c_3,\ E_R(t,u)\}
 \tag{38}
\]
for a uniform \(c_3>0\). The displacement in (35)
changes the regular endpoint phases by \(O(N^{-1})\)
and is absorbed by the polynomial constants.

The real integral in (36a) deforms exactly as
\[
 \int_{\alpha_N}^{\beta_N}T_N
 =\int_{\alpha_N+ih_*}^{\beta_N+ih_*}T_N
   +\int_{\alpha_N}^{\alpha_N+ih_*}T_N
   -\int_{\beta_N}^{\beta_N+ih_*}T_N .
 \tag{38a}
\]
Thus its two unweighted joins use only positive heights,
as estimated above. No unpenalized lower join has been
silently assigned the positive-height convexity bound.
Equations
(26)--(27) give its usual nonzero Gaussian coefficient:
\[
 \begin{split}
 N\int_{\alpha_N+ih_*}^{\beta_N+ih_*}T_N(y)\,dy
   &=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                             (1+O(N^{-1})),\\
 a_e(t,u)&=
  \frac{\sqrt{2\pi}}{4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}
                      \ne0 .
 \end{split}
 \tag{39}
\]
The Gaussian root has positive real part and agrees
with the original complete-end normalization. The powers
are exactly \(N\cdot N^{-2}\cdot N^{-1/2}\).
This estimates an actual integral of the original
interpolation; it does not by itself identify the
coefficient of the entire finite sum.

Combining the exact residue identity, (23), (32), and
(38)--(39), the full kernel admits the source reduction
\[
 \boxed{\quad
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                  (1+O(N^{-1}))
          +\mathscr E_N(t,u)+\mathscr R_N^{\rm low}(t,u)
          +\mathscr R_N^{\rm rad}(t,u).
 \quad}
 \tag{40}
\]
Here the two unreplaced physical sums are literally
\[
 \begin{split}
 \mathscr R_N^{\rm low}
   &=\sum_{k=\lfloor N\beta\rfloor+1}^{M-1}
                       e_k(-2\cos t)e_k(-2\cos u),\\
 \mathscr R_N^{\rm rad}
   &=\sum_{k=M}^{N-1}
                       e_k(-2\cos t)e_k(-2\cos u),
 \end{split}
 \tag{41}
\]
and for a fixed \(\epsilon>0\),
\[
 |\mathscr E_N(t,u)|
       \le C N^A
              \exp N\max\{\Re\psi-\epsilon,\ E_R(t,u)\}.
 \tag{42}
\]
The error includes the paid left physical rows, both
horizontal aliases at every integer frequency, all four
weighted sides, and both joining segments. Its exact
definition is their signed sum from the original
cotangent identity, rather than a discarded group.
All constants are uniform on (1), at both parities.

For reference, the original radical Fourier estimate
already supplies
\[
 |\mathscr R_N^{\rm rad}(t,u)|
        \le N^2 e^{(N-1)(H_t+h)}.
 \tag{43}
\]
This is equation (22) of the free-boundary ray theorem,
with every original upper Newton index retained. No
comparison of \(H_t+h\) with \(\Re\psi\) is asserted here.

## 6. Remaining scope

The concrete missing estimates are a right real-cut gap
for (37), control of the original physical interval
\(\mathscr R_N^{\rm low}\), and an eligible comparison
for the radical rate in (43), or a coherent alternative
retaining those same terms. They are not consequences
of the selected critical point or of horizontal curvature.
Until these are supplied, (40) is not a full packet
expansion for \(K_N(t,u)\).

The restriction to the positive outer half in (1) is
essential to this proof: it makes \(\Im B\ge0\), giving
(9), the upper saddle, and the signs in (24),(29).
No corresponding statement is made for the negative
outer half, where \(\Im B\) can be negative. Nor is
any complete three-kernel trace, outer signed integral,
parameter-jet estimate, or noncancellation assertion
inferred from this reduction.
