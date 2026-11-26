# The crossing kernel after exact leaf contraction

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

A signed crossing leaf can be contracted exactly before the remaining
boundary packets are assembled. For the positive crossing, the resulting
two-boundary source is an explicit canonical Gamma quotient plus a
uniformly bounded current. Its leading action is that of an ideal
tetrahedron, with a specified imaginary quadratic phase.

The estimate holds on the full strict tetrahedron-angle region, with
independent moduli including zero and one. Relative nonvanishing is
asserted where the displayed height is nonnegative. Every strict
tetrahedron also has an explicit growing path from the origin to its
unit boundary. The inverse crossing retains an exact reciprocal and
coefficient-conjugate formula; it is not obtained by changing only a
phase in the same disk chart.

## 1. The actual two-boundary source

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad D_N(t)=1-\eta t^N.
 \tag{1}
\]
All powers use these exponentials. The original centered basis of the
full Newton boundary algebra satisfies
\[
 \phi(f_af_b)=\delta_{ab},\quad
 R^+=\sqrt N f_0,\quad R^-=\sqrt N f_d,\quad
 \mathcal C_N(x,y,z)=\sum_{a,b,c=0}^d
                         \phi(f_af_bf_c)x^ay^bz^c .
 \tag{2}
\]
Here \(\phi\) is the original Frobenius closing; the complete
algebra, including its first derivatives at double Casimir roots,
is retained. Define
\[
 A_N^+(y,z)=\mathcal C_N(0,y,z),\qquad
 \mathcal K_N^+(y,z)=\sqrt N\,A_N^+(y,z).
 \tag{3}
\]
Thus \(\mathcal K_N^+\) is the actual multiplication kernel of
\(R^+\) in the centered coordinates. If \(v=\sum_bv_bf_b\),
the \(f_c\) coefficient of \(R^+v\) is
\(\sum_b\sqrt N C_{0bc}v_b\), without conjugating \(v_b\).
This is an exact leaf contraction before any subsequent closing.

Take the strict tetrahedron angles
\[
                    b>0,\quad c>0,\quad b+c<1
 \tag{4}
\]
and put
\[
 y=-r_y e^{-2\pi ib},\quad z=-r_z e^{-2\pi ic},
                         \qquad 0\le r_y,r_z\le1.
 \tag{5}
\]
For positive moduli set \(\ell_j=-\log r_j/(2\pi)\) and
\[
 \alpha=N(1-b)-\tfrac12+iN\ell_y,\quad
 \beta=N(1-c)-\tfrac12+iN\ell_z,\quad
 \gamma=N(1-b-c)+iN(\ell_y+\ell_z).
 \tag{6}
\]
These obey \(\alpha+\beta-\gamma=d\). Let \(F_N\) be the
canonically normalized complex factorial from the full prism theorem,
with
\[
 F_N(0)=1,\quad F_N(w+1)=(1-Q^{w+1})F_N(w),\quad
 F_N(w+N)=(1-e^{2\pi iw})F_N(w).
 \tag{7}
\]
Its definition is the original convergent Gamma product with its
displayed quadratic phase, not an arbitrary periodic solution.
The nonzero quotient
\[
                 G_N^+(y,z)=
                  \frac{\kappa F_N(\alpha)F_N(\beta)}
                                  {\sqrt N F_N(\gamma)}
 \tag{8}
\]
has continuous nonzero limits when either modulus is zero. Indeed
the canonical \(F_N\) has the same nonzero upper-half-plane limit
for every fixed real offset. The affected factors in (8) therefore
have well-defined canceling limits. For example, as \(r_y\to0\),
the quotient \(F_N(\alpha)/F_N(\gamma)\) tends to one.

Use the disk branches
\[
 \Psi_0(y,z)=-\frac{\pi}{12}
       +\frac{\operatorname{Li}_2(-y)+\operatorname{Li}_2(-z)
                              -\operatorname{Li}_2(yz)}{2\pi},
 \qquad B_0(y,z)=(1-yz)^{-1/2}.
 \tag{9}
\]
Their boundary values in (5) are regular on (4).

**Theorem.** On every compact subset of (4), uniformly for all
\((r_y,r_z)\in[0,1]^2\), there is an explicitly prescribed current
\(J_N^+(y,z)\) such that
\[
 \boxed{\quad
 A_N^+(y,z)=G_N^+(y,z)
                  -\frac{\kappa}{N}D_N(y)D_N(z)J_N^+(y,z),
                 \qquad |J_N^+|\le C .
 \quad}
 \tag{10}
\]
The identity is exact for sufficiently large \(N\), and includes
both parities. The geometric quotient obeys
\[
 G_N^+=\kappa e^{\,i\pi/4-\pi i/(4N)}
              B_0e^{iN\Psi_0}(1+O(N^{-1})).
 \tag{11}
\]
Consequently \(A_N^+\) has the nonzero relative asymptotic (11)
wherever \(-\operatorname{Im}\Psi_0\ge0\). The asymptotic for
the actual crossing kernel \(\mathcal K_N^+\) is obtained by
multiplying that expression by \(\sqrt N\). The estimates
are uniform there.
No positive height is asserted for all independent moduli in
the one-large-angle part of (4).

## 2. The full source contour at the endpoint

We give the endpoint proof, including the change to the lower
current when one angle exceeds \(1/2\).
With the shifts (6), define
\[
 W_N(s)=
 \frac{F_N(s)F_N(s+\gamma)F_N(\alpha)F_N(\beta)}
      {F_N(\gamma)F_N(s+1+\alpha)F_N(s+1+\beta)}.
 \tag{12}
\]
The original wall and Cauchy formulas, at \(x=0\), give
\[
 A_N^+(y,z)=
     \frac{\kappa}{N^{3/2}}D_N(y)D_N(z)
                                   \sum_{j=0}^{N-1}W_N(j).
 \tag{13}
\]
In particular the two \(+1\)'s in (12) are retained.

First assume the moduli are positive and strictly less than one.
For \(t=e^{2\pi is}\), use the same source-preserving differential
as in the full prism theorem, now without its Cauchy factor:
\[
 \Omega_N(s)=
 2\pi i\,\frac{(1-\eta y^Nt)(1-\eta z^Nt)}
                {D_N(y)D_N(z)(t-1)}W_N(s)\,ds.
 \tag{14}
\]
The rectangle has vertical sides \(\operatorname{Re}s=-1/2\)
and \(N-1/2\). Its integer residues are precisely \(W_N(j)\).
All shifted denominator zeros in this window lie in the first
simple-zero block of \(F_N\); the two numerator factors in (14)
cancel them exactly, including coincident families. The numerator
factorials have no poles in this window. These statements use
only (4), not \(b,c<1/2\).

The lower horizontal side vanishes, by the balanced canonical
asymptotic from the full prism theorem. The upper side now
contributes, rather than vanishing:
\[
              W_N(s)\longrightarrow
                      \frac{F_N(\alpha)F_N(\beta)}{F_N(\gamma)}
                  \qquad(\operatorname{Im}s\to+\infty).
 \tag{15}
\]
Its orientation is from right to left, and the coefficient
in (14) tends to \(-2\pi i/(D_N(y)D_N(z))\).
Thus its integral divided by \(2\pi i\) is
\(N F_N(\alpha)F_N(\beta)/(D_N(y)D_N(z)F_N(\gamma))\).
This is the finite source of the term (8); no coefficient is
assigned by continuity of a saddle formula.

The exact vertical-side difference is still
\[
 \Omega_N(s+N)-\Omega_N(s)
            =-2\pi i\,\frac{t}{t-1}W_N(s)\,ds .
 \tag{16}
\]
The residue theorem proves (10) with
\[
 J_N^+(y,z)=\frac1{\sqrt N}
   \int_{-1/2-i\infty}^{-1/2+i\infty}
                     \frac{e^{2\pi is}}{e^{2\pi is}-1}W_N(s)\,ds .
 \tag{17}
\]
It remains to prove convergence and its uniform bound on the
whole tetrahedron domain.

## 3. Both halves of the same canonical current

Use the full-vertical-strip estimates proved in the prism transport.
They remain uniform when the imaginary shifts in (6) are
arbitrarily large. Put
\[
 f(w)=L(w)+\frac{i\pi}{2}(w^2-w),\qquad
 h(w)=\sqrt{2\sin\pi w}\,e^{i\pi w/2},
 \quad L'(w)=\log(2\sin\pi w),\quad L(0)=0 .
 \tag{18}
\]
The analytic branches are those on \(0<\operatorname{Re}w<1\).
In particular \(f'(w)=\operatorname{Log}(1-e^{2\pi iw})\)
and \(h(w)^2=i(1-e^{2\pi iw})\).
At \(s=-1/2+iNY\), the exact endpoint factor has modulus
\[
                         |F_N(s)|^2
                              =\frac{N}{1+e^{-2\pi NY}}.
 \tag{19}
\]
More explicitly, set
\[
 \begin{gathered}
 U_Y=1-b+i(Y+\ell_y),\quad V_Y=1-c+i(Y+\ell_z),\\
 Z_Y=1-b-c+i(Y+\ell_y+\ell_z),\\
 Q_0(Y)=f(Z_Y)-f(U_Y)-f(V_Y)+f(U_0)+f(V_0)-f(Z_0),\\
                         R(Y)=\Re Q_0(Y)+\pi\min(Y,0).
 \end{gathered}
\]
Applying the complete-strip expansion to the six shifted factors
in (12) gives
\[
                      |W_N(s)|/\sqrt N
                                      \le C e^{N R(Y)},
                         \qquad R(0)=0,
 \tag{20}
\]
where the derivative of its explicit real rate is
\[
 \begin{aligned}
 T(Y)={}&\arg(1-v_y e^{-2\pi ib})
          +\arg(1-v_z e^{-2\pi ic})
          -\arg(1-v_0 e^{-2\pi i(b+c)}),\\
 R'(Y)&=T(Y)\ (Y>0),\qquad
 R'(Y)=\pi+T(Y)\ (Y<0),\\
 v_y&=r_y e^{-2\pi Y},\quad
 v_z=r_z e^{-2\pi Y},\quad
 v_0=r_yr_z e^{-2\pi Y}.
 \end{aligned}
 \tag{21}
\]
The rate and its normalization are obtained by differentiating
the same shifted \(f\)-combination as in the full prism theorem.
The arguments are its original-strip arguments.
The amplitude bound in (20) holds for all real \(Y\):
for an angle in a compact subset of \((0,1)\),
\(|1-v e^{-2\pi i b}|\) has a positive lower bound for every
\(v\ge0\). Likewise the factor at \(b+c\) stays away from zero
for \(0\le r_yr_z\le1\).

For \(Y>0\), all three radii in (21) are below one, so
\[
                              T(Y)<3\pi/2 .
 \tag{22}
\]
For \(Y<0\), if \(b,c\le1/2\), the two-small-angle proof from
the full prism theorem gives \(T(Y)>0\), including a possible
equality of one angle with \(1/2\) by its direct argument signs.
If \(b>1/2\), then \(c<1/2\) and \(b+c>1/2\).
The first argument in (21) lies between \(\pi-2\pi b\)
and zero; the second is positive and the third is negative.
Therefore
\[
                     \pi+T(Y)>2\pi(1-b)>0.
 \tag{23}
\]
The case \(c>1/2\) is symmetric.
On a compact subset of (4), there is consequently a fixed
\(\epsilon>0\) such that
\[
 R(Y)\le 3\pi Y/2\quad(Y\ge0),\qquad
 R(Y)\le\epsilon Y\quad(Y\le0).
 \tag{24}
\]

Finally, on the half-step line,
\[
 \left|\frac{t}{t-1}\right|
      =\frac1{1+e^{2\pi NY}}
      \le e^{-2\pi NY}\ (Y\ge0),\qquad \le1\ (Y\le0).
 \tag{25}
\]
Since \(ds=iN\,dY\), equations (17), (20), and (24)--(25)
prove \(|J_N^+|\le C\).
All constants are uniform for \(0<r_y,r_z\le1\).
At unit moduli the final canceled identity extends by dominated
convergence, without defining (14) at a norm-wall collision.
At zero moduli the canonical upper limits give the pointwise
limits of (8), (12), and (17); the same current majorant
again applies. This proves the exact identity on the entire
closed square of moduli.

For (11), apply the half-shift expansion to \(F_N(\alpha)\)
and \(F_N(\beta)\), and the zero-shift expansion to
\(F_N(\gamma)\). Their clocks are \(-y,-z,yz\), respectively.
The \(f\)-combination is exactly \(i\Psi_0\); the amplitude is
\(\kappa e^{i\pi/4-\pi i/(4N)}(1-yz)^{-1/2}\).
The uniform vertical estimates also cover the limits where
a modulus is zero. Equations (10)--(11) now prove the
relative and nonvanishing statements where the height is
nonnegative.

## 4. Tetrahedron geometry and explicit growing paths

For unit moduli let
\[
                  T(b,c)=L(b+c)-L(b)-L(c).
 \tag{26}
\]
The unit-circle dilogarithm formulas give the full marked action
\[
             \boxed{\quad i\Psi_0(y,z)=T(b,c)-i\pi bc.\quad}
 \tag{27}
\]
The ideal tetrahedron with dihedral angles
\(\pi b,\pi c,\pi(1-b-c)\) has volume \(\pi T(b,c)\).
This is the usual Lobachevsky volume formula; see
[Milnor in Thurston's notes, Theorem 7.2.1](https://library.slmath.org/nonmsri/gt3m/PDF/Thurston-gt3m.pdf).
Here \(\Lambda(\pi u)=-\pi L(u)\), which fixes the sign
and the factor of \(\pi\).

The exact logarithmic momenta at this boundary are
\[
 \begin{aligned}
 \partial_b(i\Psi_0)&=
        \log\frac{\sin\pi(b+c)}{\sin\pi b}-i\pi c,\\
 \partial_c(i\Psi_0)&=
        \log\frac{\sin\pi(b+c)}{\sin\pi c}-i\pi b .
 \end{aligned}
 \tag{28}
\]
Its real Hessian, meaning the Hessian of the real action \(T\)
in these two real angle coordinates, is
\[
 H_T=\pi
 \begin{pmatrix}
 \cot\pi(b+c)-\cot\pi b&\cot\pi(b+c)\\
 \cot\pi(b+c)&\cot\pi(b+c)-\cot\pi c
 \end{pmatrix},\qquad \det H_T=\pi^2 .
 \tag{29}
\]
Both diagonal entries are negative. The identity
\(\cot\pi(b+c)(\cot\pi b+\cot\pi c)=
\cot\pi b\cot\pi c-1\) proves the determinant and negative
definiteness. Writing \(a=\cot\pi(b+c)\),
\(b_0=\cot\pi b,c_0=\cot\pi c\), its inverse is explicitly
\[
                   H_T^{-1}=\frac1\pi
                       \begin{pmatrix}a-c_0&-a\\-a&a-b_0\end{pmatrix}.
 \tag{30}
\]
Thus the real angle action is uniformly strictly concave on
every strict tetrahedron compact. The full phase additionally
retains its term \(-i\pi bc\). This two-dimensional Hessian
is not a bound for the full \(N\)-dimensional packet response.
There is also a normalization check for the crossing kernel.
If \(\Phi=T-i\pi bc\), then
\[
 \Phi_{bc}=\pi\cot\pi(b+c)-i\pi,\qquad
 |B_0|^2=\frac1{2\sin\pi(b+c)}
                          =\frac{|\Phi_{bc}|}{2\pi}.
 \tag{30a}
\]
Consequently the actual leading amplitude \(\sqrt N B_0\)
has the mixed-Hessian half-density magnitude
\(\sqrt{N|\Phi_{bc}|/(2\pi)}\). This scalar identity
asserts neither global unitarity nor control of packet tails.

There are also explicit growing paths. Set
\[
 F_r(u)=-\operatorname{Im}\operatorname{Li}_2
                              (r e^{-2\pi iu}) .
 \tag{31}
\]
For \(0<u<1/2\), this function is positive, strictly concave
in \(u\), increasing in \(r\), and convex in \(\log r\).
These statements follow by differentiation:
\[
 \partial_u^2F_r=
 -\frac{4\pi^2r\sin2\pi u}{1-2r\cos2\pi u+r^2}<0,\quad
 \partial_{\log r}F_r=\arg(1-r e^{-2\pi iu})>0,\quad
 \partial_{\log r}^2F_r=
 \frac{r\sin2\pi u}{1-2r\cos2\pi u+r^2}>0.
 \tag{32}
\]
It vanishes at \(u=0,1/2\) and satisfies
\(F_r(1-u)=-F_r(u)\).
The height is
\[
 -2\pi\operatorname{Im}\Psi_0
                 =F_{r_y}(b)+F_{r_z}(c)-F_{r_yr_z}(b+c).
 \tag{33}
\]
When \(b,c\le1/2\) and both radii are positive, it is strictly
positive for arbitrary independent radii. If \(b+c\ge1/2\),
the last term has the favorable sign. Otherwise strict
subadditivity from angle concavity, and radial monotonicity,
give
\[
 F_{r_yr_z}(b+c)<
       F_{r_yr_z}(b)+F_{r_yr_z}(c)
                         \le F_{r_y}(b)+F_{r_z}(c).
 \tag{34}
\]

For every strict pair (4), a single growing path is
\[
                         r_y=r^b,\quad r_z=r^c,\qquad 0<r\le1.
 \tag{35}
\]
For two small angles this follows from the arbitrary-modulus
positivity already proved. If \(b=1-\delta>1/2\), then
\(0<c<\delta<1/2\). Put \(R=r^c\),
\(k=b/c>\delta/c\), and \(\alpha=c/\delta\).
The height on (35) is
\(-F_{R^k}(\delta)+F_R(c)+F_{R^{k+1}}(\delta-c)\).
Strict angle concavity bounds the last two terms below
\[
       \alpha F_R(\delta)+(1-\alpha)F_{R^{k+1}}(\delta).
 \]
Log-radius convexity bounds this expression below
\(F_{R^m}(\delta)\), where
\(m=\alpha+(1-\alpha)(k+1)=k+1-\alpha k\le k\).
Since \(0<R\le1\), radial monotonicity gives
\(F_{R^m}(\delta)\ge F_{R^k}(\delta)\).
The strict angle inequality proves positive height.
Interchanging the two legs handles \(c>1/2\).
Thus (35) supplies a growing origin-to-unit-boundary path
throughout the strict tetrahedron region. This is a local
construction; compatibility with the angle orientations and
cycles of a whole Conway assembly is not asserted.

## 5. The inverse crossing and the original attachments

Define the inverse kernel by its actual coefficients,
\[
 \mathcal K_N^-(y,z)
                   =\sqrt N\sum_{j,k=0}^d C_{djk}y^jz^k.
 \tag{36}
\]
Let coefficient conjugation be denoted by \(\sharp\).
The centered compiler gives exactly
\[
 \boxed{\quad
 \mathcal K_N^-(y,z)
       =(yz)^d(\mathcal K_N^+)^\sharp(1/y,1/z).
 \quad}
 \tag{37}
\]
This is a polynomial identity, with its removable interpretation
at zero arguments. It follows from
\(\overline{C_{abc}}=C_{d-a,d-b,d-c}\).
Thus the positive-kernel estimates also give the inverse kernel
in the corresponding reciprocal and conjugate chart, with the
displayed monomial retained. They do not give an inverse-kernel
estimate in the same disk chart by simply conjugating \(y,z\).

Both kernels are actual multiplication operators on the complete
boundary space, and their coefficient matrices are inverses.
Contracting either signed leaf first therefore preserves every
subsequent original turn and closing functional, and every
Casimir normal. No Hermitian adjoint or positive replacement
for the bilinear gluing has been inserted.

The theorem supplies the source-sensitive two-boundary block
needed after this contraction. It does not identify a full
Conway geometric critical point, a common contour for all
attachments, or a nonzero coefficient of the assembled period.
The tetrahedron Hessian and local growing paths alone do not
solve those remaining gluing questions.

## Complete proof sources

Both complete proof texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Full initialized prism source transport](research_centered_tensor_full_prism_source_transport.md) | eb43e287eca5933b70de3b6362a81f92d46bb2e121f0eb5716793c107adaef10 |
| [Centered full source compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

The standard tetrahedron volume interpretation is cited above.
The source-specific additions are the exact top-side endpoint
term, the full tetrahedron current bound, the initialized crossing
kernel and its explicit growing paths. No novelty is claimed
for Gamma limits, concavity, or the Lobachevsky volume formula.

Only written mathematics, text/hash operations and the stated
primary-source lookup were used. No mathematical program,
numerical experiment, test, build, git operation or earlier-final
edit was performed.
