# The full quotient-section kernel near its coalescent endpoints

Private written proof, 19 November 2026.

The actual quotient section has two finite endpoint terms. We estimate
their difference together on the scale \(v=e^{s/N}\), including \(s=0\).
The result is an explicit nonzero local scalar profile for small activity,
with the original caps and true meridian derivatives. This scalar
estimate alone does not identify a geometric-head kernel: its Cartan
insertion has a finite shift profile, computed below, rather than the exponential of its
mean occupation.

R supplies the actual section and reduced source. Q supplies the
low-degree q-inverse method. We verify its hypotheses for the entire
recipient coproduct, without replacing it by a product of individual
Euler factors. These are the two complete proof directs.

## 1. The actual section and both endpoints

Fix \(r\ge1\) recipient heads, one first head, and
\[
 N\ge2,\quad d=N-1,\quad h=N^{-1},\quad c=2\pi i,\quad
 Q=e^{ch},\quad x=-M e^{-ch/2},\quad
 f_n=(Q;Q)_n,\qquad E_N(Z)=\sum_{n=0}^d Z^n/f_n.        \tag{1}
\]
The quantum root is fixed when \(M\ne0\) varies. The physical arrows are
\[
 Fe_b=(1-Q^{b+1})e_{b+1},\quad Fe_d=0,\qquad
 Ke_b=xQ^{-b}e_b.
\]
On the recipients, numbered \(1,\ldots,r\), put
\[
 F_{\rm r}=\sum_{j=1}^rK_1^{-1}\cdots K_{j-1}^{-1}F_j,
 \qquad A=x^{-1}F_{\rm r}.
                                                               \tag{2}
\]
Every statement uses these finite arrows. In particular
\(F_{\rm r}^N=0\) throughout the meridian family. Indeed, for
\(Y_j=K_1^{-1}\cdots K_{j-1}^{-1}F_j\),
\(Y_iY_j=Q^{-1}Y_jY_i\) for \(i<j\) and \(Y_j^N=0\).
The intermediate Gaussian coefficients in degree \(N\) vanish,
since their numerator contains \(1-Q^N\) and their denominators
contain only \(1-Q^k\), \(0<k<N\). Induction over the heads proves
the assertion, also at even and composite levels.

The extra first head is kept separate from the recipient labels:
\(F_\Sigma=F_{\rm first}+K_{\rm first}^{-1}F_{\rm r}\).
With \(L e_b=e_{b-1}\), \(Le_0=0\), R gives
\[
 S=\sum_{k=0}^d L^k\otimes A^k/f_k,\qquad
 S^{-1}F_\Sigma S=F_{\rm first},\qquad
 q_F=p_0S^{-1},\qquad i_0u=e_0\otimes u.                \tag{3}
\]
Here \(F_\Sigma\) is the full ordered coproduct. Define its actual section
\[
 i_a=E_N(aF_\Sigma)i_0
       =S\left(\sum_{n=0}^d a^ne_n\otimes I\right).
                                                               \tag{4}
\]
For the second equality conjugate by \(S\), use \(S^{-1}i_0=i_0\),
and \(F_{\rm first}^ne_0=f_ne_n\). Consequently \(q_Fi_a=I\), and for
every actual total intertwiner \(W\),
\[
                    q_FW i_a=q_FW i_0=\mathcal B(W).   \tag{5}
\]
This is an exact source identity, not a statement that \(i_0\) or
\(i_a\) is annihilated by \(F_\Sigma\).

Let \(\ell_y(e_n)=y^n\) be the physical first-head evaluation row
and write \(v=ay\). Directly from (3),(4),
\[
 (\ell_y\otimes I)i_a
  =\sum_{k=0}^d\frac{(aA)^k}{f_k}
                   \sum_{\ell=0}^{d-k}v^\ell
  =:\widehat{\mathcal S}_N(a,v).                       \tag{6}
\]
Thus
\[
 \boxed{\widehat{\mathcal S}_N(a,v)=
       \frac{E_N(aA)-v^NE_N(aA/v)}{1-v}.}              \tag{7}
\]
The finite sum (6) defines the expression at \(v=0,1\); the apparent
negative powers and denominators are removable. At coalescence,
with \(D_a=a\partial_a\),
\[
           \widehat{\mathcal S}_N(a,1)=(N-D_a)E_N(aA).
                                                               \tag{8}
\]
No endpoint in (7) has been discarded. The coordinates \(a,v\)
are convenient for the estimate. For \(a\ne0\), they represent the
literal first-head row \(y=v/a\). Their analytic continuation to
\(a=0,v\ne0\) is the finite polynomial (6), not a finite physical
value of \(y\).

## 2. A local unit for the entire recipient Euler polynomial

Choose a subset \(\mathcal H\subset\{1,\ldots,r\}\) of factorial recipients.
On those heads let \(G_Fe_b=f_be_b\), and put
\(G_{\mathcal H}=\prod_{j\in\mathcal H}G_{F,j}\),
\(A_{\mathcal H}=G_{\mathcal H}^{-1}AG_{\mathcal H}\).
All inverse frame changes stay on the incident source tensors.
Use evaluation variables \(z_j\) and ordinary-binomial input
variables \(w_j\) in this chosen frame, and set
\[
 I(\mathbf z,\mathbf w)=\prod_{j=1}^r(1+z_jw_j),\qquad
 \mathcal E_N(a)=
 \sum_{\alpha,\beta}\mathbf z^\alpha
 [E_N(aA_{\mathcal H})]_{\alpha\beta}
                    \prod_j\binom d{\beta_j}w_j^{\beta_j}.
                                                               \tag{9}
\]
Every index in the actual kernel lies between \(0\) and \(d\).
Work on buffered compact sets with
\[
 M\ne0,\quad 1+z_jw_j\ne0,\qquad
 |z_jw_j|\le\rho<1/8\quad(j\in\mathcal H).              \tag{10}
\]
There is no size condition on physical-recipient products.
The conclusion below holds on a sufficiently small fixed disk
\(|a|<a_0\), uniformly for sufficiently large \(N\).

First remove only the factorial-recipient output caps. Its output
raising arrow is multiplication by \(z_j\); physical recipients keep
\(z_j(1-QT_j)\), \(T_j:z_j\mapsto Qz_j\). The resulting operator
\(\widehat A\) on output polynomials is
\[
 \widehat A=\sum_{j=1}^r x^{-j}z_j
       \left(\prod_{i<j}T_i\right)
       \begin{cases}1,&j\in\mathcal H,\\1-QT_j,&j\notin\mathcal H.\end{cases}
                                                               \tag{11}
\]
For the auxiliary finite kernel
\(\widehat{\mathcal E}_N=E_N(a\widehat A)I^d\), the exact equation is
\[
 \widehat{\mathcal E}_N(Qa)
   =(1-a\widehat A)\widehat{\mathcal E}_N(a)
                  +a^N\widehat A^NI^d/f_d.             \tag{12}
\]
For the actual capped operator the last term is zero by (2).
It need not vanish in the auxiliary calculation. We keep it;
it starts in degree \(N\). The equality follows termwise from
\((1-Q^n)/f_n=1/f_{n-1}\).

For clarity we give the exact coefficients used in the estimate.
Index by \(\nu=(j,e)\), with \(e=0\) always and also \(e=1\)
when \(j\notin\mathcal H\). Put
\[
 J_\nu=\{i:i<j\}\cup(\{j\}\text{ if }e=1),\qquad
 Y_\nu=c\sum_{i\in J_\nu}z_i\partial_{z_i},
\]
\[
 b_{\nu,h}=(-1)^eQ^ex^{-j}z_j
    \prod_{i\in J_\nu}
       \left(\frac{1+Qz_iw_i}{1+z_iw_i}\right)^{h^{-1}-1}.
                                                               \tag{13}
\]
In particular, if \(u_i=z_iw_i/(1+z_iw_i)\), the first two
coefficients used below are explicitly
\[
 b_{\nu,0}=(-1)^e(-M)^{-j}z_j e^{c\sum_{i\in J_\nu}u_i},
 \qquad
 \frac{b_{\nu,1}}{b_{\nu,0}}
 =ec+\frac{jc}{2}
    +\sum_{i\in J_\nu}\left[-cu_i+\frac{c^2}{2}u_i(1-u_i)\right].
                                                               \tag{13a}
\]
The quotient denotes the analytic multiplier even where \(z_j=0\).
Branches of ratio logarithms are zero at \(h=0\); all coefficients
are analytic there on (10). This is an analytic coefficient
extension, not an off-root finite representation. For
\(B_N=\widehat{\mathcal E}_N/I^d\), the below-degree-\(N\)
logarithm \(V_N=h\log B_N\) satisfies
\[
 \frac{e^{hcD_a}-1}{h}V_N
 =\mathscr F_h(V_N):=
   \log\left(1-a\sum_\nu b_{\nu,h}
              e^{(e^{hY_\nu}-1)V_N/h}\right).           \tag{14}
\]

All hypotheses of Q's low-degree q-inverse argument are now explicit.
There are finitely many analytic shifts, each accompanied by \(a\).
For \(n\le\delta N\), \(0<\delta<1/2\), the inverse multiplier
\(h/(Q^n-1)\) is bounded by \(C_\delta/n\). Positive spatial
padding by \(nh\) stays inside (10) after choosing \(\delta\).
The coefficient induction is dominated by
\[
 D_aU=\frac{C(y)a}{1-C(y)(a+D_aU+\mathcal LU)},\quad
 U(0,y)=0,\qquad \mathcal L=C(1+y)^2\partial_y.           \tag{15}
\]
As proved in Q, division by \(a\) gives an implicit analytic
equation for \(U_a\) whose derivative at \(a=0\) is one.
Its positive small branch and characteristic solution give
\(|[a^n]V_N|\le C R^{-n}\) for \(n\le\delta N\).
Here the shifts \(Y_\nu\) have no activity component, so the same
spatial padding construction applies.

The separate whole-polynomial bound also holds directly.
On a fixed coordinate polydisk each of the at most \(2r\) terms
in (11) has weighted coefficient norm bounded independently of
\(N\); its clock shifts have unit modulus. Thus
\(\|\widehat A^nI^d\|_{\rm coeff}\le C^{n+rd}\).
The root reflection identity
\(|f_n||f_{d-n}|=N\) gives \(1/|f_n|\le2^d\).
It follows that \(|B_N|\le e^{C_rN}\) on a fixed activity disk.
Matching the actual polynomial with the exponential of its
degree-\(\delta N\) logarithm, then shrinking the disk ratio,
recovers every high degree with exponentially small relative error.
This is precisely Q's complete-tail argument, including the
auxiliary forcing in (12).

Here are the specified phase and first transport. Expand
\(b_{\nu,h}=b_{\nu,0}+hb_{\nu,1}+O(h^2)\), and define
\[
 Z(V)=1-a\sum_\nu b_{\nu,0}e^{Y_\nu V},\qquad
 \mathscr F_0(V)=\log Z(V),
\]
\[
 \mathscr F_1(V)=-\frac{a}{Z(V)}
   \sum_\nu e^{Y_\nu V}
       \left(b_{\nu,1}+\tfrac12b_{\nu,0}Y_\nu^2V\right).
\]
The unique small analytic solutions, with zero initial data, are
\[
 cD_aV=\mathscr F_0(V),\quad V(0)=0,\qquad
 (cD_a-d\mathscr F_0[V])T
     =\mathscr F_1(V)-\tfrac12c^2D_a^2V,\quad T(0)=0.    \tag{16}
\]
After division by \(a\) these are an analytic characteristic
equation and a linear transport. Q's padded error equation has
forcing \(O(h^2a)\) and gives
\([a^n](V_N-V-hT)=O(h^2R^{-n})\) for \(n\le\delta N\).
The entire finite tail just proved then gives
\[
 \widehat{\mathcal E}_N=I^d e^{NV}\mathfrak a(1+O(N^{-1})),
            \qquad \mathfrak a=e^T,\quad \mathfrak a(0)=1. \tag{17}
\]

To restore a factorial recipient, mark \(z_j\mapsto\xi_jz_j\).
Choose \(R_*>1\) with \(R_*\rho<1\) and
\(\log R_*-\log((1+R_*\rho)/(1-\rho))>0\).
The same theorem holds on all finitely many marker circles.
Their phase is \(O(a)\); their amplitude is a bounded unit.
Cauchy extraction of output degrees at least \(N\) supplies
\(R_*^{-N}\), while the background costs at most
\(((1+R_*\rho)/(1-\rho))^d\) per marked head.
Shrink \(a_0\) after these constants. Inclusion--exclusion
of the finitely many output projections has exponentially small
relative error. Since every recipient transfer raises occupation,
this projection is exactly its original cap. Therefore
\[
 \boxed{\mathcal E_N(a)=I^d e^{NV(a)}\mathfrak a(a)(1+r_N(a)),
       \quad r_N=O(N^{-1}),\quad \mathfrak a=e^T\ne0.}   \tag{18}
\]
All fixed coherent and true fixed-\(Q\) meridian derivatives
\(\partial_\mu^k\), \(M=e^\mu\), of \(r_N\) have the same
bound on smaller fixed buffers. The phase and amplitude keep
every \(x(M)\), \(Q\), and degree-\(N-1\) contribution.

No identity \(E_N(a\sum Y_j)=\prod E_N(aY_j)\) was used.
Such a product has additional total degrees at least \(N\).
The theorem estimates the actual total polynomial, and retains
its root cancellations inside (12).

## 3. The uniform coalescent profile

Let \(\mathcal K_N(a,v)\) be the recipient kernel of (6), with the
same hybrid frames and binomial inputs as (9). Linearity gives exactly
\[
 \mathcal K_N(a,v)=
       \frac{\mathcal E_N(a)-v^N\mathcal E_N(a/v)}{1-v}.
                                                               \tag{19}
\]
Put
\[
 v=e^{s/N},\qquad H(a)=1-D_aV(a),\qquad
 \mathcal L(s,H)=
 \begin{cases}(e^{sH}-1)/s,&s\ne0,\\H,&s=0.\end{cases}   \tag{20}
\]
We may shrink the activity disk so that the scalar \(H(a)\)
is uniformly close to one.

The exact subtraction has a convenient integral form. Set
\[
 F_N(s)=e^s\frac{\mathcal E_N(ae^{-s/N})}{\mathcal E_N(a)}.
\]
Then \(F_N(0)=1\) and, by (19),
\[
 \frac{\mathcal K_N(a,e^{s/N})}{N\mathcal E_N(a)}
 =\frac{\int_0^1F_N'(\theta s)\,d\theta}
        {\int_0^1e^{\theta s/N}\,d\theta},\qquad
 F_N'(s)=F_N(s)
   \left[1-N^{-1}D_a\log\mathcal E_N(ae^{-s/N})\right].
                                                               \tag{21}
\]
These formulas hold by analytic continuation at \(s=0\).
For every fixed bounded complex \(s\)-set, use (18) on a slightly
larger activity buffer. Taylor expansion and its normalized
derivative bound give
\[
 F_N(s)=e^{sH}(1+O(N^{-1})),\qquad
 F_N'(s)=H e^{sH}+O(N^{-1}).                           \tag{22}
\]
For example
\(N[V(ae^{-s/N})-V(a)]=-sD_aV+O(N^{-1})\);
the change in \(r_N\) is \(O(|s|N^{-2})\).
All estimates are holomorphic and uniform with fixed derivatives
in the rescaled variables and in the true meridian.
Substituting into (21) proves the full endpoint estimate
\[
 \boxed{\mathcal K_N(a,e^{s/N})
 =N I^d e^{NV(a)}\mathfrak a(a)
          \left[\mathcal L(s,H(a))+O(N^{-1})\right].}    \tag{23}
\]
The bracket error and all its fixed \(a,s,\mathbf z,\mathbf w,\mu\)
derivatives are \(O(N^{-1})\) on smaller buffers.
This is an absolute profile estimate even where \(\mathcal L\)
vanishes. On any compact where \(\mathcal L\) is a unit, it is
a relative estimate and the exact kernel is nonzero for large \(N\).
In particular a fixed neighborhood of \(a=s=0\) has that property,
since \(\mathcal L(0,1)=1\).

At coalescence itself,
\[
 \mathcal K_N(a,1)
       =N I^d e^{NV(a)}\mathfrak a(a)
                         [1-D_aV(a)+O(N^{-1})].        \tag{24}
\]
The leading amplitude is explicitly \(\mathfrak a\mathcal L\), with the
first transport \(T\) in (16), and the factor \(N\) is retained.
In an unscaled full phase \(\log I+V\), the amplitude also contains
the exact \(I^{-1}\), since \(d=N-1\).

The derivatives just stated use the rescaled coordinate \(s=N\log v\).
For original \(a,y\) with \(v=ay\ne0\), converting fixed coherent
derivatives brings the corresponding factors of \(N\); no uniform
unscaled transverse derivative claim is made. At fixed \(N\),
true meridian differentiation holds \(a,y,Q\) fixed, hence also
holds \(v,s\) fixed. It incurs no such coordinate conversion.

## 4. The head profile and its exact affine transport

The profile is not a lower-occupation point. Indeed (6) gives the
exact identities
\[
 \mathcal K_N(a,1)=(N-D_a)\mathcal E_N(a),
\]
\[
 (v\partial_v\mathcal K_N)(a,1)
   =\tfrac12[(N-D_a)^2-(N-D_a)]\mathcal E_N(a).
                                                               \tag{25}
\]
On a unit profile, (23) and its derivatives imply
\[
 \frac{v\partial_v\mathcal K_N}{N\mathcal K_N}
       \longrightarrow \partial_s\log\mathcal L(s,H),
 \qquad
 \left.\frac{v\partial_v\mathcal K_N}{N\mathcal K_N}
                                           \right|_{v=1}
       \longrightarrow H/2.                           \tag{26}
\]
For small \(a\) this is close to \(1/2\), not zero.

Likewise the literal first-head Cartan insertion sends
\(\ell_y\) to \(x\ell_{Q^{-1}y}\). Its normalized kernel is exactly
\[
 x\,\frac{\mathcal K_N(a,e^{(s-c)/N})}
          {\mathcal K_N(a,e^{s/N})}
 =x_{\rm cl}\frac{\mathcal L(s-c,H)}{\mathcal L(s,H)}
                                      +O(N^{-1}),\quad x_{\rm cl}=-M,
                                                               \tag{27}
\]
where the denominator profile is a unit. Equation (23) is used
on a bounded set containing both \(s\) and \(s-c\); its numerator
may vanish. This is a finite shift of the profile, not the
exponential of (26). At the continued point \(a=0,s=0\), the exact
first-head occupation average is \(d/(2N)\), whereas the exact Cartan
sum is \(xN^{-1}\sum_{n=0}^dQ^{-n}=0\).
Thus a nonzero scalar in (24) does not supply a regular
geometric-head canonical graph or identify \(F_\Sigma=0\).

There is nevertheless an exact transport character in the full
profile, including its vacuum term. At the operator level, (7)
and the homogeneous version of (12) give
\[
 (1-Q^{-1})\widehat{\mathcal S}_N(a,Q^{-1})
       =E_N(aA)-E_N(QaA)=aA E_N(aA).
                                                               \tag{28}
\]
The matrix \(E_N(aA)\) is invertible: it is the identity plus
a polynomial in the nilpotent \(A\) with zero constant term.
Thus the exact completed expression is
\[
 I-(1-Q^{-1})\widehat{\mathcal S}_N(a,Q^{-1})
                                    E_N(aA)^{-1}=I-aA. \tag{29}
\]
This keeps the vacuum identity \(I\). It is a matrix identity;
its use does not permit multiplication of normalized scalar
coherent kernels.

More generally put \(J_N(a,v)=(1-v)\widehat{\mathcal S}_N(a,v)\).
The full affine row and its matrix completion are
\[
 J_N(a,Q^{-1}v)
   =(I-aA/v)J_N(a,v)+(aA/v)E_N(aA),
\]
\[
 Y_N(a,v)=I-(1-v)\widehat{\mathcal S}_N(a,v)E_N(aA)^{-1}
        =v^NE_N(aA/v)E_N(aA)^{-1}
\]
with the exact homogeneous row
\[
 Y_N(a,Q^{-1}v)=(I-aA/v)Y_N(a,v),\qquad Y_N(a,1)=I.    \tag{30}
\]
This follows from the homogeneous Euler row; all factors are
polynomials in \(A\). The equality extends through its removable
expressions at \(v=0\). Its complete clock cycle is exact:
\[
 \prod_{j=0}^{N-1}(I-aQ^jA/v)=I-(aA/v)^N=I.
\]
The root and the actual nilpotence, rather than a discarded endpoint,
pay this product.

This completion also has a uniform estimate in actual matrix norm.
Give the chosen recipient occupation coordinates the coefficient
Euclidean norm. In a physical frame \(\|F_j\|\le2\), and in a
factorial frame \(\|G_F^{-1}F_jG_F\|\le1\).
Also \(\|K_j^{-1}\|=|M|^{-1}\), so on a fixed meridian buffer
\(\|A_{\mathcal H}\|\le B_r\), independently of \(N\).
After a further activity restriction
\(|a|B_r\le\rho<1\), for bounded \(s\) one has
\[
 \boxed{
 Y_N(a,e^{s/N})
   =e^s(I-aA_{\mathcal H})^{-s/c}+O_{\rm op}(N^{-1}).
 }                                                            \tag{31}
\]
Here and in this estimate \(Y_N\) is expressed in that same hybrid
frame. The matrix on the right uses the actual \(N\)-dependent
\(A_{\mathcal H}(M)\). Its power is the convergent binomial series
at \(a=0\), not a classical scalar substitution. Both matrices
and their inverses are uniformly bounded, and the analogous inverse
comparison has the same error.

Here is a direct logarithmic proof including the whole cap. Put
\(Z=aA_{\mathcal H}\). Modulo \(Z^N\), the homogeneous Euler
row determines the logarithm coefficient by coefficient, giving
the exact nilpotent identity
\[
 \log E_N(Z)=\sum_{k=1}^{N-1}\frac{Z^k}{k(1-Q^k)}.
\]
One can verify this without any analytic logarithm choice:
its difference under \(Z\mapsto QZ\) is
\(-\sum_{k<N}Z^k/k=\log(I-Z)\), and the constant term is zero.
Consequently the marked logarithm of \(Y_N\) is
\[
 \Lambda_N(s)=sI+
       \sum_{k=1}^{N-1}
       \frac{e^{-sk/N}-1}{k(1-Q^k)}Z^k,\qquad
                         Y_N=e^{\Lambda_N(s)}.        \tag{32}
\]
For \(k\le N/2\), analyticity at \(t=0\) of
\((e^{-st}-1)/(1-e^{ct})\) gives
\[
 \left|\frac{e^{-sk/N}-1}{k(1-Q^k)}-\frac{s}{ck}\right|
                                      \le C_S/N.
\]
For \(N/2<k<N\), the first coefficient is bounded by
\(C_S/(N-k)\), using the elementary sine bound. The factor
\(\rho^k\) pays this entire upper half, while the missing infinite
logarithmic tail is also exponentially small. Therefore
\[
 \left\|\Lambda_N(s)-
        s\left[I-c^{-1}\log(I-Z)\right]\right\|
                                      \le C_{\rho,S}/N.
\]
All logarithms on the right are their convergent series at zero.
The two matrices commute and have uniform norm bounds. Exponentiating
proves (31) and the inverse comparison, including the stated
uniform bounds for both inverses.
At coalescence the exact derivative gives an additional matrix row:
\[
 \frac1N\widehat{\mathcal S}_N(a,1)E_N(Z)^{-1}
 =I-\frac1N\sum_{k=1}^{N-1}\frac{Z^k}{1-Q^k}
 =I-c^{-1}\log(I-Z)+O_{\rm op}(N^{-1}).                 \tag{33}
\]
Here the section matrix is expressed in the same hybrid frame.
Buffered holomorphy gives the same \(O_{\rm op}(N^{-1})\)
for every fixed \(a,s,\mu\) derivative. This is a bound in the
declared actual coordinates, not a bound for separate \(G_F\)
interfaces or the returning \(q_F\).

The corresponding scalar limit follows separately from the actual
homogeneous row. Let \(\mathcal E_N^{F}(a)\) be (9) with the
literal insertion \(G_{\mathcal H}^{-1}F_{\rm r}G_{\mathcal H}\)
on the output of \(E_N(aA_{\mathcal H})\). Exactly,
\[
 \frac{\mathcal E_N^{F}(a)}{\mathcal E_N(a)}
   =\frac{x}{a}
        \left(1-\frac{\mathcal E_N(Qa)}{\mathcal E_N(a)}\right)
   = f_{\rm r,out}(a)+O(N^{-1}),\qquad
 f_{\rm r,out}(a)=
          \frac{x_{\rm cl}}{a}(1-e^{cD_aV(a)}).          \tag{34}
\]
The expressions extend at \(a=0\). The error and its fixed
derivatives also extend with the same bound: both numerators vanish
at zero, and the normalized remainder in (18) has buffered derivative
bounds. All caps and the true meridian dependence remain in this
inserted kernel.

There is an explicit recipient expression as well. Put
\(u_i'=z_iw_i/(1+z_iw_i)+z_iV_{z_i}\) and \(A_i'=e^{cu_i'}\).
Equation (16) with the literal coefficients (13) gives
\[
 f_{\rm r,out}=
  \sum_{j=1}^r x_{\rm cl}^{-(j-1)}z_j
     \left(\prod_{i<j}A_i'\right)
     \begin{cases}1,&j\in\mathcal H,\\1-A_j',&j\notin\mathcal H.\end{cases}
                                                               \tag{35}
\]
These are the output physical or factorial raising symbols in the
retained frame; their formula follows here from the actual q-difference
row and its proved kernel, not an independent product of symbols.

The separately completed scalar quotient is
\(\mathcal Y_N=1-(1-v)\mathcal K_N/\mathcal E_N(a)
=v^N\mathcal E_N(a/v)/\mathcal E_N(a)\).
Equivalently it is the kernel of \(Y_N(a,v)E_N(aA)\), in the
chosen recipient frames, divided by the kernel of \(E_N(aA)\).
It is not an independently established kernel symbol for \(Y_N\)
or \(E_N(aA)^{-1}\). It is \(F_N(s)\) in (21), so it tends to the following leading
profile:
\[
 Y(s)=1+s\mathcal L(s,H)=e^{sH},\qquad
 C(a)=e^{-cH(a)}=e^{cD_aV(a)}
                   =1-a f_{\rm r,out}(a)/x_{\rm cl}.
\]
Since \(e^{-c}=1\), it has the exact scalar transport law
\[
                         Y(s-c)=C(a)Y(s).              \tag{36}
\]
Thus the affine profile, including its vacuum \(1\), recovers a
unit transport character. The mean occupation or the ratio in
(27) alone is not that character. These identities do not identify
the returning \(q_F\) pairing or a selected geometric relative class.

Finally (5) remains the source-preserving statement. In the hybrid
recipient frame its maps are conjugated by the same \(G_{\mathcal H}\) on
their incident tensors. The original pointed source remains R's
\[
 \Phi_0(W)=
 \operatorname{Tr}_{\rm r}
   \left[\frac{D_N(M)}{D_N(MK_{\rm r})}\mathcal B(W)\right],
 \qquad D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},              \tag{37}
\]
with its prescribed removable continuation, true meridian jet,
and every external scalar line. The returning \(q_F\) is still
present. This theorem estimates the actual evaluation of its full
section, including both endpoints, on the stated small-activity,
rescaled coalescent window. It does not estimate that returning
pairing, transport arbitrary section parameters, or select the
original geometric relative cycle.

## Complete proof-source pins

* Q: notes/research_physical_crossing_qexponential_section_kernel.md,
  424 lines, SHA256
  a935669d6c534f3c1f572abefcc1687f1e6150d85218cfc6c5e398de0a13a404.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

Both complete directs were freshly read nontruncated in this active
author sequence. The entire matching final was read back, every used
implication checked, and all three hashes renewed before freezing.
Only written mathematics and text/hash operations were used; frozen
and public files are unchanged.
