# A complete inner-source upper envelope to the right half-period

Private finite-source theorem, 9 November 2026. The complete inner
source is bounded on the outgoing rectangle beyond the previously
proved packet. The bound is the larger of the original inner action
and one explicit endpoint-sector ceiling. It retains all original
currents and is uniform at every real angle in the stated interval,
not merely at physical nodes.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used. No outgoing stationary equation
is imposed in this theorem.

## 1. Source and conclusion

Let
\[
 \mathcal R_{\rm far}=
 \{u=\beta-iK:8/7\le\beta\le\pi/2,\quad0\le K\le2/5\}.
\tag{1}
\]
Keep the original cubic \(t_*(u)=a_*(u)-iH_*(u)\),
action \(S(u)\), \(s(u)=\Re S(u)\), coefficient \(\mathcal A(u)\),
and the two exact sources \(Q_N^{\rm sh},Q_N^{\rm full}\)
of the selected-curve and outgoing-tail theorems.
In particular the first edge and the full inner Hermite trace
are unchanged; the shortened source only shortens its second edge.

**Theorem.** For every fixed \(\tau>0\), uniformly on (1),
at both parities and all sufficiently large \(N\),
\[
 \boxed{\quad
 |Q_N^\star(u)|\le C_\tau
    \exp N\{\max(s(u),33/20)+\tau\},
                \qquad \star\in\{{\rm sh},{\rm full}\}.
 \quad}
\tag{2}
\]
More precisely there is a fixed \(\epsilon>0\) such that the
original partial-Gaussian representation can be retained in the form
\[
 Q_N^\star(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                      (1+r_N(u))+E_N^\star(u),
\tag{3}
\]
where \(|r_N|\le C/N\), and
\[
 |E_N^\star(u)|\le C_\tau
       \exp N\{\max(s(u)-\epsilon,33/20)+\tau\}.
\tag{4}
\]
These are absolute source bounds. In particular (3) does not
assert a relative packet where the endpoint ceiling is larger
than \(s(u)\).

## 2. The new outgoing guards

For \(\beta\) in (1), sine is increasing up to \(\pi/2\), and
\[
 \sin\beta\ge\sin(8/7)>
       \frac87-\frac{(8/7)^3}{6}
       =\frac{920}{1029}>\frac12.
\]
On the other hand the positive series gives
\(\sinh K\le (2/5)/(1-(2/5)^2/6)=30/73<1/2\).
Consequently, writing \(\cos u=P+iQ\),
\[
                 |\cos u|<1,\qquad P\ge0,\qquad Q\ge0.
\tag{5}
\]
No lower bound \(P>7/30\) is used.

Consider first
\[
        \pi/2\le a\le2\pi/3,\qquad1/10\le H\le1,
        \qquad t=a-iH.
\tag{6}
\]
On the incoming upper wire cut put \(C=\cosh H\) and
\(q=-\cos2\pi\Re y\). The original incoming squared
numerator is bounded, for \(q\ge0\), by
\[
 O\le q^2+A_Cq+B_C,\qquad
 A_C=(8C^2-5)/3,\quad B_C=(4C^2-1)/12.
\tag{7}
\]
By (5), the outgoing squared numerator is at most \(C^2+q^2\).
The exact squared denominator minus the product is therefore
\[
\begin{split}
 &(C+q)^4-(q^2+A_Cq+B_C)(q^2+C^2)\\
 &=(4C-A_C)q^3+(5C^2-B_C)q^2
                   +C^2(4C-A_C)q+C^2(C^2-B_C).
\end{split}
\tag{8}
\]
For \(1\le C\le8/5\), the original bound
\(4C-A_C\ge31/25\) and \(B_C<C^2/3\) make every coefficient
positive. Its constant exceeds \(2C^4/3\), and
\((C+q)^4\le16C^4\). Thus the force satisfies
\[
                        \mathfrak f^2\le23/24<1.
\tag{9}
\]
For the negative incoming cut coordinate the original
unit-modulus comparison still applies: (5) gives
the other squared numerator at most \((C-q)^2\).
The exact original bound is \(9/(8\sqrt3)<1\).

The outgoing upper cut has its own angle
\(8/7\le\beta\le\pi/2\), and its cut coordinate is nonnegative,
including zero at \(\beta=\pi/2\).
The same complete own-numerator calculation with
\(\cosh K<8/7\), \(|\cos t|<8/5\) gives
\[
                         \mathfrak f\le13\sqrt{79}/150<1.
\tag{10}
\]
It includes the starting zero and the \(K=0\) bottom limit.

For the original half-cosines, \(A=\cos^2(t/2)\),
\(B=\cos^2(u/2)\), \(D=A+B-AB\), \(W=AB/D\), (5) gives
\[
 \Re B\ge1/2,\quad |B|^2\le\Re B,\quad
 \Re(1/B)\ge1,\quad \Im B\ge0,\quad |1-B|<13/24.
\tag{11}
\]
Together with \(\Re A>1/10\), \(|A|<4/5\),
\(|1-A|<21/20\), and \(\Im A>0\), this implies
\[
 |1-D|<91/160,\qquad \Re(1/W)>5/32,\qquad\Im(1/W)<0.
\tag{12}
\]
Thus the same principal upper root remains simple and
in a compact eligible domain. Its charge starts from the
original positive edge at \(a=\pi/2,H=H_*(u)\), available
on all of \(\mathcal U_+\). Continue \(H\), then \(a\).
Equations (9)--(10) prevent crossing an original cut;
the logarithmic charge stays zero and the critical value
remains the calibrated \(\psi(t,u)\).

## 3. The complete edge envelope, also on the initial low horizontal

Put \(a_0=\arccos(-13/20)\) and \(h_0=1/10\).
For the additional family
\[
              2\pi/3\le a\le a_0,\qquad H=h_0,
\tag{13}
\]
the exact incoming-cut proof of the adopted initial
low-horizontal theorem uses only \(P,Q\ge0\) and
\(|\cos u|\le1\), rather than its old stronger lower
bound on \(P\). Its two force bounds consequently remain
\[
                  55539/56000<1,\qquad1683/2000<1.
\tag{14}
\]
The outgoing bound (10) is unchanged. The low-family
incoming guards \(\Re A>1/6,|A|<1/3,|1-A|<83/100\),
together with (11), give
\[
                |1-D|<1079/2400<1/2,\qquad
                \Re(1/W)>3/2,\qquad\Im(1/W)<0.
\tag{15}
\]
Thus the original simple zero-charge root continues
along (13) as well.

The finite upper-envelope argument applies to (6) and
(13) with the following full boundary inventory.
If \(K>0\), both real-wire logarithms have their original
arguments in \((0,\pi)\), so the upper normal derivative
is negative. If \(K=0\), the outgoing real cut starts
at \(1/2-\beta/(2\pi)\). Before that point its argument
is zero and the incoming argument gives negative normal
derivative; on and after the cut (10) gives horizontal
descent. There is no bottom or cut minimum.
The original left trace is increasing. The right trace
has its single minimum at the smaller of the two cut
heights, with connected strict sublevels. These formulas
are valid also at \(\beta=\pi/2\).
The positive jumps and zero starting-point flux make the
upper envelope subharmonic, and it tends uniformly to
infinity at large upper height.
The original component/Jordan proof therefore gives
an unweighted path at rate
\(\max\{\Re\psi(t,u),(H+K)/2\}+\varepsilon\).

Both penalized side bounds retain all original reflection
terms. With \(D_{\rm side}=(aH+\beta K)/(2\pi)\) and
\(e=(H+K)/2\), their left reserve is at least
\(H/6+K/4\ge1/60\) on (6), and at least
\(H/8+K/4\ge1/80\) on (13).
Both complete alias horizontals may use wire heights
\(\pm2\); their full remainder is less than \(1/600\).
The unchanged reciprocal-factorial interpolation remains
holomorphic in the open wire half-strip. Its zero-safe
upper bound includes every physical row through the true
odd cutoff \(U_N\).

Use exactly the original midpoint residue identity,
including its two signed caps, both physical endpoint
groups, both aliases and residue factor \(N\).
After splitting \(1/(1-\zeta)=1+\zeta/(1-\zeta)\), move
the whole unweighted upper term to the path just constructed.
The two oriented endpoint connectors are retained in the
same paid collars. This is the literal formula (20) in
the axis theorem, or (19)--(20) in the original upper-envelope
theorem, without any change of finite source.
It proves, uniformly on both families,
\[
 |K_N^<(t,u)|\le C_\tau
       \exp N\{\max(\Re\psi(t,u),(H+K)/2)+\tau\}.
\tag{16}
\]
No relative packet or domination of the endpoint term
was used in this argument.

## 4. The low geometric endpoint over the larger output interval

Let \(t_0=2\pi/3-i/10\). The existing first-edge bound is
\[
                   2\Re\psi(t_0,0)<19/12+1/300.
\tag{17}
\]
For \(u=\beta-ik\) on the output vertical, (5) remains
valid at every \(0\le k\le K\).
Hence \(\Re B\ge1/2\), \(\Re B\le1\), and
\(\Re D\ge\Re B\ge1/2\).
Writing \(c=\cos(t_0/2)\), \(C_u=\cos(u/2)\), we have
\[
 |c|<13/25,\qquad |C_u|\ge1/\sqrt2,\qquad
                         |\sqrt D|\ge1/\sqrt2.
\]
The exact original derivative thus obeys
\[
                  |\psi_{uu}(t_0,u)|<13/(25\pi).
\tag{18}
\]
The change along the real output from zero to \(\beta\)
is nonpositive. Its initial downward height derivative
is also nonpositive, by the original principal return.
Twice integrating (18) gives a height cost at most
\(26/(625\pi)<208/15625\), using \(\pi>25/8\).
Therefore, since the first-angle crossing and charge
cancel at \(2\pi/3\),
\[
 \Re\Phi(t_0,u)
 <\frac{19}{12}+\frac1{300}+\frac{208}{15625}
 =\frac85-\frac1{46875}<\frac85 .
\tag{19}
\]
All estimates are for the original primitive over the
full real continuum in (1).

## 5. The full remaining current and the source ceiling

The original one-current identity is already valid
on all of \(\mathcal U_+\), including (1).
Its local Gaussian has the same \(\mathcal A,S\);
all other previously paid terms have rate \(s-\epsilon_0\)
for some uniform \(\epsilon_0>0\).
Its literal remaining current has scalar
\(-N^2C_{N,3}/(\pi i)\) and integrand
\[
 \sin t\,K_N^<(t,0)K_N^<(t,u)
       e^{3iNt^2/(4\pi)}
          \frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\tag{20}
\]
Replace its path, with no crossed sampling pole, by
\[
 \pi/2-iH_*(u)\ \longrightarrow\
 2\pi/3-iH_*(u)\ \longrightarrow\
 2\pi/3-i/10\ \longrightarrow\
 a_0-i/10\ \longrightarrow\ 5\pi/6-i/10 .
\tag{21}
\]
The complete first-short slit bound applies everywhere
on this compact path. The full trace multiplier has
rate \(-H\), uniformly for all its heights.

On the high horizontal the original phase descent gives
rate at most \(s-\epsilon_1\), with \(\epsilon_1>0\) uniform
on (1), because \(\max a_*<\pi/2\).
The competing endpoint-sector rate is less than \(33/20\):
the independent first-edge calculation only uses
\(a\le2\pi/3,H\le1,K\le2/5\), with the actual \(H_*>2/3\).
The latter height bound follows from the same original
imaginary cubic equation, since \(\Im\cos(u/2)\ge0\).

On the vertical, the original geometric rate is convex
in height. Its endpoints are bounded by
\(s-\epsilon_1\) and \(8/5\), by (19).
The endpoint-sector rate increases with height and is
bounded by its already controlled upper endpoint.
The estimate (16) consequently bounds this whole piece
at rate \(\max(s-\epsilon_1,33/20)+\tau\).

Along the initial low horizontal both the geometric
and endpoint-sector rates decrease with the first real
angle, by the original positive-phase return bounds
on the whole outgoing \(\mathcal U_+\).
Equation (16) retains the entire source on this piece.
Finally the original far-low slit proof depends only
on \(K\le2/5\), not on the outgoing real angle.
It bounds the last horizontal, with the full (20),
by rate \(329/200<33/20\).

Fix any \(\tau>0\) and choose the finite edge tolerances
smaller than a fixed fraction of it. The contour lengths,
all polynomial factors, and the original \(N^2\) scalar
can be absorbed in the remaining tolerance. Thus the
complete current (21) has rate
\(\max(s-\epsilon_1,33/20)+\tau\).
Combining it with the original one-current identity
proves (3)--(4) for \(Q_N^{\rm sh}\), with
\(\epsilon=\min(\epsilon_0,\epsilon_1)>0\).

The full outgoing-tail difference is independently bounded
on the entire strip under consideration by
\[
                  CN^A e^{47N/30}.
\tag{22}
\]
Since \(47/30<33/20\), it is included in (4), proving
the same statement for \(Q_N^{\rm full}\).
The leading amplitude is bounded on the compact domain,
so (2) follows.

This is a complete continuum source ceiling beyond
\(\Re u=8/7\). Applying it to an outer contour still
requires paying both its geometric and endpoint-sector
rates with the original outer crossing, charge, sampling
kernel and reflected factor. No such comparison is
inferred from the source theorem alone.

## Frozen source bindings

- Original whole cubic and action:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Original single-current identity:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
- Exact source normalization and selected-curve assembly:
  e3bc75e93e1c1834faa920ff2f4ef0711c8f6cc7906b6c0c5b59bbadc86f57b7.
- Original incoming and outgoing cut formulas:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Original low-cut calculation and exact finite assembly:
  2f0287cf9655c04d2b9ca0a1545707619b57f23e899c3b76430c73b143929141.
- Complete upper envelope and its side formulas:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Complete vertical aliases and physical endpoints:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Complete axis residue formula:
  8cdfab84a1b0dfb817efe41b79caa5cc74fc62fce01bac54adddd54115507d90.
- Original endpoint-sector ceiling:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Original low-height first-edge estimate:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Original positive-phase extension and returns:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- Complete first-short slit theorem:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Complete far-low horizontal:
  1cb4d220d4fbf5fddeaf9ecb24b572908a4485e907ac4634ea2623acee0b34bd.
- Full outgoing-tail restoration:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.

