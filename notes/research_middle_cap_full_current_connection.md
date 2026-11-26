# The complete marked cap as a rational quantum connection

21 November 2026. Research note. Earlier final notes and the public
manuscripts remain unchanged.

The marked cap has a full-function description retaining every
fixed-root clock current. After the actual middle Euler change of
coordinates, its resolvent is a reciprocal finite Pochhammer product.
The literal cap is its value at zero; the original Conway root
closing is a specified residue. The complete current family
is an explicit finite Fourier transform of the physical boundary
vector. The physical clock and shift act by scalar quantum-difference
operators with a specified point source.

The reciprocal product also equals a ratio of the already fixed
literature cyclic dilogarithm, including its central norm factor.
It has a uniform nonzero asymptotic on every fixed disk inside the
unit circle, at all boundary indices, including both endpoints.
This estimates an actual boundary kernel. It does not select the
geometric contribution of an arbitrary short component.

## 1. The original cap and all of its clock currents

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\[
 x=-q^{-1},\qquad
 F_a=(Q;Q)_a=\prod_{h=1}^a(1-Q^h),\qquad
 \nu_a=(-1)^aQ^{a(a+1)/2}.
 \tag{1}
\]
Empty products equal one. All physical indices lie between zero
and \(d\). Write
\[
 v_a=|a,d-a\rangle,\qquad Zv_a=Q^av_a,\qquad
 {r\brack a}_Q=\frac{F_r}{F_aF_{r-a}}\quad(0\le a\le r\le d).
\]
The actual middle cyclic-column matrix and literal marked cap are
\[
 C_{ar}=\nu_a(-q)^{r-a}{r\brack a}_Q\quad(a\le r),
 \qquad C_{ar}=0\quad(a>r),\qquad
 m(v_a)=x^{d-a}/N^2.
 \tag{2}
\]
These have the original source conventions of the Euler theorem.
In particular
\[
 \mu_r:=(mC)_r=\frac{x^d(-q)^rF_r}{N^2}\ne0.
 \tag{3}
\]
For \(0\le j<N\), define
\[
                         g_{j,r}=\frac{(mZ^jC)_r}{\mu_r}.
\]
The finite binomial theorem gives every fixed-root current:
\[
 \boxed{\quad
 g_{j,r}=\frac{(Q^{j+1};Q)_r}{F_r},\qquad
 F_jg_{j,r}=(Q^{r+1};Q)_j.
 \quad}
 \tag{4}
\]
Indeed the unnormalized numerator is
\[
 \frac{x^d(-q)^r}{N^2}
 \sum_{a=0}^r(-1)^aQ^{a(a-1)/2}(Q^{j+1})^a
                  {r\brack a}_Q
 =\frac{x^d(-q)^r}{N^2}(Q^{j+1};Q)_r.
\]
For \(r+j<N\), canceling factorials proves the second equality.
For \(r+j\ge N\), both products contain \(1-Q^N=0\), so it
remains true. Consequently
\[
                g_{0,r}=1,\qquad |F_jg_{j,r}|\le2^j.
 \tag{5}
\]
This retains all physical currents at the given level, rather than
a fixed finite jet.

## 2. The exact resolvent and its central factor

For \(t^N\ne1\), form the actual row
\[
                   m_t=m(I-tZ)^{-1},\qquad m_0=m.
 \tag{6}
\]
Since \(Z^N=I\),
\[
             (I-tZ)^{-1}=
                 \frac{\sum_{j=0}^{d}t^jZ^j}{1-t^N}.
 \tag{7}
\]
Thus all currents belong to one pointed rational function.

**Theorem 1.** The normalized cap resolvent is
\[
 \boxed{\quad
 \mathcal R_r(t):=\frac{(m_tC)_r}{\mu_r}
     =\frac1{(t;Q)_{r+1}},\qquad
 \sum_{j=0}^{d}g_{j,r}t^j
     =\frac{1-t^N}{(t;Q)_{r+1}}
     =\prod_{k=r+1}^{d}(1-tQ^k).
 \quad}
 \tag{8}
\]

**Proof.** Substitution of (2) gives
\[
 \mathcal R_r(t)=
    \sum_{a=0}^r
       \frac{\nu_a}{F_aF_{r-a}}\frac1{1-tQ^a}.
 \tag{9}
\]
This is the partial-fraction expansion of the reciprocal product:
its coefficient at \(t=Q^{-a}\) is
\[
 \prod_{\substack{0\le k\le r\\k\ne a}}(1-Q^{k-a})^{-1}
   =\frac{(-1)^aQ^{a(a+1)/2}}{F_aF_{r-a}}
   =\frac{\nu_a}{F_aF_{r-a}}.
\]
Both functions vanish at infinity. Matching their simple poles proves
the rational identity; (7) then proves the polynomial identity.
\(\square\)

In particular
\[
 \mathcal R_r(0)=1,\qquad
 \mathcal R_0(t)=\frac1{1-t},\qquad
 \mathcal R_d(t)=\frac1{1-t^N}.
 \tag{10}
\]
The last factor is part of the source. Useful exact ratios are
\[
 \frac{\mathcal R_r(Qt)}{\mathcal R_r(t)}
      =\frac{1-t}{1-tQ^{r+1}},\qquad
 \frac{\mathcal R_r(t/Q)}{\mathcal R_r(t)}
      =\frac{1-tQ^r}{1-t/Q},
 \tag{11}
\]
\[
 \mathcal R_{r+1}(t)=
    \frac{\mathcal R_r(t)}{1-tQ^{r+1}}\quad(r<d),\qquad
 \prod_{j=0}^{d}\mathcal R_r(Q^jt)=(1-t^N)^{-(r+1)}.
 \tag{12}
\]
The cap kernel is not a norm-one cyclic function by itself.

## 3. A complete scalar model and its marked evaluation

For an arbitrary physical middle vector \(w\), set
\[
 (\mathcal B_Nw)(t)=m_t w
      =\frac{p_w(t)}{1-t^N},\qquad
 p_w(t)=\sum_{j=0}^{d}b_j(w)t^j,\qquad b_j(w)=mZ^jw.
 \tag{13}
\]
This is an isomorphism onto
\[
              \mathcal V_N=
       \{p(t)/(1-t^N):p\in\mathbb C[t],\ \deg p<N\}.
\]
Indeed
\[
                 \mathcal B_Nw=
             \sum_{a=0}^{d}\frac{m(v_a)w_a}{1-tQ^a}.
\]
The poles are distinct and every weight is nonzero, so vanishing
forces \(w=0\). The two spaces have dimension \(N\).
Fourier orthogonality also gives the exact norm identity
\[
 \boxed{\quad
        \sum_{j=0}^{d}|b_j(w)|^2
                       =N^{-3}\sum_{a=0}^{d}|w_a|^2.
 \quad}
 \tag{14}
\]
To prove it, expand \(b_j=\sum_a m(v_a)w_aQ^{aj}\), sum
\(Q^{j(a-b)}\) over a complete period, and use
\(|m(v_a)|=N^{-2}\).

The original cyclic face unit obeys
\[
 XZ=QZX,\quad X^N=I,\quad
 Xv_a=xv_{a-1}\ (a\ge1),\quad Xv_0=x^{N+1}v_d.
\]
The actual mark satisfies \(mX=Q^{-1}m\): the interior and cyclic
arrows both give the ratio \(x^2=Q^{-1}\). Therefore
\[
 \boxed{\quad
 m_tX=Q^{-1}m_{t/Q},\qquad
 m_tZ=\frac{m_t-m_0}{t}.
 \quad}
 \tag{15}
\]
At zero the quotient has its removable value. The scalar operators
corresponding to the actual \(X,Z\) are thus
\[
 (\mathcal D_Xf)(t)=Q^{-1}f(t/Q),\qquad
 (\mathcal D_Zf)(t)=\frac{f(t)-f(0)}t,
 \qquad
 \mathcal B_N(Xw)=\mathcal D_X\mathcal B_Nw,\quad
 \mathcal B_N(Zw)=\mathcal D_Z\mathcal B_Nw.
 \tag{16}
\]
The original marked source is precisely
\[
                            (\mathcal B_Nw)(0)=mw.
 \tag{17}
\]
On numerator coefficients, \(\mathcal D_Xp=Q^{-1}p(t/Q)\), while
\[
 \mathcal D_Z:\sum_{j=0}^{d}b_jt^j\longmapsto
               \sum_{j=0}^{d-1}b_{j+1}t^j+b_0t^d.
 \tag{18}
\]
The last term is the evaluation term together with the retained
denominator. Consequently, on the entire space,
\[
             \mathcal D_X\mathcal D_Z
                   =Q\mathcal D_Z\mathcal D_X,\qquad
             \mathcal D_X^N=\mathcal D_Z^N=I.
 \tag{19}
\]
The point source has not been replaced by an unpointed shift.

The literal strict Euler argument is \(n=(Q-Z^{-1})X\).
If \(b_d=[t^d]p\), inverse cyclic shift in (18) gives
\[
                  \mathcal D_Z^{-1}f=tf+b_d.
\]
Consequently its actual scalar operator is
\[
 \boxed{\quad
    (\mathcal D_nf)(t)=(1-t/Q)f(t/Q)-b_d.
 \quad}
 \tag{19a}
\]
For the basis in (8), its full endpoint rule is
\[
 \mathcal D_n\mathcal R_r=\mathcal R_{r-1}\quad(r\ge1),
 \qquad \mathcal D_n\mathcal R_0=0.
 \tag{19b}
\]
Indeed the first term of (19a) is
\((1-tQ^r)\mathcal R_r\). For \(r\ge1\) the numerator has
degree below \(d\), while for \(r=0\) its degree-\(d\)
coefficient is one; precisely this last subtraction kills the
bottom arrow. In particular \(\mathcal D_n^N=0\).
Define \(P_Q(B)=\sum_{h=0}^{d}(-1)^hQ^{h(h-1)/2}B^h/F_h\).
This finite Euler operator has the exact Cauchy form
\[
 P_Q(\mathcal D_n)\mathcal R_r
           =\frac{\nu_r}{F_r(1-tQ^r)}.
 \tag{19c}
\]
To prove it without discarding an endpoint, use
\(P_Q(n)C e_r=D_\nu e_r=\nu_re_r\) from the Euler theorem
and apply \(\mathcal B_N\), with \(e_r\) a standard coordinate
column. The left side becomes
\(\mu_rP_Q(\mathcal D_n)\mathcal R_r\); the right side is
\(\nu_rm(v_r)/(1-tQ^r)\), and their coefficient ratio is
\(\nu_r/F_r\).

## 4. The face clock, cup and correct boundary orthogonality

For the actual middle clock
\[
                          \mathcal H=Z+(I-QZ)X,\qquad
                          \mathcal HC=CZ,
\]
substitution in (16) gives
\[
 \boxed{\quad
 (\mathcal D_{\mathcal H}f)(t)
       =\frac{f(t)-f(t/Q)}t+Q^{-1}f(t/Q).
 \quad}
 \tag{20}
\]
The two evaluation terms cancel in this combination; neither has
been dropped separately. Since \(1-(t/Q)^N=1-t^N\), the same
displayed expression acts on numerators. The basis functions satisfy
\[
 \mathcal D_{\mathcal H}\mathcal R_r=Q^r\mathcal R_r,\qquad
 p_r(t)=\prod_{k=r+1}^{d}(1-tQ^k),\qquad p_r(0)=1.
 \tag{21}
\]
This follows from \(\mathcal HC=CZ\), or from the second ratio in
(11). The numerator degrees \(d-r\) also prove that they form a
basis.

The literal cup is \(p=N\sum_a x^{a-d}v_a\). Since every
\(m(v_a)p_a=1/N\),
\[
 \boxed{\quad
                    \mathcal B_Np=\frac1{1-t^N},\qquad
                    (\mathcal B_Np)(0)=mp=1.
 \quad}
 \tag{22}
\]
All source and cyclic factors are retained. For a specified physical
operator \(W\), its original literal contraction is exactly
\[
                            mWp=(\mathcal B_NWp)(0).
 \tag{23}
\]
The Conway packet marked-cap and Frobenius rows are distinct typed
functionals. They have equally explicit, different realizations here.
Inverse finite Fourier transform in (13) is
\[
               w_a=Nx^{a-d}\sum_{j=0}^{d}b_jQ^{-aj}.
\]
The packet rows are \(m_{\rm pkt}(w)=\sum_a x^aw_a\) and
\(\phi_{\rm pkt}(w)=w_d\). Since \(x^2=Q^{-1}\), this gives
\[
 \boxed{\begin{aligned}
 mw&=b_0=(\mathcal B_Nw)(0),\\
 m_{\rm pkt}(w)&=N^2x^{-d}[t^d]p_w(t),\\
 \phi_{\rm pkt}(w)&=Np_w(Q)
          =-N^2Q^{-1}\operatorname{Res}_{t=Q}
                                      \mathcal B_Nw(t).
 \end{aligned}}
 \tag{23a}
\]
The residue identity follows from
\((1-t^N)'|_{t=Q}=-NQ^{-1}\). Thus for a full Conway
packet with original Frobenius root closing, the original scalar
is precisely the last residue in (23a), with its unchanged external
framing and peripheral line. Only \(r=d\) among the basis functions
\(\mu_r\mathcal R_r\) has a pole at \(Q\), and its residue is
\(-Q/N^2\). The protected root functional therefore extracts exactly
the original last Newton coefficient. No literal cap has replaced it.

There are two explicit positive norms on this function model, with
different meanings. Equation (14) transports the flat physical norm.
To transport the correct Newton boundary Gram
\(G=(C^{-1})^*C^{-1}\), define instead
\[
 \langle\mathcal B_Ny,\mathcal B_Nz\rangle_{\mathscr G}
                                      =\langle y,z\rangle_G.
\]
Then
\[
 e_r(t):=\mu_r\mathcal R_r(t),\qquad
                     \mathcal B_N(C\alpha)=\sum_r\alpha_re_r
\]
is an orthonormal basis in \(\mathscr G\). Its positive reproducing
kernel is exactly
\[
 K_{\mathscr G}(t,s)=
       \sum_{r=0}^{d}
       \frac{|\mu_r|^2}
       {(t;Q)_{r+1}\overline{(s;Q)_{r+1}}}.
 \tag{24}
\]
In particular evaluation at the original point has squared dual norm
\[
                         K_{\mathscr G}(0,0)
                            =N^{-4}\sum_{r=0}^{d}|F_r|^2.
 \tag{25}
\]
This is precisely the previously retained literal-cap cost.
Full-function orthogonality has not removed it. Both transforms are
invertible on all \(N\) coordinates, so they retain every Casimir
Hermite direction; the simple spectrum in (21) is a face-clock
spectrum, not a semisimplification of the Casimir.

## 5. The fixed literature cyclic function

Use the cyclic function already fixed in the original Hardy network:
\[
 \mathfrak V_N(t)=
 (1-t^N)^{(N-1)/(2N)}
       \prod_{\ell=1}^{d}(1-Q^\ell t)^{-\ell/N}.
 \tag{26}
\]
All powers are holomorphic branches equal to one at zero. On
\(|t|<1\), its exact logarithm is
\[
 \log\mathfrak V_N(t)=
       \sum_{\substack{m\ge1\\N\nmid m}}
                     \frac{t^m}{m(Q^m-1)}.
\]
Subtracting the logarithms at \(Qt\) and \(t\) gives
\[
 \frac{\mathfrak V_N(Qt)}{\mathfrak V_N(t)}
                      =\frac{(1-t^N)^{1/N}}{1-t}.
\]
Iteration proves the actual full-function identity
\[
 \boxed{\quad
 \mathcal R_r(t)=
 (1-t^N)^{-(r+1)/N}
       \frac{\mathfrak V_N(Q^{r+1}t)}{\mathfrak V_N(t)}.
 \quad}
 \tag{27}
\]
At \(r=d\) the cyclic ratio is one and the entire central factor
remains. Continuation outside the anchored disk must retain the
same factors and branches.

## 6. A uniform nonzero local asymptotic at every index

Fix \(0<\rho<1\). Use the power-series branches of
\(\operatorname{Li}_2\) and logarithms in the unit disk. Uniformly
for \(|t|\le\rho\) and every actual \(0\le r\le d\),
\[
 \boxed{\quad
 \mathcal R_r(t)=
 \frac{\exp\!\left\{\dfrac{N}{2\pi i}
       [\operatorname{Li}_2(tQ^r)-\operatorname{Li}_2(t)]\right\}}
      {\sqrt{(1-t)(1-tQ^r)}}\,
                         (1+O_\rho(N^{-1})).
 \quad}
 \tag{28}
\]
The square root is anchored at zero. The relative error is
holomorphic; its fixed \(t\)-derivatives remain \(O(N^{-1})\)
on smaller fixed disks. No interpolation of \(r\) is used.

Here is a proof uniform at both endpoints. The function
\[
                        f_t(s)=\Log(1-te^{2\pi is})
\]
has bounded first two \(s\)-derivatives for \(0\le s\le1\) on
the stated disk. With \(u=r/N\), the composite trapezoidal estimate is
\[
 \sum_{k=0}^{r}f_t(k/N)
   =N\int_0^u f_t(s)\,ds
            +\tfrac12(f_t(0)+f_t(u))+O_\rho(N^{-1}).
\]
For \(r=0\) this is exact with zero integral and zero error.
Moreover
\[
 -\int_0^u f_t(s)\,ds
    =\frac{\operatorname{Li}_2(te^{2\pi iu})
                       -\operatorname{Li}_2(t)}{2\pi i}.
\]
Exponentiating the negative sum proves (28). Applying the estimate
on a slightly larger disk and using Cauchy's estimate proves the
relative-error derivative assertion.

The amplitude is an explicit holomorphic unit. The exact kernel is
zero-free in the disk, and its pointed value is one. At \(r=d\),
(28) remains an asymptotic for the exact \((1-t^N)^{-1}\), not
a deletion of that factor. This local kernel therefore has a
selected nonzero coefficient fixed by its actual source, without an
assigned geometric-cycle coefficient.

## 7. Source and geometric scope

The auxiliary \(t\) is a marked source-resolvent coordinate, not a
peripheral meridian, a filling parameter, or a quantum lift of the
classical companion gauge. The physical Fourier norm (14) and the
transported Newton norm (24) remain distinct. Neither uses an
unknown closed period.

All identities are at the original root and retain the full finite
space. The currents in (4) are fixed-root clock insertions.
Quantum-parameter and peripheral derivatives require their actual
whole families and normal walls before specialization.
Differentiating \(Z^N=I\) as though it held off root would not
supply those derivatives.

The existing Hardy construction already supplies scalar-function
periods for entire signed words. The additional result here is the
complete, controlled current description of this marked cap and
its marked point, coefficient and residue sources. The disk estimate
(28) does not estimate the original root residue at the moving
unit-circle pole \(t=Q\). Its boundary layer and its pairing with
the actual transported component remain to be analyzed.
The result does not replace an arbitrary short component
by the special kernel (8), put the original knot cycle on a positive
Rivin contour, or lower-bound the complete knot scalar.

## Complete proof sources and coverage

Both complete proof sources were read at matching pins. The first
fixes the actual cap, cyclic-column matrix, complete source and face
clock. The second fixes the literature cyclic function, norm divisor,
anchored branches and existing Hardy-period scope.

| Source | SHA-256 |
|---|---|
| [Literal Euler orthonormalizer and sources](research_middle_face_euler_orthonormalizer.md) | 3477cdbbd2dcc1c60ef0c62939f396fee57cd21ed548c2abecff2c4ca06d249d |
| [Original cyclic/Hardy network](actual_cyclic_hardy_dilog_network.md) | bdde89f19901f1df29eeee174c163312bbb40b905852083bd75f0d138e5c65c5 |

The complete [actual Clebsch generating-kernel note](research_actual_clebsch_magnetic_generating_kernel.md)
was read for coverage at SHA-256
9601b29b73caab6c4705efb36abcc5539f6b22ada43961cdbcc2da848aa1b1c6.
Its equation (5) already uses the same finite Gaussian-binomial
generating identity. No novelty is claimed for that identity,
Fourier orthogonality, partial fractions or trapezoidal asymptotics.
The literal-cap identification, complete pointed transport and
source checks are the assembly proved here.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
