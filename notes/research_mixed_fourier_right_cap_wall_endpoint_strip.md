# The actual Wall solution on a fixed endpoint strip

Research deduction, 7 November 2026. The finite normalization of the
outgoing contraction selects a nonzero solution on a fixed positive
fraction of its degree range. An exact degree recurrence proves this
directly. It also gives a uniform asymptotic with an explicit nonzero
coefficient there. No real-base orthogonality or numerical evaluation
is used.

The result concerns the complete outgoing sum at each retained physical
index sufficiently close to its upper endpoint. Thus it retains the
cancellation among all of that sum's rows. The interval is not claimed
to cover the entire previously unpaid physical wedge, and the remaining
sum over the retained index is not estimated here.

## 1. The exact degree recurrence

Use the original notation and normalization of the
[Wall contraction](research_mixed_fourier_right_cap_wall_operator.md):
\[
 r=e^{-2\pi i/N},\qquad
 W_n(u;a)=\sum_{l=0}^n
 \frac{(r^{-n};r)_l}{(r;r)_l(ar;r)_l}u^l,
 \qquad 0\le n<N.
 \tag{1}
\]
The parameter \(a\) and argument \(u\) are kept fixed when the degree
changes. Assume \((ar;r)_{N-1}\ne0\). Put
\[
 A_n=r^n(1-ar^{n+1}),\qquad C_n=ar^n(1-r^n).
 \tag{2}
\]
Then for \(0\le n\le N-2\),
\[
 A_nW_{n+1}=(A_n+C_n-u/r)W_n-C_nW_{n-1},
 \qquad W_0=1.
 \tag{3}
\]
At \(n=0\), the term involving \(W_{-1}\) is absent because
\(C_0=0\). In particular
\[
                   W_1=1-\frac{u}{r(1-ar)}.
 \tag{4}
\]

Here is a finite coefficient proof, including the endpoints of the
recurrence. Write \(c_{n,l}\) for the coefficient in (1). For
\(1\le l\le n\), set \(z=r^n,v=r^l\). The three required ratios are
\[
 \frac{c_{n+1,l}}{c_{n,l}}=\frac{rz-1}{rz-v},\qquad
 \frac{c_{n-1,l}}{c_{n,l}}=\frac{z-v}{z-1},\qquad
 \frac{c_{n,l-1}}{c_{n,l}}
       =\frac{rz(1-v)(1-av)}{rz-v}.
 \tag{5}
\]
Substitution shows
\[
 A_n\frac{c_{n+1,l}}{c_{n,l}}-(A_n+C_n)
       +C_n\frac{c_{n-1,l}}{c_{n,l}}
       +\frac1r\frac{c_{n,l-1}}{c_{n,l}}=0.
\]
Indeed the first difference contributes
\(z(1-arz)(v-1)/(rz-v)\), the \(C_n\) difference contributes
\(az(v-1)\), and the last term cancels their sum. The constant
coefficient cancels directly. At degree \(n+1\), use
\[
 c_{n,n}=\frac{(-1)^n r^{-n(n+1)/2}}{(ar;r)_n},\qquad
                 A_nc_{n+1,n+1}=-r^{-1}c_{n,n}.
 \tag{6}
\]
The case \(n=0\) follows directly from (4). No coefficient at
degree \(N\), and no limiting infinite series, enters this proof.

## 2. A contracting ratio fixed by the actual initial condition

Let \(Y_0=e^{2\pi ix_0}\) be the original Fourier parameter. Its
inherited bounds give
\[
 .605<|Y_0|<.615,\qquad
 2/5<\cos\arg Y_0<21/50,\qquad \Im Y_0>0.
 \tag{7}
\]
They are the analytic bounds in the
[allocation-curvature theorem](research_mixed_fourier_allocation_curvature.md),
not a new evaluation. Throughout this section specialize \(a=u=Y\),
where \(Y\) ranges in a sufficiently small fixed complex neighborhood
of \(Y_0\) with compact closure in \(0<|Y|<1\).

Introduce independent analytic variables \(t,\varepsilon\) and set
\[
 \begin{split}
 z&=e^{-2\pi it},\qquad r_\varepsilon=e^{-2\pi i\varepsilon},\\
 A(t,\varepsilon)&=z(1-Yr_\varepsilon z),\\
 C(t,\varepsilon)&=Yz(1-z),\\
 B(t,\varepsilon)&=A(t,\varepsilon)+C(t,\varepsilon)
                                      -Y/r_\varepsilon.
 \end{split}
 \tag{8}
\]
At \(t=\varepsilon=0\), the two roots of
\[
                       AR^2-BR+C=0
 \tag{9}
\]
are zero and
\[
                         R_0(Y)=\frac{1-2Y}{1-Y}.
 \tag{10}
\]
The second is nonzero. In fact
\[
 |1-2Y_0|^2-|1-Y_0|^2=3|Y_0|^2-2\Re Y_0>0,
 \tag{11}
\]
by (7). The implicit function theorem supplies one holomorphic
root \(R(t,\varepsilon,Y)\) near (10). Shrink the fixed neighborhoods
so that \(A\) and \(R\) have uniform positive lower bounds in modulus.
Choose a fixed small radius \(b>0\). Since \(C(0,\varepsilon)=0\),
the same shrinking gives, for a fixed \(\vartheta<1\),
\[
 \left|\partial_w\left(\frac BA-\frac{C}{Aw}\right)\right|
 =\left|\frac{C}{Aw^2}\right|\le\vartheta
 \quad\text{when } |w-R(t,\varepsilon,Y)|\le b,
 \qquad b<\tfrac14\inf|R|.
 \tag{12}
\]
These are elementary local continuity choices at a nonzero simple
root. In particular there exist fixed \(\delta>0\),
\(\varepsilon_0>0\), and a common complex \(Y\)-neighborhood on which
all these bounds and finitely many analytic derivative bounds hold for
\(0\le t\le\delta\), \(|\varepsilon|\le\varepsilon_0\).
We may take \(\delta<1/4\). No numerical value of \(\delta\) is asserted.

**Theorem 1.** There is \(N_0\) such that, for every integer
\(N\ge N_0\), every \(0\le n\le\delta N\), and every \(Y\) in a
fixed smaller neighborhood, the actual polynomial \(W_n(Y;Y)\) is
nonzero. If \(\varepsilon=1/N\), its successive ratios satisfy
\[
 \frac{W_n(Y;Y)}{W_{n-1}(Y;Y)}
       =R(n\varepsilon,\varepsilon,Y)+O(\varepsilon),\qquad n\ge1,
 \tag{13}
\]
uniformly in this range.

*Proof.* Let \(\Phi_t(w)=B/A-C/(Aw)\). At \(n=0\), (3) fixes
the actual first ratio exactly:
\[
 \frac{W_1}{W_0}=R(0,\varepsilon,Y)
                  =1-\frac{Y}{r_\varepsilon(1-Yr_\varepsilon)}.
 \tag{14}
\]
Its distance from \(R(\varepsilon,\varepsilon,Y)\) is at most
\(L\varepsilon\), for a uniform derivative bound \(L\).
Whenever the preceding ratio lies in (12), recurrence (3) gives
the next ratio as \(\Phi_{n\varepsilon}\) of that ratio. Its error
from \(R((n+1)\varepsilon,\varepsilon,Y)\) is at most
\(\vartheta\) times the preceding error plus \(L\varepsilon\).
Choose \(N_0\) so that \(L\varepsilon/(1-\vartheta)<b\).
Induction proves (13), and every generated ratio stays separated
from zero. Starting with \(W_0=1\), this also proves that no denominator
used in the induction vanishes. Thus it concerns the actual finite
solution, rather than a separately selected formal solution. \(\square\)

## 3. A nonzero leading coefficient, with its normalization

All functions in the following formulas are the analytic root of
(9). Define
\[
 d=\frac{C}{AR^2},\qquad
 v=-\frac{R_t}{1-d},\qquad L=\log R.
 \tag{15}
\]
The logarithm is continued from (10). At the original parameter,
\[
 \Re R_0=\frac{1-3\Re Y+2|Y|^2}{|1-Y|^2}>0,
 \qquad \Im R_0=-\frac{\Im Y}{|1-Y|^2}<0,
\]
so its principal logarithm fixes this choice. Changing this initial logarithm by \(2\pi i\)
would also leave every discrete exponential below unchanged.

The more precise ratio estimate is
\[
 \frac{W_n}{W_{n-1}}
       =R(n\varepsilon,\varepsilon,Y)
                +\varepsilon v(n\varepsilon,\varepsilon,Y)
                +O(\varepsilon^2).
 \tag{16}
\]
To prove it, substitute the expression on the right into the exact
ratio recurrence. Its first-order residual is zero because
\((1-d)v=-R_t\); its remaining residual is uniformly
\(O(\varepsilon^2)\). At the initial ratio (14), the error is already
\(O(\varepsilon^2)\): \(d(0,\varepsilon)=0\), hence
\(v(0,\varepsilon)=-R_t(0,\varepsilon)\), which cancels the
first-order shift from zero to \(\varepsilon\). The same contraction
(12) proves (16) for every successive ratio.

Put
\[
 \begin{split}
 I(t,Y)&=\int_0^t L(s,0,Y)\,ds,\\
 \mathcal A(t,Y)&=
 \exp\left\{\frac{L(t,0,Y)-L(0,0,Y)}2
       +\int_0^t\left(
          \frac{R_\varepsilon}{R}
          -\frac{R_t}{R(1-d)}\right)(s,0,Y)\,ds\right\}.
 \end{split}
 \tag{17}
\]
Then \(\mathcal A\) is holomorphic and nonzero, and
\(\mathcal A(0,Y)=1\).

**Theorem 2.** Uniformly in the range of Theorem 1,
\[
 \boxed{\qquad
 W_n(Y;Y)=\mathcal A(n/N,Y)
                    e^{NI(n/N,Y)}(1+O(N^{-1})).
 \qquad}
 \tag{18}
\]
The normalized error has the same bound after every fixed number
of \(Y\)-derivatives on a smaller common neighborhood.

*Proof.* Sum the logarithms of (16). The accumulated
\(O(\varepsilon^2)\) error is \(O(\varepsilon)\), since
\(n\varepsilon\le\delta\). The elementary endpoint-corrected
Riemann sum gives
\[
 \begin{split}
 \log W_n={}&\varepsilon^{-1}\int_0^t L(s,\varepsilon,Y)\,ds
       +\frac{L(t,\varepsilon,Y)-L(0,\varepsilon,Y)}2\\
       &+\int_0^t\frac{v}{R}(s,\varepsilon,Y)\,ds
       +O(\varepsilon),\qquad t=n\varepsilon.
 \end{split}
 \tag{19}
\]
The identity here uses the logarithm obtained by multiplying the
nonzero successive ratios; no global logarithm of an unrelated
solution is assumed. Expand the first integral to first order in
\(\varepsilon\) and the remaining terms to zeroth order. Since
\(L_\varepsilon=R_\varepsilon/R\), (17)--(18) follow. Uniform
analyticity on the common complex \(Y\)-neighborhood and Cauchy's
formula give the derivative statement. \(\square\)

In particular, the coefficient in (18) is obtained from the exact
initial condition and is bounded above and below in modulus on every
closed subdomain just stated. This conclusion is stronger than merely
identifying the two roots of a commutative symbol.

## 4. Identification with the original outgoing saddle and action

Set \(z=e^{-2\pi it}\), use \(R(t,0,Y)\), and define
\[
 Q(t,Y)=z-\frac{z-1}{R(t,0,Y)},\qquad
 q(t,Y)=-\frac{\log Q(t,Y)}{2\pi i},\qquad q(0,Y)=0.
 \tag{20}
\]
These functions are analytic near \(t=0\). Substitution of (20)
in (9) gives
\[
 YQ^2+(Yz^{-1}-1-Y)Q+1-Y=0.
 \tag{21}
\]
Thus it is the original outgoing quadratic with
\(S=z^{-1}=e^{-2\pi i(1-t)}\), including the orientation of the
physical retained index. Its expansion at the endpoint is
\[
             q(t,Y)=\frac{Y}{2Y-1}\,t+O(t^2).
 \tag{22}
\]
At the original \(Y\), if \(v_0=Y/(2Y-1)\), then
\[
 \Re v_0=
 \frac{2|Y|^2-\Re Y}{|2Y-1|^2}>0,\qquad
 1-\Re v_0=
 \frac{2|Y|^2-3\Re Y+1}{|2Y-1|^2}>0,\qquad
 \Im v_0=-\frac{\Im Y}{|2Y-1|^2}<0.
 \tag{23}
\]
The strict signs follow directly from (7), and persist on a smaller
fixed neighborhood. Shrink \(\delta\) if needed. For real
\(0<t\le\delta\),
\[
                    0<\Re q(t,Y)<t,
                         \qquad \Im q(t,Y)<0.
 \tag{24}
\]
Consequently both original factorial arguments \(q\) and
\(1-t+q\) have real parts in \((0,1)\). Also \(|Q|<1\);
the other root of (21) has modulus greater than one because
\(|Y^{-1}-1|>1\). No independent square-root choice is made.

The exponential equation (21) has the original zero logarithmic lift
on this strip. Indeed as \(t\downarrow0\),
\[
 \frac{1-SQ}{1-Q}\longrightarrow
                  -\frac{1-v_0}{v_0}=\frac{1-Y}{Y}.
\]
The original arguments of the numerator and denominator tend to the
arguments of \(-i(1-v_0)\) and \(iv_0\), respectively. By (23)
their difference is in \((-\pi,0)\), which is exactly
\(\arg(1-Y)-\arg Y\). Thus the original residual
\(g'(1-t+q)-g'(q)+\log Y-\log(1-YQ)\) tends to zero.
Its exponential is one, so continuity makes it identically zero.
This retains the cardinal chirp and the original branch of \(g\).

The same branch check gives
\[
 \log R(t,0,Y)=g'(1-t)-g'(1-t+q(t,Y)).
 \tag{25}
\]
For example at zero the ratio is \(1/(1-v_0)=R_0\), whose
argument is in \((-\pi/2,0)\), as is the difference of the two
original logarithmic arguments. Define the original critical action
\[
 \Phi(s;y)=g(s+q)-g(q)+\ell_q(y),\qquad
                  s=1-t,\quad q=q(t,Y),\quad Y=e^{2\pi iy}.
 \tag{26}
\]
Stationarity and (25), followed by the continuous endpoint limit,
prove the calibrated identity
\[
 \boxed{\qquad
 \Phi(1-t;y)=g(1-t)-\pi iy+I(t,Y).
 \qquad}
 \tag{27}
\]
Both sides tend to \(-\pi iy\) at zero. In particular no arbitrary
additive action constant is lost in the recurrence argument.

## 5. Consequence for the complete physical outgoing contraction

The exact contraction is
\[
 H_{j,N}(y)=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
                  P_jW_{N-j-1}(Y;Y).
 \tag{28}
\]
Equations (18) and (28) give a relative asymptotic for this entire
sum uniformly even when \(N-j-1\) is bounded, with \(P_j\) kept
exact. All original outgoing rows and their cancellations remain
inside \(H_{j,N}\).

For the usual fixed interior scaling choose any
\(0<t_-<\delta'<\delta\) and let
\(s=j/N\), \(t_-\le1-s\le\delta'\). The original marked factorial
symbol is
\[
 A_g(s)=\sqrt{2\sin\pi s}\,e^{-\pi is/2},\qquad
                   P_j=N^{1/2}A_g(s)e^{Ng(s)}(1+O(N^{-1})).
\]
Since the degree in (28) is exactly \(N-j-1\), the shift by one
produces the factor \(R(1-s,0,Y)^{-1}\). Thus
\[
 \boxed{\quad
 H_{j,N}(y)=N^{-1/2}\,\mathcal B(s,y)
                         e^{N\Phi(s;y)}(1+O(N^{-1})),\qquad
 \mathcal B(s,y)=
 \frac{e^{\pi iy}A_g(s)\mathcal A(1-s,Y)}
                  {(1-Y)R(1-s,0,Y)}\ne0.
 \quad}
 \tag{29}
\]
This retains the original lifted Fourier scalar, the exact index
shift and both level parities. The same fixed normalized output jets
hold on a smaller neighborhood. It is an asymptotic for the actual
finite outgoing contraction, obtained without deleting physical rows
or assuming an unknown connection coefficient.

Only a fixed endpoint strip has been proved. Nothing here establishes
the corresponding asymptotic on \(\delta< (N-j-1)/N\le1/2\), or a
uniform comparison of \(\Phi\) with the original full right-cap
supporting plane. In particular the remainder of the high-inner-index,
low-outgoing-index wedge and the final retained-index contour remain
open. No whole right-cap, arbitrary-prefix remainder or knot-invariant
lower bound follows from (29) alone.
