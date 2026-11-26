# An all-parity comparison for a whole low-Newton multiplication hub

Private proof, 1 November 2026. No repository file is changed.

The alternating Fourier terms at even levels can be controlled without taking their cancellation for granted. The comparison passes through the adjacent odd level and returns to the original even positive Newton trace. Both changes have only polynomial cost for a fixed number of input factors. The adjacent level is an auxiliary estimate, not a change in the level of the physical invariant.

The exact Fourier identity and odd-level argument are in `/private/tmp/md-odd-level-low-newton-hub-trace-comparison.md`. The positive complete multiplication law is `notes/actual_positive_newton_multiplication.md`. The proof below uses the entire trace after quotient reduction, including all return sectors and first normals.

## 1. Statement and the exact finite trace

At level \(N\ge2\), put \(d=N-1\), \(m_N=\lfloor d/2\rfloor\), and
\[
S_r^{(N)}=\prod_{a=1}^{r}2\sin(\pi a/N),\qquad
 e_n^{(N)}(z)=\frac{\prod_{a=0}^{n-1}(2\cos((2a+1)\pi/N)-z)}{(S_n^{(N)})^2}.
\tag{1}
\]
For the moving quotient \(P_{N,s}=\mathsf T_N+2\cos2\pi s\), define
\[
\phi_{N,s}(F)=(-1)^{N-1}N^2[z^{N-1}]\operatorname{rem}_{P_{N,s}}F.
\tag{2}
\]
Fix the number \(B\) of multiplied factors and a finite parameter radius \(R\). There exist constants \(C_{B,R},A_B\), independent of level and all low indices, such that
\[
\boxed{\quad
\left|\phi_{N,s}\left(\prod_{i=1}^{B}e_{n_i}^{(N)}\right)\right|
 \le C_{B,R}N^{A_B}
 \phi_{N,0}\left(\prod_{i=1}^{B}e_{n_i}^{(N)}\right),
\quad n_i\le m_N,\quad |s|\le R.
\quad}
\tag{3}
\]
At odd levels the polynomial factor can be omitted. A zero on the right forces the left to vanish as well. The radius restriction \(R<1\) is not needed for this trace identity; it is needed separately when applying a physical pre-resonance turn or crossing bound.

Write \(D=\sum_i n_i\), and
\[
F_N(-u-u^{-1})=\sum_{k=-D}^{D}a_k^{(N)}u^k,
\quad d_l^{(N)}=a_{lN-1}^{(N)}-a_{lN+1}^{(N)},
\quad L_N=\lfloor(D+1)/N\rfloor.
\]
The exact trace formula is
\[
\phi_{N,s}(F_N)=N^2\sum_{l=1}^{L_N}
 (-1)^{(N+1)(l+1)}d_l^{(N)}
 U_{l-1}(\cos2\pi s).
\tag{4}
\]
It follows by generic Lagrange interpolation and the root-of-unity sum, and extends through all collisions as a polynomial identity in \(2\cos2\pi s\). The factor count bounds \(L_N\le B\). Every low Newton factor has positive symmetric unimodal Laurent coefficients
\[
[u^{k-n}]e_n^{(N)}(-u-u^{-1})
 =\frac{S_{2n}^{(N)}}{(S_n^{(N)})^2S_k^{(N)}S_{2n-k}^{(N)}},
\qquad0\le k\le2n<N.
\tag{5}
\]
Products preserve that property, so all \(d_l^{(N)}\ge0\). The bound
\[
|U_{l-1}(\cos2\pi s)|\le l e^{2\pi(l-1)R}
\tag{6}
\]
proves (3) immediately at odd levels. At even levels it only gives an absolute sum; the following two comparisons recover the original complete trace.

If \(D<N-1\), both sides of (3) are zero by degree, regardless of the quotient. Hence assume \(N\) is even and \(D\ge N-1\). The case \(N=2\) cannot satisfy this assumption because every low index is zero. We may take \(N\ge4\), set \(L=N-1\), and use the same indices at the odd level \(L\). Their common low bound is
\[
m=m_N=m_L=(N-2)/2.
\tag{7}
\]

## 2. Adjacent sine factorials have polynomial ratios

For \(1\le a\le N-2\), concavity of sine and the monotonicity of \(\sin t/t\) on \((0,\pi)\) give
\[
\frac{N(N-1-a)}{(N-1)(N-a)}
\le\frac{\sin(\pi a/(N-1))}{\sin(\pi a/N)}
\le\frac N{N-1}.
\tag{8}
\]
For the lower bound reflect both sine arguments about \(\pi/2\), and apply \(\sin(\lambda t)\ge\lambda\sin t\) with
\(\lambda=N(N-1-a)/((N-1)(N-a))\le1\). Multiplication telescopes:
\[
\left(\frac N{N-1}\right)^r\frac{N-1-r}{N-1}
\le\frac{S_r^{(L)}}{S_r^{(N)}}
\le\left(\frac N{N-1}\right)^r,
\qquad0\le r\le N-2.
\tag{9}
\]
There is a sharper exact bound in the even-level case used here:
\[
\frac1L\le\frac{S_r^{(L)}}{S_r^{(N)}}\le\sqrt2,
\qquad0\le r\le N-2.
\tag{9a}
\]
To see it, write \(N=2h\), so \(L=2h-1\). The individual sine ratio in (8) is at least one exactly when \(r\le NL/(N+L)\), whose floor is \(h-1\). The partial product ratio therefore increases to \(r=h-1\) and decreases afterward. Its maximum is
\(S_{h-1}^{(L)}/S_{h-1}^{(N)}=\sqrt{2L/N}<\sqrt2\), by reflection of the full sine products. Its endpoint value is \(2L\sin(\pi/N)/N\ge4L/N^2\ge1/L\); the other endpoint is one. This proves (9a).

In particular these ratios and their reciprocals are polynomial in \(N\), uniformly in \(r\). Replacing an index by one more or one less still costs only a polynomial whenever both indices are allowed: every added factor lies between \(4/N\) and \(2\).

Apply (9) to (5). Every individual Laurent coefficient at level \(N\) is bounded by a fixed power of \(N\) times the corresponding coefficient at level \(L\). Convolution of the \(B\) positive factors preserves this comparison term by term. Thus there is a constant exponent \(A'_B\) such that
\[
a_k^{(N)}\le C_B N^{A'_B}a_k^{(L)}
\quad\text{for every integer }k.
\tag{10}
\]
This comparison preserves the support exactly. It is not an asymptotic approximation of the two trigonometric products.

## 3. A discrete tail difference controls the tail coefficient

**Lemma.** Let \(f_1,\ldots,f_B\) be nonnegative symmetric unimodal sequences, each supported on the integers \([-m,m]\). Let \(a=f_1*\cdots*f_B\). Then, for every integer \(k\ge m\),
\[
a_k\le(2m+1)^B(a_k-a_{k+2}).
\tag{11}
\]

Write each sequence as a nonnegative linear combination of interval indicators:
\(f_i=\sum_{r=0}^{m}(f_i(r)-f_i(r+1))\mathbf1_{[-r,r]}\).
It suffices to prove (11) for convolutions of these indicators. Let the radii be \(r_1,\ldots,r_B\), with largest radius \(r\). Such a convolution \(C\) is symmetric unimodal, positive at every integer of its support, and satisfies
\[
C(k)>C(k+1)\quad\text{whenever }k\ge r\text{ and }C(k)>0.
\tag{12}
\]
For completeness, prove (12) by induction on \(B\), choosing a factor with largest radius \(r\). If \(H\) is the convolution of the other factors, then
\(C(k)-C(k+1)=H(k-r)-H(k+r+1)\).
For \(k\ge r\), both arguments are nonnegative. If \(C(k)>0\), the first lies in the support of \(H\). If the second is outside that support the difference is positive. Otherwise the induction hypothesis gives a strict decrease at its last step, since \(k+r\) is at least the largest radius of \(H\); monotonicity handles the intervening steps. The one-factor case is immediate. This also covers zero radii.

The quantities in (12) are integers. Thus \(C(k)-C(k+2)\ge1\) whenever \(C(k)>0\) and \(k\ge r\), while \(C(k)\le\prod_i(2r_i+1)\le(2m+1)^B\). The same inequality is trivial if \(C(k)=0\). Sum the interval decompositions to obtain (11).

For each even-level alias \(1\le l\le L_N\), put \(k_l=lL-1\). Then \(k_l\ge L-1=2m\). Unimodality, (10), and (11) give
\[
\begin{aligned}
d_l^{(N)}
&\le a_{lN-1}^{(N)}
 \le C_BN^{A'_B}a_{lN-1}^{(L)}
 \le C_BN^{A'_B}a_{lL-1}^{(L)}\\
&\le C_BN^{A'_B+B}
 \bigl(a_{lL-1}^{(L)}-a_{lL+1}^{(L)}\bigr).
\end{aligned}
\tag{13}
\]
The odd-level alias range contains this range because \(L<N\). Its complete trace has only positive terms. Equations (4), (6), and (13) therefore prove
\[
|\phi_{N,s}(F_N)|\le C_{B,R}N^{A''_B}\phi_{L,0}(F_L).
\tag{14}
\]
No cancellation of the even alternating terms has been assumed. They were bounded by the actual positive odd trace.

## 4. Returning to the original even-level positive trace

The complete Newton law is
\[
e_i^{(K)}e_j^{(K)}=
\sum_{r=\max(i,j)}^{i+j}\mu_K(i,j;r)e_r^{(K)},
\qquad
\mu_K(i,j;r)=
\frac{S_{i+j}^{(K)}S_r^{(K)}}
 {S_i^{(K)}S_j^{(K)}S_{r-i}^{(K)}S_{r-j}^{(K)}S_{i+j-r}^{(K)}}>0,
\tag{15}
\]
when \(i+j<K\); the product is zero when \(i+j\ge K\). The trace extracts the last basis coefficient. Expand \(F_L\) by successive multiplication in the original fixed order. An admissible path starts with \(r_1=n_1\), ends with \(r_B=L-1=N-2\), and at every gate has
\[
r_{j-1}+n_j\le N-2,\qquad
\max(r_{j-1},n_j)\le r_j\le r_{j-1}+n_j.
\tag{16}
\]
Define its slack at gate \(j\) to be \(r_{j-1}+n_j-r_j\). The sum of its slacks is \(D-(N-2)\ge1\). Choose the first gate \(j_0\) with positive slack, and construct an even-level path by
\[
r'_j=r_j\quad(j<j_0),\qquad
r'_j=r_j+1\quad(j\ge j_0).
\tag{17}
\]
At the first changed gate the positive slack makes its new output admissible. At subsequent gates both the incoming running index and output increase by one, so the upper and lower gate inequalities persist; their input sum increases from at most \(N-2\) to at most \(N-1\), still strictly below the even level \(N\). The path now closes at \(r'_B=N-1\). All leaf indices stay unchanged.

For a given image path and \(j_0\), its preimage is unique, so the map has multiplicity at most \(B-1\). Each factorial argument in an image gate differs from its old argument by at most one. The only decrease, at the first changed slack, is legitimate because that slack was positive. Equations (9) and (15) thus bound each old gate coefficient by a fixed polynomial in \(N\) times its image coefficient. There are \(B-1\) gates. Summing these positive path weights yields
\[
\phi_{L,0}(F_L)\le C_BN^{A'''_B}\phi_{N,0}(F_N).
\tag{18}
\]
If there are no old paths, the left side is zero and the inequality remains valid. The construction itself is exact and includes all support-boundary cases; no interior saddle or lower asymptotic coefficient estimate is used.

Combining (14) and (18) proves (3) at even levels. Together with the odd proof and the trivial degree cases, it proves the all-level theorem.

## 5. Actual low arrays, low outputs, and the remaining scope

Let \(F_i=\sum_{n\le m_N}f_{i,n}e_n^{(N)}\), and \(F_i^{\mathrm{abs}}=\sum|f_{i,n}|e_n^{(N)}\). Multilinear expansion of the inputs and (3), followed by the triangle inequality, give
\[
\left|\phi_{N,s}\left(\prod_{i=1}^B F_i\right)\right|
 \le C_{B,R}N^{A_B}
 \phi_{N,0}\left(\prod_{i=1}^B F_i^{\mathrm{abs}}\right).
\tag{19}
\]
This is a finite whole-hub comparison for arbitrary complex low-coordinate arrays. The factor count is fixed before taking \(N\to\infty\). It is not an assertion that an absolute value can be passed through a Laurent-coefficient difference.

For a physical turned output \(k\le m_N\), insert the additional low probe \(e_k\) before the trace and retain the exact paired prefactor
\[
[e_k]\mathscr T_s^{\mathrm{fix}}\left(\prod_iF_i\right)
 =\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}
   \phi_{N,s}\left(e_k\prod_iF_i\right).
\tag{20}
\]
On \(|s|\le R<1\), that prefactor is uniformly bounded. Thus (19) gives the original positive low-probe comparison, at both parities, with only polynomial cost. It can be combined with any established complete positive-probe estimate at its actual geometric pressure.

This theorem does not yet control a high input or high output/probe. Those basis polynomials lack the positive unimodal Laurent coefficients used here. An intermediate physical turn may produce high coordinates, so arbitrary trees do not follow by iterating (19) alone. The adjacent-level comparison is only an algebraic estimate inside this proof: it does not identify invariants, colors, framings, or knot volumes at different levels.
