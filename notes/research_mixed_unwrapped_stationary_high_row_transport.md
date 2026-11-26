# The complete joint high-row block before the second leg wraps

Research deduction, 10 November 2026. At the original fixed heights
of an actual first cap and its ordinary neighbor, the joint
first-coordinate derivative is positive at every stationary physical
row between one half and the reflected second target. This includes
both own types, all five complex cap profiles, and the separate
true-end cap profile. An envelope argument then pays the complete
finite block before the second leg wraps, without selecting a
differentiable critical branch. The remaining wrapped strip is
stated explicitly below.

## 1. Original source and actual height inputs

Fix an actual positive three/four open word of length at least three.
The first and second types are \(3+\alpha,3+\epsilon\).
Retain the actual reference heights \(c,d\), and put
\[
 a=x+ic,\quad b=z+id,\qquad
 1/10\le x\le11/50,\quad 11/50\le z\le9/20,\qquad
 r=e^{2\pi c},\quad t=e^{2\pi d}.
\tag{1}
\]
These are fixed-height targets, not a new moving critical reference.
The endpoint rectangle and the coupled attached-four theorem give
\[
 c>-.072\quad(\alpha=0),\qquad
 -.078<c<-.020\quad(\alpha=1),\qquad c<.021.
\tag{2}
\]
The ordinary output has
\[
 -.065<d<.068\quad(\epsilon=0),\qquad
 -.102<d<-.001\quad(\epsilon=1).
\tag{3}
\]
The use of the full ordinary block image at an open reference is
licensed by the open local-factor coverage theorem, Section 1.
No cyclic repetition or independent endpoint input is substituted.

The following convenient consequences will be used:
\[
 \frac35<r<\frac{23}{20},\qquad
 \begin{cases}
  13/20<t<31/20,&\epsilon=0,\\
  1/2<t<1,&\epsilon=1.
 \end{cases}
\tag{4}
\]
For the new lower first-radius bound, the positive atanh series gives
\(\log(5/3)>49/96> .156\pi\), using \(\pi<22/7\).
Likewise \(\log(20/13)>14/33>.13\pi\).
For the upper ordinary radius, put \(u=.136\pi<187/437\);
the elementary bound
\[
 e^u\le1+u+\frac{u^2}{2(1-u/3)}
\]
at \(u=187/437\) equals \(1507659/982376<31/20\).
The remaining bounds in (4) are the original elementary radius
bounds used in the complete cap and joint low-row proofs.

Use the original phases \(\Xi_\alpha(e,a)\) and
\(F_{\alpha\epsilon}(s;a,b)\) of equation (7) of the joint
low- and half-row theorem. The cap parameter is fixed in
\[
 e\in[27/100,49/100]+i[-11/200,1/25].
\tag{5}
\]
This includes the main line, both real cuts, and both horizontal
aliases of the complete fixed-height cap theorem. Their alias
penalties are constant in \(x\).
The joint regular rate and the joint true-end rate are
\[
 \begin{split}
 H_e(x,s)&=\Re\{\Xi_\alpha(e,a)+F_{\alpha\epsilon}(s;a,b)\},\\
 H_{\rm end}(x,s)&=
 E_{\rm end}(c)-\frac{\alpha}{2}\Re g(a)
                         +\Re F_{\alpha\epsilon}(s;a,b).
 \end{split}
\tag{6}
\]
The same original cap true-end exponent \(E_{\rm end}\) is retained.
There is no first-color asymptotic or division by a finite row.

For real \(s\), write
\[
 \begin{gathered}
 Q=2\sin\pi s,\quad D=|1-r e^{-2\pi ix}|,\quad
 N_s=|1-r e^{-2\pi i(s+x)}|,\\
 N_b=|1-t e^{-2\pi i(s+z)}|,\quad
 N_e=|1-r e^{2\pi\Im e}e^{-2\pi i(\Re e+x)}|.
 \end{gathered}
\tag{7}
\]
The literal ordinary row ratio, including its first chirp, gives
\[
 \partial_s\Re F_{\alpha\epsilon}
       =\log\frac{N_sN_b}{rQ^{2+\epsilon}}.
\tag{8}
\]
Consequently at a stationary physical row,
\[
                         N_sN_b=rQ^{2+\epsilon}.
\tag{9}
\]
Its two joint derivatives are exactly
\[
 \partial_x H_e=\log\frac{N_eN_s}{D^{2+\alpha}},\qquad
 \partial_x H_{\rm end}=\log\frac{N_s}{D^{1+\alpha}}.
\tag{10}
\]
These derivatives keep the original two first-coordinate allocations.

## 2. A uniform cap numerator comparison

The same elementary angular bounds as in the joint low-row proof give
\[
 \begin{split}
 N_e^2&>
 A_0:=1+\frac49r^2+\frac8{25}r,\\
 D^2&<
 B_0:=1+r^2-\frac9{25}r<2.
 \end{split}
\tag{11}
\]
Indeed the private radius is at least \(2/3\),
\(\cos(2\pi(\Re e+x))<-6/25\), and
\(\cos(2\pi x)>9/50\). Since
\[
 A_0-B_0=r\left(\frac{17}{25}-\frac59r\right)>0,
\]
we have \(N_e>D\) for every profile in (5).
Also (4) gives
\[
 \frac{D^2}{r}<r+r^{-1}-\frac9{25}
                          \le\frac{143}{75}.
\tag{12}
\]
The endpoint maximum of \(r+r^{-1}\) on
\([3/5,23/20]\) is \(34/15\).

## 3. The second numerator before wrapping

Suppose
\[
                 1/2\le s\le1-z,\qquad v=1-s\in[z,1/2].
\tag{13}
\]
Set \(z_0=11/50\), \(c_0=\cos(2\pi z_0)\),
\(s_0=\sin(2\pi z_0)\). The original elementary bounds give
\[
 0<c_0<1/5,\quad s_0>49/50,\quad
 \cot(\pi z_0)<5/4,\quad
 2\sin(\pi z_0)>5/4,\quad \cos(\pi z_0)<4/5.
\tag{14}
\]
For explicit witnesses, the sine lower polynomial at
\(11/16<\pi z_0\) gives
\(\sin(\pi z_0)>15565/24576>5/8\).
The cosine upper polynomial through degree four at the same
argument gives
\(\cos(\pi z_0)<1215793/1572864<25/32\);
together these imply the cotangent bound. Finally
\(c_0=\sin(.06\pi)<33/175<1/5\), and
\(s_0=\cos(.06\pi)>1-1089/61250>49/50\).

First take \(\epsilon=0\). Since \(z\le v\), the second numerator
is largest at \(z=z_0\). Put \(q=\cot\pi v\) and
\[
 B=1+t^2-2tc_0,\qquad C=1+t^2+2tc_0.
\]
Direct substitution gives
\[
 \frac{N_b^2}{Q^4}
 \le\frac{(1+q^2)(Bq^2-4ts_0q+C)}{16}.
\tag{15}
\]
The right side is at most \(C/16\) for \(0\le q\le5/4\).
Indeed its difference from \(C/16\), multiplied by \(16/t\),
is
\[
 q\{(T-2c_0)q^3-4s_0q^2+2Tq-4s_0\},
 \qquad T=t+t^{-1}<11/5.
\tag{16}
\]
The expression in braces is strictly below
\[
 K(q)=\frac{11}{5}q^3-\frac{98}{25}q^2
                         +\frac{22}{5}q-\frac{98}{25}.
\]
Its derivative is positive on the real line: the quadratic
discriminant is \(-34184/625<0\) and its leading coefficient
is positive. Moreover \(K(5/4)=-397/1600<0\).
Thus (15) implies
\[
 \frac{N_b}{Q^2}\le\frac{\sqrt C}{4},
             \qquad \sqrt C<81/40.
\tag{17}
\]
For the last bound, \(t<31/20\) and \(c_0<1/5\) give
\(C<1609/400<(81/40)^2\).

If \(\epsilon=1\), retain its actual \(t<1\).
Convexity of the radial modulus gives
\[
 \frac{N_b}{Q}
 \le\max\left\{\frac1Q,
             \frac{\sin\pi(v-z)}{\sin\pi v}\right\}<\frac45.
\tag{18}
\]
Here \(Q>5/4\), and the second quotient is
\(\cos\pi z-\cot\pi v\sin\pi z\le\cos\pi z<4/5\).
The extra own-four factorial has not been discarded.

## 4. Positive stationary-row transport

**Theorem 1.** At every stationary real row satisfying (13),
both joint rates in (6) satisfy
\[
                 \partial_x H_e>1/50,\qquad
                 \partial_x H_{\rm end}>1/50.
\tag{19}
\]
If \(c\ge0\), both derivatives are greater than \(1/4\).
The statement holds for every fixed profile in (5), including
either alias and every point of the main private line.

*Proof.* For \(\epsilon=0\), (9) and (17) give
\(N_s>160r/81\). For either \(\alpha\), if \(D<1\), then
\[
 \frac{N_s}{D^{1+\alpha}}>160r/81>32/27.
\]
If \(D\ge1\), use (12) to obtain
\[
 \frac{N_s}{D^{1+\alpha}}\ge\frac{N_s}{D^2}
                    >\frac{12000}{11583}=\frac{4000}{3861}.
\tag{20}
\]
Thus its logarithm is greater than \(139/4000>1/50\).

For \(\epsilon=1\), equations (9), (18), and \(Q>5/4\) give
\[
                         N_s>\frac{125}{64}r.
\]
The same two cases yield
\[
 \frac{N_s}{D^{1+\alpha}}>
            \min\{75/64,9375/9152\}=9375/9152.
\tag{21}
\]
Its logarithm exceeds \(223/9375>1/50\).
The logarithm bounds use \(\log(1+h)>h/(1+h)\).
These prove the true-end assertion in (19). Since \(N_e>D\),
equation (10) proves the regular assertion as well.

Finally \(c\ge0\) implies \(\alpha=0\) and \(r\ge1\).
For \(\epsilon=0\), (11) and \(\sqrt2<10/7\) give
\[
 N_s/D>\frac{160}{81\sqrt2}>\frac{112}{81},
 \qquad \log(N_s/D)>\frac{31}{112}>\frac14.
\]
For \(\epsilon=1\), the same argument gives
\(N_s/D>(125/64)(7/10)=175/128\), whose logarithm is
greater than \(47/175>1/4\). This proves the final assertion.
\(\square\)

At a differentiable stationary branch \(s=s(x)\), equation (8)
vanishes, so its joint critical value has precisely the derivative
in (19). The theorem does not assume such a branch exists or choose
a quartic root. Its inequalities also hold at degenerate stationary
points; no division by a row second derivative occurs.

The upper endpoint of (13) cannot maximize the continuous row rate.
At \(s=1-z\), the literal ratio in (8) is strictly below
\[
 \frac{(1+r)|1-t|}{rQ^{2+\epsilon}}
 <\frac83\frac{11}{20}\frac{16}{25}
                         =\frac{352}{375}<1.
\tag{22}
\]
If \(t=1\), the ratio is zero and the one-sided logarithmic limit
has the same consequence. Moving slightly left increases the rate.

## 5. The complete unwrapped block and its calibrated gap

The complete fixed-height cap theorem additionally retains a
right-physical-row allowance \(\Delta_0<1/200\), only when
\(\alpha=0,c>0,x<4/25\). It is zero for \(x\ge4/25\) or
\(c\le0\). We pay it separately below, rather than differentiate
it or treat it as constant.

Write \(a_*=a_0+ic\) and retain exactly the allocated plane
\(\Gamma(z)\) from equation (9) of the joint low- and half-row
theorem. Put
\[
 \kappa=\frac1{2500000},\qquad
 \gamma_*=\kappa(a_0-11/50)^2>0.
\tag{23}
\]
The actual endpoint rectangles give \(.246<a_0<.391\), so
\(\gamma_*>\kappa(13/500)^2\) and \(2\gamma_*<1/2000\).

Let \(K(x)\) be the maximum of (6) over
\(1/2\le s\le1-z\) and over the five actual cap profile sets:
the full main line through \(\Im e_*\), the two real cuts,
and the two horizontal aliases with their original penalties.
Include \(H_{\rm end}\) in this same maximum.
The extra \(\Delta_0\) is not yet included in \(K\).
All profile sets and heights are fixed when \(x\) varies.

At \(x=11/50\), the completed cap plane bounds every cap profile,
including its true ends. The original plateau endpoint theorem,
half-row comparison and typed last-row comparison bound every
ordinary real rate in (13) by its original ordinary plane.
These are the profile statements used in the proof of the
three-row source assembly, not an estimate of an absolute sum
deduced from a bound on a signed kernel. The first-coordinate
marginals cancel exactly. Both first-coordinate quadratic losses
remain, so
\[
                   K(11/50)\le\Gamma(z)-2\gamma_*.
\tag{24}
\]
No numerical lower bound for the last-row deficit is needed.
At \(s=1/2\), every joint profile is at most
\(\Gamma(z)-1/2000\) by equation (23) of the separate joint
half-row proof, at every \(x\) under consideration.

First suppose \(c\le0\), so there is no additional cap allowance.
We claim \(K(x)\le\Gamma(z)-2\gamma_*\) throughout the early
interval. Otherwise, on a connected interval where this constant
barrier is exceeded, no maximizing profile can be at \(s=1/2\),
by the half-row bound. Equation (22) excludes \(s=1-z\).
Every maximizing row is therefore interior and stationary, and
Theorem 1 gives its \(x\) derivative greater than \(1/50\).
The envelope is consequently increasing on that interval, which
contradicts its exit through the barrier to the right and (24).

Here is a precise elementary justification for the envelope step.
The compact maximizing sets stay away from the upper endpoint,
uniformly locally in \(x\), by (22). All remaining joint profiles
are continuously differentiable in \(x\). If every active profile
has \(x\) derivative at least \(\delta>0\), compactness gives the
same bound with any smaller \(\delta'\) for all nearly active
profiles on a sufficiently small interval. Integrating these
fixed-profile inequalities and then taking the maximum gives
\(K(y)-K(x)\ge\delta'(y-x)\) there. Chaining intervals proves
the assertion. This also handles switches and degenerate critical
points. A zero numerator at the excluded upper endpoint causes
no problem: its exponentiated row ratio is continuous and
strictly below one on a uniform one-sided neighborhood.

Now suppose \(c>0\), so \(\alpha=0\). At an interior maximizing
row, Theorem 1 gives derivative greater than \(1/4\).
At \(s=1/2\), the regular cap profiles have positive derivative
everywhere and derivative greater than \(18/125>1/8\) when
\(x\in[4/25,11/50]\), by the joint half-row proof.
The true-end derivative at that row is \(\log(N_s/D)>0\).
On the same shorter interval it satisfies
\[
 \frac{N_s^2}{D^2}
 =1+\frac{4r\cos(2\pi x)}{D^2}>\frac{34}{25},\qquad
 \log(N_s/D)>\frac9{68}>\frac18.
\tag{25}
\]
Here \(r>1\), \(\cos(2\pi x)>9/50\), and \(D^2<2\).
Thus the envelope argument proves that \(K\) is nondecreasing
on the whole early interval and has slope at least \(1/8\)
on \([4/25,11/50]\). For \(x<4/25\), (24) gives
\[
 K(x)+\Delta_0
 \le K(4/25)+\frac1{200}
 \le\Gamma(z)-2\gamma_*-\frac3{400}+\frac1{200}
 =\Gamma(z)-2\gamma_*-\frac1{400}.
\tag{26}
\]
For \(x\ge4/25\), the allowance is zero and monotonicity gives
the bound (24). Therefore, for every height-sign class, the entire
cap envelope plus every ordinary rate in (13) is at most
\(\Gamma(z)-2\gamma_*\).

For clarity, the finite rows to which this applies are exactly
\[
 R_{j,N}(a,b)=X^{-j}
  \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{(r_N;r_N)_j^{2+\epsilon}},
 \quad r_N=e^{-2\pi i/N},\quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
\tag{27}
\]
**Theorem 2.** For every \(\tau>0\), both level parities satisfy
\[
 \begin{split}
 &|U_{\alpha,N}(w,X)|\,|d_N(X)|^\alpha |d_N(Y)|^{\epsilon/2}
 \sum_{j=\lceil N/2\rceil}^{\lfloor N(1-z)\rfloor}
                                      |R_{j,N}(a,b)|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                 \exp N\{\Gamma(z)-\gamma_*+\tau\}.
 \end{split}
\tag{28}
\]
The estimate holds on a sufficiently small fixed ordinary-color
neighborhood of \(w=-2\), and for every fixed derivative of the cap
in that color on a smaller neighborhood. It imposes no sign
restriction on the original private critical height of the
ordinary neighbor.

To prove (28), use the original zero-safe finite-product estimate
on every row in (27), including rounded endpoints and possible
zeros. It supplies the continuous allocated rate in (6), with
an arbitrarily small tolerance and a polynomial prefactor.
Multiplication by the complete cap envelope and maximization give
the rate just proved. There are at most \(N\) rows.
The original unselected Fourier estimates have precisely the
allocations in (6), because every type-four target retains its
actual negative height. No finite Fourier factor is divided out.

The cap source bounds hold uniformly on the entire real
ordinary-color interval. Its favorable angular loss may be
discarded in this upper bound; the separate true-end profile
already has a uniform bound there. The degree is less than \(N\).
Interval polynomial continuation therefore supplies a fixed
ordinary-color neighborhood at an arbitrarily small additional
exponential cost. Cauchy's formula gives every fixed ordinary
derivative on a smaller neighborhood. These costs can be chosen
inside the reserve between \(2\gamma_*\) and \(\gamma_*\), or
inside the displayed tolerance. The whole cap, both parities and
every physical row in (28) are retained.

## 6. The remaining wrapped strip

No statement that every high maximum satisfies (13) is made.
In the wrapped strip
\[
                         1-z<s<1-x
\tag{29}
\]
put \(q=-\cot\pi s\), \(A=\cot\pi a\), \(B=\cot\pi b\).
The exact exponentiated row derivative from the original high-tail
source is
\[
 P_\epsilon(q)=
 4^{-\epsilon}e^{2\pi(d-c)}
 |\sin\pi a\,\sin\pi b|^2
 |q-A|^2|q-B|^2(1+q^2)^\epsilon.
\tag{30}
\]
A stationary local maximum must satisfy
\[
                     P_\epsilon(q)=1,\qquad
                     P_\epsilon'(q)\le0.
\tag{31}
\]
These are the descending level-one crossings of the actual quartic
or sextic. They have not been excluded or paid here. The original
reflection theorem pays all rows \(s\ge1-x\) by the true last-row
rate, but its separate calibrated joint comparison must still be
retained. No full high-tail, whole boundary, signed lower-bound,
or finite-exception conclusion follows from (19).

## Direct source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_cyclic_critical_height_bounds.md | 39dff66057a82bc974aa38d65e39a13f508024440bd4e3936783c1c37fe290a9 |
| research_mixed_open_local_factor_coverage.md | b0fdc0b9b968c29469b86f5d29f9bc86b1dd535f762ac1386f96bd3514e3659a |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_first_attached_high_tail_seam.md | c21393b49f6c1aaf0de1a01ef232bb4bcd1e78b5f9d48e691ddb01aa72490bec |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

All directly used proofs and domains were read. No mathematical
numerical evaluation, saved-value arithmetic, source replay, import,
test or compilation was performed. Frozen sources were unchanged.
