# Whole-meridian fusion of the two complementary Gauss factors

Private written proof, 19 November 2026.

The reflected Gauss factor and the actual transported
complementary-degree factor have an exact product identity after the physical
full twist. Its scalar contains precisely the original complementary
source divisor. Differentiating this whole-meridian identity gives
the full combined first normal, including every root Jordan entry.
It does not differentiate a root-only factorization.

This is a building-block identity at every fixed width and every actual
degree \(0\le T\le rd\). It supplies a dual-normal convolution without a
spectral-projector norm. It does not estimate either factor's inverse
on a coherent window or discard a noncommuting exterior word.
Sections 1--4 give an independent two-tail calibration. Section 5
proves the full-width identity, using W's finite block-braid proof
on every highest multiplicity. The complete directs are G, L, R,
and W, pinned below.

## 1. The actual reflected-domain operators

Put
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 f_n=(Q;Q)_n,\quad M=e^\mu,
 \qquad 1\le H<N/2,\quad T=d-H,\quad C=Q^H.
 \tag{1}
\]
The quantum root is fixed. The original two-head degree space is
\(V_T=\operatorname{span}\{|a,T-a\rangle:0\le a\le T\}\).
Write \(E_\pm,F_\pm,K_\pm,\Omega_\pm\) for the actual totals at
meridian \(M^{\pm1}\), with
\[
 \Omega_\pm=F_\pm E_\pm+qK_\pm+q^{-1}K_\pm^{-1}.
\]
On \(V_T\), \(K_-=M^{-2}C\).
G's actual Gauss polynomial is denoted by
\(A_N(M;k,z)\). Its finite formula and normalization are
\[
 A_N(M;K,\Omega)
 =\sum_{n=0}^d\frac{Q^{-n}x_+^{-n}}{f_n}
        \frac{H_d(M)}{H_n(M)}F^nE^nK^{d-n},
 \quad x_+=-M/q,
 \quad H_n(M)=\prod_{j=1}^n(MQ^{-j}-M^{-1}).
 \tag{2}
\]
The quotient \(H_d/H_n\) is its finite product. Thus this is
analytic near \(M=1\), with every transfer cap retained.

Let \(\mathscr C_2(M)\) be the actual balanced turnover with tensor
reversal. On one head its coefficient is
\[
 \mathscr C(M)w_a
   =\left\{\prod_{j=1}^a
       \frac{MQ^j-M^{-1}}{1-Q^j}\right\}w_{d-a}.
 \tag{3}
\]
It is invertible near one. Direct ratios of consecutive coefficients
give
\(\mathscr C_2^{-1}E_+\mathscr C_2=F_-\),
\(\mathscr C_2^{-1}F_+\mathscr C_2=E_-\), and
\(\mathscr C_2^{-1}K_+\mathscr C_2=K_-^{-1}\).
The missing top and bottom arrows give zero on both sides.
Tensor reversal restores the ordered coproduct.

Remove only the common crossing scalar from G's degree coupon:
\[
 L(M)=\kappa(M)^{-2}D_{\rm top}(M)\mathscr C_2(M)
      =x_+^{-2d}t^{\mathsf n}\mathscr C_2(M),
 \qquad t=x_+^{-1}Q^{-1}=-M^{-1}q^{-1}.
 \tag{4}
\]
It maps \(V_T\) to the actual degree \(2d-T\).
Because \(E\) lowers and \(F\) raises integer degree,
\[
 L^{-1}E_+L=tF_-,\qquad L^{-1}F_+L=t^{-1}E_-,
 \quad L^{-1}K_+L=K_-^{-1},\quad
 L^{-1}\Omega_+L=\Omega_-.
 \tag{5}
\]
For the last equality use
\(EF-FE=(q-q^{-1})(K-K^{-1})\). In particular the two scalar
arrow factors cancel in the Casimir; neither is omitted separately.

Define on the fixed space \(V_T\)
\[
 A_-(M)=A_N(M^{-1};K_-,\Omega_-),\qquad
 B_+(M)=L(M)^{-1}A_N(M)|_{V_{2d-T}}L(M)
       =A_N(M;K_-^{-1},\Omega_-).
 \tag{6}
\]
The coefficient meridian in \(B_+\) is \(M\), whereas its underlying
total is the reflected \(\Omega_-\). Both matrices are analytic and
commute for the entire meridian germ.
Let
\[
 \mathcal R_-(M)=\kappa(M^{-1})^{-1}
        R_{\rm phys}(M^{-1})|_{V_T}
 \tag{7}
\]
be the stripped positive checked crossing. R proves that the
physical crossing is an invertible total intertwiner for this
whole fixed-root meridian family. All three matrices in (6),(7)
therefore commute.

## 2. Exact fusion and its source scalar

The whole-meridian identity is
\[
 \boxed{\quad
 A_-(M)B_+(M)\mathcal R_-(M)^2=\Sigma_{N,H}(M)I_{V_T},
 \quad
 \Sigma_{N,H}(M)
   =Q^{H^2}M^{2d-4H}D_N(M)D_N(M^3C^{-1}),
 \quad}
 \tag{8}
\]
where \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\) has its Laurent-polynomial
continuation. An equivalent finite-product expression, useful in
the proof, is
\[
 \Sigma_{N,H}(M)
  =Q^{H(H+1)}M^{4T}(M^2Q;Q)_d
                   \frac{1-M^{-6N}}{1-C^2M^{-6}} .
 \tag{9}
\]
The denominator in (9) is a unit near one because \(C^2\ne1\).
Using the physical crossing instead of (7) multiplies the right
side of (8) by \(\kappa(M^{-1})^2\). No framing scalar is changed.

Here is a proof entirely by finite matrices and products. For
generic \(M\) near one construct the actual highest vector \(h_j\)
of degree \(j\), \(0\le j\le T\), with first coefficient one.
If \(h_{j,a}\) is its coefficient at \(|a,j-a\rangle\), the equation
\(E_-h_j=0\) gives
\[
 \frac{h_{j,a+1}}{h_{j,a}}
 =-\frac{M^{-1}Q^{-(j-a)}-M}
 {(M^{-1}Q^{-(a+1)}-M)x_-Q^{-(j-a-1)}},
 \qquad x_-=-M^{-1}/q.
 \tag{10}
\]
All displayed denominators are nonzero on a punctured generic
neighborhood, and in fact near the root for these indices.
Multiplication telescopes the lowering products:
\[
             h_{j,j}=(-1)^jx_-^{-j}Q^{j(j-1)/2}.
 \tag{11}
\]
The descendant \(F_-^{T-j}h_j\) is nonzero. Its first-occupation-zero
coefficient is \(x_-^{-(T-j)}f_T/f_j\ne0\): only the first term of
\(h_j\) and the all-second-head raising path can reach that position.
Its Casimir eigenvalue is
\[
            \lambda_j(M)=qM^2Q^j+q^{-1}M^{-2}Q^{-j}.
 \tag{12}
\]
These \(T+1\) values are distinct away from a finite meridian set,
so these descendants form a basis there.

The first row of R's literal checked crossing has only its last
column on degree \(j\), with stripped coefficient \(x_-^{-j}\).
Since it preserves the highest line, (11) gives its eigenvalue
on that line, and hence on its descendant:
\[
       \mathcal R_{-,j}(M)=M^{2j}\nu_j,\qquad
                       \nu_j=(-1)^jq^{j(j+1)}.
 \tag{13}
\]
Thus this calculation uses the genuine meridian family, not an
interpolation of the root eigenvalues.

L's finite grid identity is
\[
 \mathcal S_N(Q^l,v;c)=\frac{(cv;Q)_l}{(c;Q)_l},
 \qquad 0\le l<N,\qquad
 A_N(M;k,z)=H_d(M)k^d\mathcal S_N(u,v;M^{-2}Q),
 \tag{14}
\]
where \(u+v=z/(qk)\), \(uv=(Qk^2)^{-1}\).
On (12), the two pairs for (6) can be chosen as
\[
 \begin{array}{c|cc|c}
 &u&v&c\\ \hline
 A_-&Q^{T-j}&M^4Q^{j-H}&M^2Q\\
 B_+&Q^{H+j}&M^{-4}Q^{H-j-1}&M^{-2}Q .
 \end{array}
 \tag{15}
\]
Both grid indices \(T-j\) and \(H+j\) are in \(0,\ldots,d\).
There is no noninteger factorial interpolation or choice of a
logarithm deck in this use of (14). The two scalar factors are
\[
 \frac{(M^6Q^{j-H+1};Q)_{T-j}}{(M^2Q;Q)_{T-j}},
 \qquad
 \frac{(M^{-6}Q^{H-j};Q)_{H+j}}{(M^{-2}Q;Q)_{H+j}}.
 \tag{16}
\]
Their Cartan prefactors cancel.

Put \(l=T-j\), \(k=j-H\). Reflect every factor in the first
numerator by \(1-z=-z(1-z^{-1})\), and do the same for its
denominator. The resulting numerator intervals, together with the
second numerator, cover a full \(Q\)-orbit except exponent \(2H\).
The denominator intervals cover precisely exponents \(1,\ldots,d\).
The lengths add to \(l+(H+j)=d\). Keeping the reflected powers gives
the exact product of (16):
\[
 M^{4l}Q^{lk}
 \frac{1-M^{-6N}}
 {(1-C^2M^{-6})(M^{-2}Q;Q)_d}.
 \tag{17}
\]
For example the numerator reflection exponent minus the denominator
reflection exponent is
\(l[(N+j-3H)-(l+1)]/2=l(j-H)=lk\).
This verifies the phase also when \(j-H<0\); the orbit, not a
positive-index interpolation, is what is being multiplied.

The exact finite lowering products satisfy
\[
 H_d(M)H_d(M^{-1})
       =(M^2Q;Q)_d(M^{-2}Q;Q)_d.
 \tag{18}
\]
Multiplying (17),(18) by (13) squared removes every channel index:
\[
          Q^{(T-j)(j-H)+j(j+1)}=Q^{H(H+1)}.
 \tag{19}
\]
This proves (9) in the generic eigenbasis. Both sides of (8) are
analytic matrices near \(M=1\); the crossing is invertible there.
Equality on the punctured generic set therefore proves the identity
at the root with all Jordan entries and every meridian derivative.
No condition number of the generic eigenbasis is used.

Finally
\[
 (M^2Q;Q)_d=M^dD_N(M),\qquad
 \frac{1-M^{-6N}}{1-C^2M^{-6}}
       =M^{-3d}C^{-1}D_N(M^3C^{-1}).
 \tag{20}
\]
Equations (9),(20) give (8).

For the original three-head opposite source, L records
\(a_N(M)=D_N(M)^3/N^2\). Thus
\[
 \Sigma_{N,H}(M)
 =a_N(M)D_N(M^3C^{-1})\,
       Q^{H^2}M^{2d-4H}\left(\frac N{D_N(M)}\right)^2.
 \tag{21}
\]
The last factor is an explicit holomorphic unit. Its root value is
\(Q^{H^2}\), and its logarithmic \(\mu\)-derivative at the root is
\(2d-4H\). It is not silently removed from a source finite part.
Equation (21) identifies the divisor of (8) with the actual
complementary-degree normalization.

## 3. The genuine dual first normal

Let \(A_0=A_-(1)\), \(B_0=B_+(1)\), \(\mathcal R_0=\mathcal R_-(1)\).
Let \(A_1\) be the positive-\(\mu\) derivative of the actual low-degree
Gauss family \(A_N(e^\mu)|_{V_T}\), and \(B_1=\partial_\mu B_+(e^\mu)|_0\).
Then \(A_-'(0)=-A_1\). Since \(\Sigma(1)=0\), (8) first gives
\[
                         A_0B_0=B_0A_0=0.
 \tag{22}
\]
Differentiating the entire analytic identity gives
\[
 \boxed{\quad
 A_0B_1-A_1B_0
     =\gamma_{N,H}\mathcal R_0^{-2},\qquad
 \gamma_{N,H}=\frac{6N^2Q^{H(H+1)}}{1-C^2}\ne0.
 \quad}
 \tag{23}
\]
The crossing derivative multiplies the zero product (22), which
is why it does not appear in (23). This is not omission of a
crossing normal before differentiation.

Writing \(D=L(1)^{-1}\partial_\mu L(e^\mu)|_0\), the actual
transported derivative is
\[
 B_1=L(1)^{-1}
        \left.\partial_\mu A_N(e^\mu)|_{V_{2d-T}}\right|_0L(1)
                           +[B_0,D].
 \tag{24}
\]
The moving turnover/Cartan frame is therefore retained. Neither
individual summand in (23) has been shown to commute with the root
Casimir; their sum does, by (23).

There are useful identities with no primary projector at all:
\[
 A_0B_1A_0=\gamma_{N,H}A_0\mathcal R_0^{-2},\qquad
 B_0A_1B_0=-\gamma_{N,H}B_0\mathcal R_0^{-2}.
 \tag{25}
\]
They follow by multiplying (23) and using (22). In particular the
dual first normal supplies an inverse on the corresponding filtered
piece, with its specified physical crossing factor.

For comparison with a moving primary resolution, if \(P(\mu)\)
is an upper-primary cluster for \(B_+\), L gives
\(B_+(\mu)P(\mu)=(1-e^{-6N\mu})G(\mu)P(\mu)\) with \(G\) invertible.
Here \(K_-^{-1}=M^2C^{-1}\) has L's required Cartan dependence,
and its norm relation with \(\Omega_-\) holds because that relation
is symmetric under \(K\mapsto K^{-1}\). Thus the reflected total
does not change the marked functional identity being applied.
Differentiation yields
\[
             B_1P(0)=6NG(0)P(0)-B_0P'(0).
 \tag{26}
\]
Thus the bare \(B_1\) need not preserve the root primary subspace.
Equations (23)--(25) retain or eliminate this current by actual
matrix multiplication, rather than assuming a bounded projector.

## 4. Exact insertion current and the analytic limit of the result

For every analytic matrix \(X(M)\) on the physical block, (8) gives
the exact ordered insertion identity
\[
 \boxed{\quad
 A_-X B_+\mathcal R_-^2
   =\Sigma_{N,H}X+[A_-,X]B_+\mathcal R_-^2 .
 \quad}                                                       \tag{27}
\]
Internal physical crossings commute with \(A_-\), so their insertion
has zero current. A general reduced braid need only preserve total
degree; R's opened-head triangular generator need not commute with
the tail Casimir. Its current in (27) must remain. The same applies
to relative coherent windows or other arbitrary marks.

All identities can be inserted between arbitrary exact finite
coherent resolutions: they are identities of the original capped
matrices. In particular the adjacent two-factor normal convolution
in (23) is exactly the kernel of
\(\gamma_{N,H}\mathcal R_0^{-2}\), with the original binomial duals.
It is the combined normal, not either individual normal kernel.

No uniform norm for a partial inverse of \(A_0\), a Riesz projector,
or a source-window current follows from (8). The root factors have
complementary zero channels, and (23) keeps both normal contributions.
A local nonzero coherent branch for \(A_0\) cannot be inverted on a
chosen original relative cycle using (8) alone. The exterior routing,
the insertion current (27), and all source finite parts must be
transported with that cycle before any such conclusion.
No geometric occurrence or closed-source lower bound is asserted.

## 5. The full-width fusion, including all highest multiplicities

Now allow every \(N\ge2\), with \(q,Q,d\) as above, fix \(r\ge2\),
\(m=r+1\), and an actual integer \(0\le T\le rd\).
There is no reduction of \(T\) modulo \(N\). Put
\[
 H=d-T,\qquad k_0=(-q^{-1})^rQ^{-T},\qquad
 \varepsilon=k_0^N=(-1)^{dr},\qquad K_-=M^{-r}k_0 .
 \tag{28}
\]
The two physical degrees are \(T\) and \(rd-T\). The same calculation
as (3)--(6), with
\[
 L_r(M)=\kappa(M)^{-r}D_{\rm top}(M)\mathscr C_r(M)
       =x_+^{-rd}t^{\mathsf n}\mathscr C_r(M),
 \tag{29}
\]
gives the exact families on \(U_T\)
\[
 A_-=A_N(M^{-1};K_-,\Omega_-),\qquad
 B_+=L_r^{-1}A_N(M)|_{U_{rd-T}}L_r
       =A_N(M;K_-^{-1},\Omega_-).
 \tag{30}
\]
In particular \(B_+\) is the literal complementary operator at
every meridian, not a root polynomial differentiated in a newly
chosen family.

Let \(\Delta_r\) be the positive half twist, and set
\[
 \Theta_-(M)=\kappa(M^{-1})^{-r(r-1)}
                    R_{\Delta_r^2}(M^{-1})|_{U_T}.
 \tag{31}
\]
This is the actual full twist, stripped of exactly its \(r(r-1)\)
common crossing scalars. W proves directly from the finite crossings
that on every generic highest string of exact integer degree \(j\),
including each multiplicity copy,
\[
                  \Theta_-(M)
                    =M^{2rj}Q^{j(j+r-1)}I .
 \tag{32}
\]
Its proof includes the finite block Euler identity: every term of
total transfer at least \(N\) in cabling a block past one head
vanishes because of that single head's actual \(N\)-th power.
No root carry or multiplicity action is suppressed.

The whole-width theorem is
\[
 \boxed{\quad
 A_-B_+\Theta_-=\Sigma_{r,T}(M)I_{U_T},\qquad
 \Sigma_{r,T}
 =\varepsilon k_0^{-1}Q^{T(T+r-1)}M^{r(2T-d)}
                         D_N(M)D_N(M^m k_0^{-1}).
 \quad}                                                       \tag{33}
\]
This identity is valid also at self-reciprocal \(k_0\), with the
Laurent-polynomial continuation of \(D_N\). The simple-zero normal
formulas below are restricted to \(k_0^2\ne1\).

We give the complete remaining finite calculation. W's generic
decomposition has highest multiplicities
\[
 \sum_j m_r(j)z^j=(1+z+\cdots+z^d)^{r-1}.
\]
Every highest string occupies exactly the integer degrees
\(j,j+1,\ldots,j+d\). Therefore every label present in \(U_T\)
satisfies
\[
             0\le l:=T-j\le d,\qquad d-l=H+j\in[0,d].
 \tag{34a}
\]
For completeness, in the initial range \(T\le d\) the same
decomposition can be seen without a projector theorem as follows.
If \(h\) is highest of degree \(j\), \(Kh=k_jh\), then
\[
 EF^n h=-q^{-1}(1-Q^n)
             (k_jQ^{1-n}-k_j^{-1})F^{n-1}h,\qquad
 k_j=x_-^rQ^{-j}.
 \tag{34}
\]
These coefficients are nonzero for \(1\le n<N\) at generic \(M\).
Inductively \(EF\) is invertible on \(U_{T-1}\), decomposed into
the previously constructed descendants. Hence
\(U_T=\ker E_T\oplus F U_{T-1}\): to split a vector \(v\), subtract
\(F(EF)^{-1}Ev\). The same nonzero coefficients give injectivity of
\(F\) there. This constructs all labels and every multiplicity.
Below degree \(N\) the individual upper caps do not alter these
spaces; the caps in the Gauss transfer polynomial remain intact.

For arbitrary physical \(T\), W's full generic decomposition supplies
all the strings in (34a), with their multiplicities and finite ends.
On a highest label \(j\), and all its descendants,
\[
 \Omega_- =z_j+z_j^{-1},\qquad
               z_j=(-1)^r q^{r-1}M^rQ^j .
 \tag{35}
\]
The labels in one fixed degree lie in the length-\(N\) integer interval
\([T-d,T]\), and hence contain no pair differing by \(N\). Their
values in (35) are distinct for generic \(M\).
Multiplicity within a label causes no problem:
both Gauss factors are functions of this Casimir, and (32) is
scalar on every copy.

For \(A_-\) the pair in (14) is
\(u=Q^{T-j}\), \(v=M^{2r}Q^{T+j+r-1}\).
For \(B_+\) one may choose
\(u=Q^{H+j}\), \(v=M^{-2r}Q^{-T-j-r}\).
Both grid indices are between zero and \(d\) by (34a), even when
\(H=d-T<0\). No factorial \(f_H\) is introduced. The exact
two Chu factors are therefore
\[
 \frac{(M^{2m}Q^{T+j+r};Q)_{T-j}}
      {(M^2Q;Q)_{T-j}},
 \qquad
 \frac{(M^{-2m}Q^{-T-j-r+1};Q)_{H+j}}
      {(M^{-2}Q;Q)_{H+j}} .
 \tag{36}
\]
Reflect the first numerator and denominator as in (17).
The reflected numerator interval starts at \(-2T-r+1\) and
ends just before the second numerator starts; together they
have length \(d\) and miss only the orbit exponent \(-2T-r\).
The denominators cover \(1,\ldots,d\).
The resulting product, including the two finite \(H_d\)'s, is
\[
 A_{-,j}B_{+,j}
 =M^{2r(T-j)}Q^{(T-j)(T+j+r-1)}(M^2Q;Q)_d
              \frac{1-M^{-2mN}}{1-k_0^2M^{-2m}}.
 \tag{37}
\]
In particular the exponent from reflecting the \(T-j\) factors
is
\((T-j)[(3T+j+2r-1)-(T-j+1)]/2
=(T-j)(T+j+r-1)\).
The quotient is the exact finite geometric polynomial
\[
 \frac{1-M^{-2mN}}{1-k_0^2M^{-2m}}
          =\sum_{a=0}^{N-1}k_0^{2a}M^{-2ma},
 \tag{38}
\]
so no new pole or infinite-series prescription occurs.

Multiplication by (32) cancels \(j\):
\[
 (T-j)(T+j+r-1)+j(j+r-1)=T(T+r-1).
 \]
This proves (33) on the complete generic decomposition, using
\[
 (M^2Q;Q)_d=M^dD_N(M),\qquad
 \frac{1-M^{-2mN}}{1-k_0^2M^{-2m}}
 =\varepsilon M^{-md}k_0^{-1}D_N(M^m k_0^{-1}).
 \tag{39}
\]
The finite analytic matrix identity extends through the root,
including every generalized primary and meridian jet.
Generic diagonalization is used only to prove equality, never
to estimate a matrix or to transport a norm.

The exact integer labels are material. In the full tensor product,
highest strings \(j\) and \(j+N\) can have the same Casimir throughout
the meridian family while their full-twist eigenvalues in (32)
differ by \(M^{2rN}\). They do not coexist in a single fixed degree,
by (34a). The proof keeps the integer \(j\) in the factor
\(M^{2r(T-j)}\) of (37) and in \(M^{2rj}\) of (32); these cancel
to the actual character \(M^{2rT}\). Neither \(j\) nor \(T\) has
been replaced by a residue modulo \(N\). Thus (33) is an all-degree
statement with its degree character retained, not an unmarked
Casimir identity on the full tensor product.

### The exact source unit and full normal

L gives
\[
 a_N(M)=(-1)^{d(m+1)}\frac{D_N(M)^m}{N^r}
                   =\varepsilon\frac{D_N(M)^m}{N^r}.
 \]
Thus (33) has the original source normalization
\[
 \Sigma_{r,T}
   =a_N(M)D_N(M^m k_0^{-1})\,\omega_{r,T,N}(M),\qquad
 \omega_{r,T,N}
  =k_0^{-1}Q^{T(T+r-1)}M^{r(2T-d)}
                     \left(\frac N{D_N(M)}\right)^r .
 \tag{40}
\]
The unit is explicit, with
\(\partial_\mu\log\omega|_0=r(2T-d)\).
It is uniformly a scalar unit on every scaled collar
\(M=e^{u/N}\), \(|u|\le\eta<\pi\), at fixed width:
\[
 \frac N{D_N(e^{u/N})}
          =\frac{N\sinh(u/N)}{\sinh u}.
 \tag{41}
\]
The removable value at zero is one, and the ratio and its inverse
are bounded on the stated compact disk. The other factor in (40)
has bounded modulus at fixed \(r\) because \(0\le T\le rd\).
Fixed \(\mu\)-derivatives consequently have polynomial \(N\)-cost.
This scalar statement says nothing about a matrix inverse norm.

For \(k_0^2\ne1\), define \(A_0,B_0,A_1,B_1\) as before, now
on \(U_T\), with the full \(L_r\) derivative in \(B_1\).
Then (33) gives
\[
 \boxed{\quad
 A_0B_0=0,\qquad
 A_0B_1-A_1B_0=\gamma_{r,T,N}\Theta_-(1)^{-1},\qquad
 \gamma_{r,T,N}
       =\frac{2mN^2Q^{T(T+r-1)}}{1-k_0^2}.
 \quad}                                                       \tag{42}
\]
Every moving frame and both actual first normals remain.
The two sandwich identities (25) hold with
\(\gamma_{r,T,N}\Theta_-(1)^{-1}\) in place of
\(\gamma_{N,H}\mathcal R_0^{-2}\).
If physical full twists are used, restore all
\(\kappa(M^{-1})^{r(r-1)}\) factors before differentiation.

For clarity the self-reciprocal blocks have a different root row.
When \(k_0^2=1\), the finite sum (38) equals \(N\) at the root, so
\[
 \Sigma_{r,T}(1)=N^2Q^{T(T+r-1)}\ne0,\qquad
 \partial_\mu\Sigma_{r,T}(e^\mu)|_0
                  =r(2T-d)\Sigma_{r,T}(1).
 \tag{42a}
\]
Both root Gauss factors are then invertible. If
\(\Theta_0=\Theta_-(1)\) and
\(\Theta_1=\partial_\mu\Theta_-(e^\mu)|_0\), differentiation gives
\[
 A_0B_1-A_1B_0
   =\Sigma_1\Theta_0^{-1}
            -\Sigma_0\Theta_0^{-1}\Theta_1\Theta_0^{-1}.
 \tag{42b}
\]
Here \(\Sigma_0,\Sigma_1\) are the value and derivative in (42a).
The full-twist normal is present; (42) is not applied to these
blocks. To check the scalar derivative in (42a), use (40):
both \(D_N(e^\mu)\) and \(D_N(e^{m\mu}k_0^{-1})\) have zero
first logarithmic derivative at zero when \(k_0=\pm1\).

For an arbitrary analytic mark \(X(M)\), the exact source current is
\[
 A_-XB_+\Theta_-
       =\Sigma_{r,T}X+[A_-,X]B_+\Theta_- .
 \tag{43}
\]
Equations (42),(43) describe an actual fused normal kernel and
its obstruction to an unrestricted exterior substitution.
They do not give a uniform inverse on a coherent window.
The original two opposite kernels, their braid/turnover routing,
Cartan normalization, and relative-cycle currents still have
to be retained in any closed-source application.

## Complete directs and coverage

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* L: notes/research_marked_gauss_functional_calculus.md,
  487 lines, SHA256
  7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* W: notes/research_actual_full_twist_highest_multiplicities.md,
  453 lines, SHA256
  2014de44e1ab880c61c6d1017d6f6a4bf3ed18cd6065e1fcf1fe84d1c8e7090f.

The earlier normal-lattice theorem gives a finite-level source
factorization and its graded inverse. The complementary boundary and
Fourier-band notes give root endpoint and range information. The
addition here consists of the whole-meridian Gauss-level identities (8),(33), their
explicit physical crossing and source unit, and the grouped actual
normal/current rows (23)--(27),(42),(43). No asymptotic inverse is imported.

Only written mathematics and text/hash operations are used. Frozen
and public files are unchanged. The entire matching final was read
nontruncated. Complete L, R, and W were freshly wholly read in this
active author/formal-review sequence; the complete matching G whole
read was retained fresh unchanged from the immediately preceding
complementary-boundary review. Every used implication was checked
and all five pins renewed. Independent matching review and root
adoption remain separate.
