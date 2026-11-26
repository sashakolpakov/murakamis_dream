# Actual long-transfer coefficients and their full normal germs

Private written proof, 18 November 2026.

A transfer from the upper donor collar to the lower donor collar has
one retained full-head factorial in the original balanced basis. At the
complete root that factor supplies \(N\). Off root its correct uniform
normalization is \(N^{1-\kappa}\), with a nonvanishing analytic factor.
The two checked extreme corners retain explicit peripheral polynomials.
These are identities and estimates for actual finite matrix entries.
They do not establish a nonzero contraction or another factor of \(N\)
in the closed knot invariant.

The complete directs are B, the literal balanced crossing; E, its
finite-head Euler and normal conventions; and U, the uniform endpoint
factorial bridge. Every formula involving a quantum normal below is
formed before root specialization. The ordinary head path is retained;
no equality of closed ordinary-Jones and ADO-pivot normal germs is used.

## 1. Finite heads, parameters and the cross-collar block

Put \(d=N-1\), \(N\ge2\), \(c_0=2\pi i\), and use the actual coordinates
\[
 h=\frac{c_0}{N-\kappa},\qquad q=e^{h/2},\qquad Q=e^h,\qquad
 M=e^{\nu h/2},\qquad x=-M/q.
 \tag{1}
\]
Fix \(0<r<1/16\), decreasing it if necessary. All estimates hold on
\(|\kappa|,|\nu|\le2r\), with fixed derivatives on smaller disks.
The symbol \(\kappa_{\rm C}\) will always denote the original common
Cartan line; it is not the normal coordinate \(\kappa\).

On the balanced head \(w_0,\ldots,w_d\), define
\[
 F_a=\prod_{j=1}^a(1-Q^j),\qquad
 H_a=\prod_{j=1}^a(MQ^{-j}-M^{-1}),\qquad F_0=H_0=1,
 \tag{2}
\]
\[
 U_F(a)=\frac{F_d}{F_{d-a}}
       =\prod_{j=1}^a(1-Q^{N-j}),\qquad
 U_H(a)=\frac{H_d}{H_{d-a}}
       =\prod_{j=1}^a(MQ^{j-N}-M^{-1}).
 \tag{3}
\]
Every denominator in (2)--(3) with index below \(N\) is a unit
on the stated disk, as follows directly from (1).
The finite head arrows at \(0,d\) remain their prescribed zeros.

With \(A=\mathcal E_1F_2\), B and E give
\[
 \Theta_+=\sum_{n=0}^d\frac{(-1)^nq^{n^2}}{F_n}A^n,\qquad
 \Theta_-=\Theta_+^{-1}
          =\sum_{n=0}^d\frac{q^n}{F_n}A^n.
 \tag{4}
\]
Write \(\sigma_+(n)=(-1)^nq^{n^2}\) and
\(\sigma_-(n)=q^n\). For nonnegative integers \(u,v,w,z\) satisfying
\[
 s=u+w=v+z\le d,\qquad n=d-s,
 \tag{5}
\]
the uncheck block goes from \((d-u,v)\) to \((w,d-z)\).
All its intermediate indices are physical. Direct multiplication of
the lowering and raising arrows gives the exact coefficient
\[
 T_\pm(u,v;w,z)
   =\sigma_\pm(n)\frac{H_{d-u}}{H_w}
                    \frac{F_{d-z}}{F_vF_n}
   =\boxed{\sigma_\pm(n)H_d
       \frac{U_F(s)}{U_H(u)F_vH_wU_F(z)}}.
 \tag{6}
\]
Only a numerator and denominator copy of the same \(F_d\) have
cancelled in the second expression. There has been no off-root
reflection of a lower product into an upper product.

For example, in the two \(G_F=\operatorname{diag}(F_a)\) gauges, the
same coefficient is exactly
\[
 T_\pm^{FF}
 =\sigma_\pm(n)H_d
       \frac{U_F(s)}{U_H(u)U_F(u)H_wF_w}.
 \tag{7}
\]
In two \(G_E=\operatorname{diag}(H_a^{-1})\) gauges it is
\[
 T_\pm^{EE}
 =\sigma_\pm(n)H_d
       \frac{U_F(s)}{U_H(z)U_F(z)H_vF_v}.
 \tag{8}
\]
These follow by multiplying (6) by the actual input gauge divided by
the actual output gauge. They are not independent changes of an
exposed source or co-source. Other endpoint gauges are treated by
that same exact input/output rule.

## 2. Checked coefficients and the surviving peripheral factors

The literal checked factors, in their original order, are
\[
 R_+=\kappa_{\rm C}\,\mathsf P D\Theta_+,\qquad
 R_-=\kappa_{\rm C}^{-1}\Theta_-D^{-1}\mathsf P,\qquad
 D_{a,b}=x^{-a-b}Q^{ab}.
 \tag{9}
\]
Let \(T=d-u+v=w+d-z\), and abbreviate the fraction after \(H_d\)
in (6) by \(\mathcal R\). Thus
\[
 \begin{aligned}
 (R_+)_{(d-z,w),(d-u,v)}
   &=\kappa_{\rm C}x^{-T}Q^{w(d-z)}
                       \sigma_+(n)H_d\mathcal R,\\
 (R_-)_{(w,d-z),(v,d-u)}
   &=\kappa_{\rm C}^{-1}x^TQ^{-(d-u)v}
                       \sigma_-(n)H_d\mathcal R .
 \end{aligned}
 \tag{10}
\]
The first pair of subscripts is the output. In particular the
large inverse corner has the opposite physical input from the
positive corner:
\[
 \boxed{\begin{aligned}
 (R_+)_{(d,0),(d,0)}
     &=\kappa_{\rm C}M^{-d}q^{Nd}H_d,\\
 (R_-)_{(0,d),(0,d)}
     &=\kappa_{\rm C}^{-1}(-1)^dM^dH_d .
 \end{aligned}}
 \tag{11}
\]
For the first identity use
\((-1)^dx^{-d}q^{d^2}=M^{-d}q^{Nd}\); for the second use
\(x^dq^d=(-1)^dM^d\).

At \(q=q_N=e^{\pi i/N}\), but with \(M\) still variable, the
cyclotomic polynomial identity gives the whole expression
\[
 H_d=(-1)^dM^{-d}\sum_{j=0}^dM^{2j}
     =(-1)^d\frac{M^N-M^{-N}}{M-M^{-1}}.
 \tag{12}
\]
The fraction in the last display means its Laurent-polynomial
continuation, including at \(M=1\). Hence
\[
 \boxed{\begin{aligned}
 (R_+)_{(d,0),(d,0)}
       &=\kappa_{\rm C}\sum_{j=0}^dM^{-2j},\\
 (R_-)_{(0,d),(0,d)}
       &=\kappa_{\rm C}^{-1}\sum_{j=0}^dM^{2j}.
 \end{aligned}}
 \tag{13}
\]
Thus both corners equal \(N\kappa_{\rm C}^{\pm1}\) at completeness.
The common Cartan line, all pivots, framing scalars and any whole
external modified-dimension line of the source remain unchanged.
Equation (13) alone is not a closed-source normalization statement.

For comparison, on the genuine ordinary-color head path
\[
 M=-q^N\quad\Longleftrightarrow\quad\nu=\kappa,
 \tag{14}
\]
one has, before any specialization,
\[
 MQ^{-j}-M^{-1}=-M^{-1}(1-Q^{N-j}),\qquad
 H_d=(-1)^dM^{-d}F_d.
 \tag{15}
\]
Consequently (11) becomes
\[
 (R_+)_{(d,0),(d,0)}
       =\kappa_{\rm C}(-1)^dq^{-Nd}F_d,\qquad
 (R_-)_{(0,d),(0,d)}=\kappa_{\rm C}^{-1}F_d.
 \tag{16}
\]
The sign in (15) is necessary even when \(N\) is even.
Equations (11), not (13), define the independent quantum normals.

## 3. Uniform full-head units

There are holomorphic units \(\mathfrak F_N(\kappa)\) and
\(\mathfrak H_N(\kappa,\nu)\) such that
\[
 F_d=N^{1-\kappa}\mathfrak F_N,\qquad
 H_d=(-1)^dN^{1-\kappa}\mathfrak H_N,
 \tag{17}
\]
\[
 \mathfrak F_N(0)=\mathfrak H_N(0,0)=1,\qquad
 C_r^{-1}\le|\mathfrak F_N|,|\mathfrak H_N|\le C_r .
 \tag{18}
\]
Here \(N^{-\kappa}=\exp(-\kappa\log N)\) with real \(\log N\).
All fixed derivatives of the units and their reciprocals are
uniformly bounded on smaller parameter disks.

Here is an elementary proof that retains both endpoint zeros.
The functions
\[
 \phi_\pm(t)=\frac{e^{\pm c_0t}-1}
                  {\pm c_0t(1-t)}
 \tag{19}
\]
have removable values at \(0,1\), are nonzero on a fixed simply
connected neighborhood of \([0,1]\), and admit holomorphic logarithms
\(L_\pm\) there. Shrink \(r\) so that all arguments below lie in
that neighborhood for every \(N\ge2\).
Writing \(\tau=N/(N-\kappa)\), exact factorization gives
\[
 \frac{F_d}{N}
 =\tau^{2d}\frac{\mathcal P_d(-\kappa)}{d!}
   \exp\sum_{j=1}^d
       \left[L_+\!\left(\frac j{N-\kappa}\right)
                         -L_+\!\left(\frac jN\right)\right],
 \tag{20}
\]
\[
 \frac{H_d}{(-1)^dN}
 =M^{-d}\tau^{2d}
       \frac{\mathcal P_d(-\nu)\mathcal P_d(\nu-\kappa)}{(d!)^2}
   \exp\sum_{j=1}^d
       \left[L_-\!\left(\frac{j-\nu}{N-\kappa}\right)
                         -L_-\!\left(\frac jN\right)\right].
 \tag{21}
\]
We used only \(F_d(q_N)=N\), from
\((z^N-1)/(z-1)\) at \(z=1\), and
\(H_d(q_N,1)=(-1)^dN\).

For \(|a|\le4r\), put
\[
 V_N(a)=N^{-a}\prod_{j=1}^d(1+a/j).
 \tag{22}
\]
Its logarithm is
\[
 a\left(\sum_{j=1}^d\frac1j-\log N\right)
  +\sum_{j=1}^d\left[\log(1+a/j)-a/j\right].
 \tag{23}
\]
The first parenthesis is bounded by integral comparison, and the
second sum is bounded by \(C|a|^2\sum j^{-2}\). Thus \(V_N\)
and its reciprocal are uniformly bounded holomorphic units.
Moreover \(d\log\tau\) and \(d\log M\) are uniformly bounded.
The two sums in (20)--(21) are uniformly bounded because the
derivatives of \(L_\pm\) are bounded and
\[
 \left|\frac{j-\nu}{N-\kappa}-\frac jN\right|
       \le C_r\left(\frac{|\nu|}{N}
                       +\frac{j|\kappa|}{N^2}\right).
 \tag{24}
\]
Replace the product ratios in (20)--(21) by
\(N^{-\kappa}V_N(-\kappa)\) and
\(N^{-\kappa}V_N(-\nu)V_N(\nu-\kappa)\), respectively.
This proves (17)--(18); Cauchy's formula proves the derivative
statement. No Stirling formula or root reflection was used.

On the root slice \(\kappa=0\), (12) also gives
\[
 \mathfrak H_N(0,\nu)
       =\frac{\sin(\pi\nu)}{N\sin(\pi\nu/N)}.
 \tag{25}
\]
Its value at zero is one. On \(\nu=\kappa\), (15) gives
\(\mathfrak H_N=M^{-d}\mathfrak F_N\).
Although the normalized units are uniformly bounded,
\(H_d/N\) and \(F_d/N\) include \(N^{-\kappa}\); this factor
must be differentiated in quantum normal calculations.

## 4. Uniform short-product factors in the long block

Write
\[
 \mathcal P_a(t)=\prod_{j=1}^a(j+t),\quad
 S_1(a)=a(a+1)/2,\quad S_2(a,t)=\sum_{j=1}^a(j+t)^2.
 \tag{26}
\]
For \(s\le C N^{3/4}\), substitution of the four actual upper and
lower factorizations of U into (6) gives
\[
 \boxed{\mathcal R
  =(-1)^{v+w}h^{-s}
    \frac{\mathcal P_s(-\kappa)}
     {\mathcal P_u(\nu-\kappa)\,v!\,
      \mathcal P_w(-\nu)\,\mathcal P_z(-\kappa)}
       \exp\{\mathcal L+\mathcal Q+\mathcal E\}},
 \tag{27}
\]
where
\[
 \mathcal L=\frac h2
  [-S_1(s)-S_1(u)-S_1(v)+S_1(w)+S_1(z)
                             +\kappa(s+u-z)],
 \tag{28}
\]
\[
 \mathcal Q=\frac{h^2}{24}
 [S_2(s,-\kappa)-S_2(u,\nu-\kappa)-S_2(v,0)
                     -S_2(w,-\nu)-S_2(z,-\kappa)].
 \tag{29}
\]
All powers are integer powers. The exact holomorphic remainder obeys
\[
 |\mathcal E|\le C_{C,r}|h|^4(s+1)^5=O(N^{-1/4}).
 \tag{30}
\]
Indeed it is the signed sum of the five remainders for
\(U_F(s),U_H(u),F_v,H_w,U_F(z)\). The powers of \(h\) in that
quotient are \(s-u-v-w-z=-s\); the two lower products produce
the displayed sign. Their linear and quadratic exponents give
(28)--(29) in exactly the same order. This also checks every
normal-parameter shift.

Thus (6), (10), (17) and (27) are a uniform full normal-germ
factorization of the actual long coefficient. All displayed factors,
including \(N^{-\kappa}\), \(\sigma_\pm(n)\), \(D\) and
\(\kappa_{\rm C}\), remain exact. On \(s=O(\sqrt N)\) one may
omit \(\mathcal Q\) and replace \(e^{\mathcal E}\) by one with
relative error \(O(N^{-1/2})\). On the larger scale the cubic
occupation term \(\mathcal Q\) is retained.

Every fixed \(\kappa,\nu\) derivative of the normalized relative
error has the same bound on smaller disks. In \(h,M\) coordinates
these bounds are \(O(N^{2j+\ell-1/4})\), or
\(O(N^{2j+\ell-1/2})\) on the smaller collar, for
\(\partial_h^j\partial_M^\ell\). They concern the relative
remainder only; derivatives of all the explicit factors are retained.
Restriction to \(\nu=\kappa\) therefore preserves the genuine
ordinary head normals.

## 5. Source and endpoint scope

The independent head walls are still
\[
 \delta=1-Q^N=1-e^{h\kappa},\qquad
 w_{\rm wall}=MQ^{-N}-M^{-1}
             =M^{-1}(e^{h(\nu-\kappa)}-1).
 \tag{31}
\]
Neither was divided out. Any head/collar projector and its two
interface currents remain the actual finite matrices. In particular
the long block is part of the complement of a same-collar
compression; it cannot be obtained by replacing that compression
by an unrestricted exponential.

Equations (6)--(31) change no support and sum no neighboring source.
The indices \(u,v,w,z\) remain integers, including the exact
\(d=N-1\) offset. The original finite Fourier projectors and their
upper endpoints are not replaced by periodic or delta kernels.
The \(N\) at the root is a verified crossing-entry normalization,
with its complete peripheral and normal factors displayed.
It is not a second factor to multiply into a separately normalized
pivotal closing identity, nor a proof of noncancellation.

Finally, the ordinary path here concerns the actual finite heads
and crossing insertions. A closed source with the ADO pivot
\(K^{1-N}\) has not thereby become the ordinary source with pivot
\(K\). Their entire pivot and twist comparison would still be
required for a claim about closed ordinary-Jones normal derivatives.

## Complete direct-source pins

* B: notes/balanced_verma_coherent_braiding.md, SHA256
  0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.
* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* U: notes/research_uniform_endpoint_factorial_normal_bridge.md,
  SHA256 e7c7c761e8c7d11277c9e413d99464f95812924379ebb864327d77fa8e6464a8.

All three complete direct texts were read nontruncated in this author
sequence. The literal coefficient, full-head normalization, checked
corner and long-block assembly proofs above were checked in their
original order. Only written mathematics and text/hash operations
were used. No frozen or public file was edited.
