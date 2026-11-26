# The physical half-node outgoing kernel with its exact middle amplitude

Private finite-source estimate, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source
change is used.

The exact normalized physical-index amplitude may be inserted into
the outgoing type-three kernel at the original first right physical
node. Its complete finite sum still has the established conditional
profile bound. The lower aliases are retained with the amplitude's
explicit growth cost. This does not bound the remaining internal
index sum or the complete next transfer.

## 1. Actual reference and exact weighted observation

Use the actual complete words in powers three and four beginning
\(343\), of length \(m\ge5\), and their base outside parameters.
Retain the original next private height \(h_t=\Im s_3^*\), output
\(z=z_*=u+ih_z\), and comparison plane
\[
 -3/100<h_t,h_z<1/50,\qquad
 3/10\le u\le39/100,\qquad
 Z=e^{-2\pi iz},\quad 4/5<|Z|<8/7,
\]
\[
 B_0=2383/1500,\qquad B_f=77/50+\pi/50,\qquad
 \Lambda=\Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*)>419/200.
 \tag{1}
\]
These are the actual correlated reference domains, not an
independent replacement of its heights.

Put
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,\\
 y_N=M/N,\quad Y_N=r^M,\quad
 L=\lfloor N/6\rfloor,\quad K=\lfloor N/4096\rfloor,\\
 P_k=(r;r)_k,\qquad p_k(Z)=(rZ;r)_k .
\end{gathered}
 \tag{2}
\]
Thus \(Y_N=-1\) at even levels. At odd levels it is the original
node \(r^{(N+1)/2}\), not the substituted value \(-1\).

Let \(\mathfrak G_N(\eta,t)\) be the exact entire amplitude of
[the analytic-amplitude theorem, equation (2)](research_mixed_next_middle_exact_analytic_amplitude.md),
with these unchanged \(L,U\). Its upper-half-plane extension in
[the half-disk amplitude theorem, Section 6](research_mixed_next_middle_outgoing_half_disk_amplitude.md)
supplies a fixed complex neighborhood \(\mathscr V\) of
\([1/64,1/2]\) on which
\[
 |\mathfrak G_N(\eta,t)|
 \le C\exp\{2\pi(U-L)(-\Im t)_+\}
 \le C\exp\{(2\pi N/3)(-\Im t)_+\},
 \quad 0\le\Re t\le1/2,\quad \eta\in\mathscr V .
 \tag{3}
\]
Indeed \(U-L<N/3\). This bounds the entire exact finite
amplitude, including its stopped products and genuine \(L\)-tail;
no approximate symbol is substituted for it.

Define
\[
\begin{split}
 \mathcal C_N^{G}(\eta,Z)
 &=\sum_{k=0}^{U}
    \frac{Y_N^{-k}p_k(Y_N)p_k(Z)}{P_k^2}
                           \mathfrak G_N(\eta,k/N),\\
 \mathcal C_N^{G,>}(\eta,Z)
 &=\sum_{k=K+1}^{U}
    \frac{Y_N^{-k}p_k(Y_N)p_k(Z)}{P_k^2}
                           \mathfrak G_N(\eta,k/N).
\end{split}
 \tag{4}
\]
These are the literal original outgoing rows. All rows above
\(U=D-M\) vanish exactly at \(Y_N\).

**Theorem.** On a possibly smaller fixed \(\mathscr V\), for
each fixed \(\tau>0\),
\[
 \boxed{\quad
 |\mathcal C_N^{G}(\eta,Z_*)|
   +|\mathcal C_N^{G,>}(\eta,Z_*)|
 \le C_\tau N^{A_\tau}
     e^{N\{\Lambda-B_0-1/50+\tau\}}.
 \quad}
 \tag{5}
\]
The constants include both parities. Every fixed derivative in
\(\eta\) has the same bound on a smaller fixed neighborhood.

In particular, for any factor \(V_N\) independent of the outgoing
index, with \(|V_N|\le CN^a e^{NB_f}\), both products in (5)
obey
\[
 |V_N\mathcal C_N^{G}|+|V_N\mathcal C_N^{G,>}|
 \le C'N^{a'}e^{N(\Lambda-1/1000)} .
 \tag{6}
\]
No hypothesis that the remaining internal-index observation has
this preceding bound is asserted.

## 2. The original conditional calibration

Keep the original logarithmic phase
\[
 Q(t;y,z)=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt .
 \tag{7}
\]
On the original regular strip,
\(g'(w)=\Log(1-e^{-2\pi iw})\), with its original continuous
principal-strip lift. All constants in (7) are unchanged.

The factor-independent calibration in
[half-period bounded prefix, equations (13),(17),(19)](research_mixed_next_three_half_grid_bounded_prefix.md)
gives, at \(y=1/2\),
\[
 B_0+\Re Q(v+ih_t;1/2,z)<\Lambda-1/50,
                 \qquad 3/20\le v\le1/2,
\]
\[
 B_0+\Re Q(v;1/2,z)<\Lambda-1/50,
                         \qquad v=3/20,\ 1/2 .
 \tag{8}
\]
The half-index values are the original zero-safe continuous
upper rates. The proof of (8) compares every fixed profile
before finite summation. It is not inferred from a bound
for a coherent kernel. Its domain includes the shared height
zero between the actual lower height and \(1/100\).

We change the private main height only when it is negative:
\[
                       h_+=\max\{h_t,0\}\le1/50 .
 \tag{9}
\]
We now prove that this preserves each main upper bound in (8).

## 3. Raising a negative main height

For a real private index \(0<v<1/2\), the exact derivative of
(7) at \(y=1/2\) satisfies
\[
 e^{Q_t}
   =-\frac{(1+\xi)(1-Z\xi)}{(1-\xi)^2}
   =\frac{\cos(\pi v)}{2\sin^2(\pi v)}
             e^{i\pi v}(1-Ze^{-2\pi iv}),
 \qquad \xi=e^{-2\pi iv}.
 \tag{10}
\]
The original logarithmic lift, not only its exponential, has
\[
 \Im Q_t=\pi v+
       \Arg(1-|Z|e^{-2\pi i(u+v)}).
 \tag{11}
\]
Indeed the incoming argument is \(-\pi v\), the own
argument is \(\pi/2-\pi v\), and the chirp contributes
\(+\pi\). Thus no unverified multiple of \(2\pi\) is
removed in (11).

Write \(\rho=|Z|\). The complex number in the last factor
of (10) has real and imaginary parts
\[
\begin{split}
 \Re[e^{i\pi v}(1-Ze^{-2\pi iv})]
       &=\cos(\pi v)-\rho\cos(2\pi u+\pi v)>0,\\
 \Im[e^{i\pi v}(1-Ze^{-2\pi iv})]
       &=\sin(\pi v)+\rho\sin(2\pi u+\pi v)>0 .
\end{split}
 \tag{12}
\]
For the first sign, \(2u+v\in[3/5,32/25]\subset(1/2,3/2)\).
For the second, divide by \(\sin(\pi v)>0\):
\[
 1+\rho\cos(2\pi u)+\rho\sin(2\pi u)\cot(\pi v)
       \ge1-\frac87\cos(11\pi/50)>\frac3{35}.
 \tag{13}
\]
The last elementary bound follows from
\(11\pi/50>2/3\) and
\(\cos(2/3)\le191/243<4/5\).
These use only \(\pi>25/8\) and the alternating cosine series.
Equations (11)--(13) therefore prove
\[
                  0<\Im Q_t(v;1/2,z)<\pi/2 .
 \tag{14}
\]

The real private curvature is
\[
 \Re Q_{tt}=\pi\Re\{\cot\pi(1/2+t)+\cot\pi(z+t)
                                      -2\cot\pi t\}.
 \tag{15}
\]
For \(1/5\le v\le1/2\), both shifted real coordinates are
at least \(1/2\) and at most one, so their real cotangents
are nonpositive at every height; the own cotangent is
nonnegative. At the limiting half index the outgoing
cotangent is strictly negative.

For \(3/20\le v\le1/5\) and \(|\Im t|\le3/100\), the
incoming cotangent is still nonpositive. Any positive
outgoing cotangent is at most
\[
 \cot(9\pi/20)=\tan(\pi/20)<1/5 .
 \tag{16}
\]
For example \(\pi/20<1/6\), so
\(\tan(\pi/20)<(1/6)/(1-1/72)=12/71<1/5\).
In the same range the own real cotangent is greater than one:
\[
 \frac{\sin(2\pi v)}
      {\cosh(2\pi\Im t)-\cos(2\pi v)}
 >\frac{4/5}{21/20-3/10}
 =\frac{16}{15}>1 .
 \tag{17}
\]
Here \(\sin(3\pi/10)>4/5\),
\(\cos(2\pi/5)>3/10\), and
\(\cosh(3\pi/50)<\cosh(1/5)<21/20\).
The trigonometric bounds follow from the elementary exact
values and \(\sqrt5>11/5\).
For the last bound the positive series gives
\[
 \cosh(1/5)
 \le1+\frac1{50}+
       \frac{1/15000}{1-1/750}<21/20 .
 \tag{18}
\]
Thus (15) is negative throughout the needed height strip.

If \(h_t<0\), equations (14)--(17) imply
\(\Im Q_t(v+i\sigma)>0\) for \(h_t\le\sigma\le0\),
because \(\partial_\sigma\Im Q_t=\Re Q_{tt}<0\).
Since \(\partial_\sigma\Re Q=-\Im Q_t\), raising the
height from \(h_t\) to zero only lowers the rate. If
\(h_t\ge0\), it is unchanged. We have proved
\[
 B_0+\Re Q(v+ih_+;1/2,z)<\Lambda-1/50
                  \quad(3/20\le v\le1/2).
 \tag{19}
\]
At the half-index numerator zero these comparisons use
one-sided regular-strip limits and the continuous upper
envelope. No relative factorial symbol at that zero is used.

## 4. Exact finite interpolation and the complete currents

Let
\[
 a_N=\frac{\lfloor3N/20\rfloor+1/2}{N},\qquad
 b_N=\frac{U+1/2}{N}.
 \tag{20}
\]
The low physical group is \(0\le k\le\lfloor3N/20\rfloor\).
The remaining group is
\(\lfloor3N/20\rfloor+1\le k\le U\), between the
half-grid cuts (20). Crucially, at both parities,
\[
                    y_N+b_N=1-\frac1{2N}.
 \tag{21}
\]
Thus the incoming factorial remains prewall throughout
the entire chosen rectangle; the original first terminating
zero is outside it. The cuts are not replaced by \(\Re t=1/2\)
in an exact residue identity.

Keep the original canonical interpolant
\[
 T_{0,N}(t;y_N,z)
 =e^{2\pi iNy_Nt}\Pi_N(y_N+t)\Pi_N(z+t)
                    E_N(y_N)E_N(z)E_N(t)^2 .
 \tag{22}
\]
At \(t=k/N\), this is exactly
\(Y_N^{-k}p_k(Y_N)p_k(Z)/P_k^2\).
The functions \(\Pi_N,E_N\), their period factors and their
normalization are those of
[complete canonical currents, equations (4)--(6)](research_mixed_next_lower_left_complete_currents.md).
Multiply (22) by the entire factor
\(\mathfrak G_N(\eta,t)\). No pole or branch is added.

Apply the same exact split cotangent identity, with lower
height \(-1/5\) and upper height \(8\), to this product.
It retains:
the original \(+N\) real middle integral;
both horizontal remainders;
the lower and upper parts of both vertical sides.
Deform the middle integral to height \(h_+\), retaining
both unweighted joining segments. These are six weighted
currents and two unweighted joins, not discarded boundary
terms.

At the limiting input \(y=1/2\), the original argument
estimate in
[half-period bounded prefix, equation (20)](research_mixed_next_three_half_grid_bounded_prefix.md)
is
\[
        -39\pi/50\le\Im Q_t\le11\pi/10 .
 \tag{23}
\]
It holds for the whole private rectangle just specified,
independently of the sign of either shifted height. The
incoming shifted real coordinate is at least \(1/2\);
the output and own arguments have precisely the domains
used in that proof. In particular no outgoing Fourier
forcing is removed in applying this conditional-row bound.

For the lower horizontal, comparison with a main profile at
height \(h_+\), the lower cotangent kernel, and (3) give
the additional exponent at most
\[
 N\pi\left\{\frac{11}{10}(1/5+h_+)
                   -\frac25+\frac{2}{15}\right\}
 \le-\frac{37\pi}{1500}N .
 \tag{24}
\]
The amplitude cost \(2\pi/15\) is its entire lower-height
growth cost, not a dropped tail. On a lower vertical side
at height \(-d\), \(0\le d\le1/5\), comparison with its
real-cut endpoint instead gives
\[
 N\pi\{11d/10-2d+2d/3\}
                  =-\frac{7\pi}{30}Nd .
 \tag{25}
\]
Thus both complete lower weighted sides are controlled
by their real cuts. At a half grid the exact cotangent
remainder is bounded by \(2e^{-2\pi N d}\), also at
\(d=0\); there is no pole or lost endpoint factor there.

On the upper half of the rectangle, (3) is bounded by
a constant. Equation (23) gives decrease at least
\(61\pi/50\) per unit upper height on each weighted
side. The upper horizontal has loss at least
\[
 16\pi-\frac{39\pi}{50}(8-h_+)>0
 \tag{26}
\]
relative to the main line. The corresponding horizontal
cotangent estimates retain their full nonconstant Fourier
remainders, with polynomial prefactors only.

For the unweighted joins, \(0\le\sigma\le h_+\le1/50\).
At the low cut (15)--(18) give vertical convexity of
\(\Re Q\), and at the half cut the shifted cotangents are
nonpositive and the own cotangent has its zero limit.
Hence each join is bounded by its main or real-cut
endpoint, both paid in (8),(19). The exact amplitude is
bounded on the entire joins by (3).

All estimates so far use limiting cut profiles at
\(y=1/2,\ a=3/20,\ b=1/2\).
The exact \(y_N,a_N,b_N\) differ by \(O(N^{-1})\).
Original uniform factorial upper bounds and integrated-log
continuity give rate changes \(O((\log N)/N)\), hence only
polynomial costs, including the half-index numerator wall.
Equation (21) also keeps every exact numerator argument
on its original prewall branch. The period/reflection
upper envelope supplies the limiting bound at the wall;
no division by its vanishing period factor, nonzero
symbol there, or new logarithmic lift is asserted.
The outgoing arguments have real part below
\(39/100+1/2<1\), and all reciprocal factors retain
their original regular domains.

Finally the positive low physical rows increase to the
low cut in the original bound of half-period bounded
prefix, Section 4. Its folded incoming modulus is greater
than \(15/16\), its outgoing modulus exceeds \(7/5\),
and its own squared denominator is less than one.
These inequalities apply at shared height zero.
The exact grid values (3) are bounded, so that entire
positive low-row estimate survives the multiplication.
It includes the true row \(k=0\). There is no upper
physical group beyond \(U\), since the next row and
every later row vanish at the original physical input.

Equations (8),(19),(24)--(26), both joins, and the low
group exhaust the finite sum (4). The original \(+N\)
measure and cotangent prefactors cost only powers of \(N\).
With an arbitrary common finite rate allowance \(\tau\),
they prove the first estimate in (5).

## 5. Removing the small outgoing indices and the exact remaining source

On the real grid the amplitude (3) is bounded. The positive
small-outgoing estimate in
[small outgoing indices, equations (9)--(14)](research_mixed_next_three_small_outgoing_indices.md),
applied at \(n=U\), gives
\[
 \sum_{k=0}^{K}
 \left|\frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}
                     \mathfrak G_N(\eta,k/N)\right|
       \le CN^A e^{N/200}.
 \tag{27}
\]
For sufficiently large \(N\), \(K<U\).
The target profile exponent is strictly greater than this
rate by the actual action floor:
\[
 \Lambda-B_0-1/50>
 \frac{419}{200}-\frac{2383}{1500}-\frac1{50}
 =\frac{1459}{3000}>\frac1{200}.
 \tag{28}
\]
Thus subtracting (27) from the complete weighted sum proves
the high-\(k\) bound in (5), uniformly on the same complex
\(\eta\)-neighborhood. Since both sums in (4) are holomorphic
in \(\eta\), Cauchy's formula proves the fixed derivative
assertion on a smaller fixed neighborhood.

For (6), use the exact reserve from half-period bounded
prefix, equation (24):
\[
 B_f-B_0<149/10500,\qquad
 1/50-149/10500=61/10500>1/200 .
 \tag{29}
\]
Choose, for example, a common finite allowance
\(\tau=1/1000\). The remaining gap exceeds \(1/1000\),
which proves (6).

To state precisely how (5) enters the restored source,
define the exact parity factor
\[
 A_{j,N}=
 \begin{cases}
 1/2,&N=2m,\\
 2\sin(\pi(m-j)/N)/\{4\cos^2(\pi/(2N))\},&N=2m+1 .
 \end{cases}
 \tag{30}
\]
The original endpoint factorial identity gives
\(a_U^{j,k}=A_{j,N}S_U/S_{U-k}\). Therefore
\[
 i^kq^{k(k-1)/2-(k+1)U}
       \frac{a_U^{j,k}p_k(Z)}{S_k^2}
 =q^{-U}A_{j,N}
           \frac{Y_N^{-k}p_k(Y_N)p_k(Z)}{P_k^2}.
 \tag{31}
\]
This is exact at both parities. In particular it introduces
no analytic approximation of the endpoint factorials.

Consequently the remaining source in
[restored middle, equation (16)](research_mixed_next_three_restored_middle_large_indices.md)
has the exact form
\[
 \mathscr R_N^{\rm both}
 =\frac{\kappa(-q)^Dq^{-U}}{N}
 \sum_{j=\lfloor N/64\rfloor+1}^U
 2\sin((2j+1)\pi/N)\,q^{3j(j+1)} A_{j,N}
 \mathcal K_{3,N}(-2,c_j)\,
                        \mathcal C_N^{G,>}(j/N,Z_*).
 \tag{32}
\]
The full Hermite kernel, its repeated-root normals and the
outer chirp are retained. The new estimate controls the
complete outgoing observation with the exact inserted
amplitude. It does not show that the remaining \(j\)-sum,
or its preceding factors, have the allowance required by
(6). No full-transfer asymptotic, noncancellation conclusion,
new outside-variable jets, or volume statement follows
from (5) alone.

