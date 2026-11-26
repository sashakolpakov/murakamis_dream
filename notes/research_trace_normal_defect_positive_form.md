# Combining the first normals before estimating the trace

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

Splitting a trace at the triangular support of a Newton polynomial
separates terms that can cancel. There is an exact way to put them
back together. Interpolate the values of the other factor at the
distinct physical roots, and subtract the derivative of this
interpolant from its actual first normal. The trace then involves
only this normal difference and the nonzero values of the Newton
polynomial. No first normal is discarded.

At even levels the resulting crossing operator has a positive
Hermitian form. Its positivity follows from an explicit integral
representation of the original quadratic crossing phase. This
gives a positive observation with a specified adjoint cap; it does
not make the original same-sign pair contraction positive.

## 1. The interpolation identity at both parities

Set
\[
 \theta=\pi/N,\quad \eta=(-1)^{N-1},\quad
 L=\lfloor(N-1)/2\rfloor,\quad
 c_a=2\cos((2a+1)\theta),\qquad 0\le a\le L.
 \tag{1}
\]
These are the distinct physical roots of
\(P_N(z)=2T_N(z/2)+2\). All are double except \(c_L=-2\)
when \(N\) is odd. Put
\[
 A_a=4-c_a^2,\qquad
 \ell_a(z)=\prod_{b\ne a}\frac{z-c_b}{c_a-c_b},\qquad
 D_{ab}=\ell_b'(c_a),\qquad
 \lambda_a=[z^L]\ell_a(z)=\prod_{b\ne a}(c_a-c_b)^{-1}.
 \tag{2}
\]
The value interpolant is
\(I_Nh=\sum_a h(c_a)\ell_a\). This is not the full Hermite
representative: the first normals of \(h\) are kept separately.
At each double node define
\[
                    d_a(h)=h'(c_a)-(I_Nh)'(c_a).
 \tag{3}
\]
The functions \(h\) below need only have the indicated physical
values and first normals. Their original trace is
\[
 \phi(h)=\eta\sum_{\text{double }a}
       \{A_a h'(c_a)-c_a h(c_a)\}
       +\boldsymbol 1_{\{N\ {\rm odd}\}}h(-2).
 \tag{4}
\]
For a polynomial this is also
\(\eta N^2[z^{N-1}]\operatorname{rem}_{P_N}h\).
These are the full trace conventions of the
[exact derivative-sampling formula](research_exact_complete_trace_contour.md).

**Theorem 1.** For every polynomial \(p\) of degree at most \(L\),
\[
 \boxed{\quad
 \phi(hp)=\eta\sum_{\text{double }a}A_a d_a(h)p(c_a)
   +\boldsymbol 1_{\{N\ {\rm odd}\}}
       N^2[z^L](I_Nh)\,[z^L]p .
 \quad}
 \tag{5}
\]
In particular, with
\[
 e_j(z)=S_j^{-2}\prod_{b<j}(c_b-z),\qquad
 S_j=\prod_{b=1}^j2\sin(b\theta),\qquad 0\le j\le L,
\]
the sum in (5) contains only \(a\ge j\). At odd levels its
additional term vanishes unless \(j=L\), when it equals
\[
             N^2\frac{(-1)^L}{S_L^2}
                   \sum_a\lambda_a h(c_a).
 \tag{6}
\]
This includes the odd simple endpoint without assigning a first
normal to it.

**Proof.** The function \(h-I_Nh\) vanishes at every distinct
physical root. Thus in the trace of \((h-I_Nh)p\) only its first
normal at the double roots survives, giving the sum in (5).
For even \(N=2m\), the polynomial \((I_Nh)p\) has degree at most
\(2m-2=N-2\), so its trace is zero. For odd \(N=2m+1\), its
degree is at most \(2m=N-1\); its trace is exactly \(N^2\)
times the product of the two leading coefficients. Finally
\(e_j(c_a)=0\) for \(a<j\), and its leading coefficient in
degree \(L\) is zero unless \(j=L\). \(\square\)

For the pair source take
\[
 h=R^n\mathcal L_N,\qquad
 \mathcal L_N(z)=\sum_{k=0}^{L}e_k(z)e_k(-2).
 \tag{7}
\]
Then (5) is an identity for the complete original coefficient
\(W_{n,j}=\phi(R^n\mathcal L_Ne_j)\). It combines the
[first-normal-only rows](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_pair_triangular_normal_region.md)
with the other trace terms before taking absolute values.
It does not estimate their separate sums.

## 2. An explicit commutator for the original crossing

Let \(l\) be any polynomial of degree at most \(L\), and write
\(F_a=l(c_a)\). The crossing values and normals are
\[
 r_a=C_{N,n}\exp(i\varphi(c_a)),\qquad
 C_{N,n}=\exp\frac{\pi i n(N-1)^2}{4N},\qquad
 \varphi(z)=\frac{nN}{4\pi}\tau(z)^2,\quad
 \tau(z)=\arccos(-z/2).
 \tag{8}
\]
At every double node \(R^n{}'(c_a)=i\varphi'(c_a)r_a\).
Here \(n\) can be any real number for the stated Hermite data;
integer \(n\) gives the original algebra power. The square
\(\tau(z)^2\) is analytic at \(z=-2\). Its derivative there is
one, but the odd trace does not use that derivative.

Writing \(R=\operatorname{diag}(r_a)\), the double-node normal
difference is the corresponding component of
\[
 d(R^nl)=\{\operatorname{diag}(i\varphi'(c_a)r_a)
                         +[R,D]\}F.
 \tag{9}
\]
Indeed \(l'=DF\) on the nodes, while
\((I_N(R^nl))'=DRF\). Formula (9) therefore uses the actual
first normals of the crossing and of \(l\).

For clarity, the full odd-level correction can be written without
any reference to an omitted endpoint. If \(N\) is odd, then
\[
 \phi(R^nlp)
   =p_{\rm val}^{\,T}A
       \{\operatorname{diag}(i\varphi' r)+[R,D]\}F
        +N^2(\lambda^TRF)(\lambda^Tp_{\rm val}),
 \tag{10}
\]
where \(A=\operatorname{diag}(A_a)\), so \(A_L=0\), and
\(p_{\rm val}=(p(c_a))_a\). This is an exact odd-level formula,
not an extension of the even-level positivity assertion below.

## 3. The even-level operator is positive

Assume \(N=2m\), so \(L=m-1\). Put
\[
 \sigma_a=2(-1)^a\sin((2a+1)\theta),\qquad
 B=AD-\tfrac12\operatorname{diag}(c_a).
 \tag{11}
\]
The Chebyshev cardinal derivatives give
\[
 B_{aa}=0,\qquad
 B_{ab}=\frac{\sigma_a\sigma_b}{c_a-c_b}\quad(a\ne b).
 \tag{12}
\]
Thus \(B\) is real and skew-symmetric. One way to check the
diagonal is to use the differential equation for \(T_m(z/2)\):
at a root, \(D_{aa}=c_a/(2A_a)\). Off the diagonal the
barycentric weights are a common multiple of \(\sigma_a\).

Define
\[
 H_{n,N}
   =A\operatorname{diag}(\varphi'(c_a))
                      +\frac{B-R^*BR}{i}.
 \tag{13}
\]
Since \(|r_a|=1\), this is Hermitian. The original trace satisfies
the exact identity
\[
 \boxed{\qquad
       \phi(R^nlp)=i\eta\,p_{\rm val}^{\,T}R H_{n,N}F .
       \qquad}
 \tag{14}
\]
Indeed multiplication of (9) by \(R^*A\) gives \(iH_{n,N}F\);
the diagonal part of \(AD\) commutes with \(R\). Applying (5)
proves (14).

**Theorem 2.** For every even \(N\ge2\) and every real \(n>0\),
the matrix \(H_{n,N}\) is positive definite. For \(n<0\) it is
negative definite, and it is zero for \(n=0\).

**Proof.** Its off-diagonal entries are
\[
 (H_{n,N})_{ab}
   =\sigma_a\sigma_b
      \frac{1-\exp(i(\varphi(c_b)-\varphi(c_a)))}
           {i(c_a-c_b)} .
 \tag{15}
\]
The diagonal is \(\sigma_a^2\varphi'(c_a)\), which equals
\(nN\tau(c_a)\sin\tau(c_a)/\pi\).
Remove the unitary half-phase factors in (15). The resulting
real symmetric matrix is
\[
 S_{ab}=\sigma_a\sigma_b
       \frac{2\sin((\varphi(c_a)-\varphi(c_b))/2)}
            {c_a-c_b},\qquad
 S_{aa}=\sigma_a^2\varphi'(c_a).
 \tag{16}
\]
To verify its sign directly, the original phase has the
divided-difference representation
\[
 \frac{\varphi(x)-\varphi(y)}{x-y}
   =\frac{nN}{2\pi}\int_2^\infty
      \frac{\operatorname{arcosh}(s/2)}
           {(s-x)(s-y)}\,ds,\qquad -2<x,y<2.
 \tag{17}
\]
The diagonal is the continuous limit. For example, the analytic
function \(\tau(z)^2\) on \(\mathbb C\setminus[2,\infty)\)
vanishes at \(-2\), grows like \(O(\log^2|z|)\), and has
upper-cut imaginary part \(2\pi\operatorname{arcosh}(s/2)\).
The Cauchy formula with one subtraction at \(-2\) gives
\[
 \tau(z)^2=2(z+2)\int_2^\infty
    \frac{\operatorname{arcosh}(s/2)}{(s+2)(s-z)}\,ds.
 \tag{18}
\]
Taking the divided difference proves (17). The integral also
gives \((\tau^2)'(-2)=1\), fixing its normalization.

The identity
\(\int_{-1/2}^{1/2}e^{iu(\varphi(x)-\varphi(y))}\,du
 =2\sin((\varphi(x)-\varphi(y))/2)/(\varphi(x)-\varphi(y))\)
now expresses the quadratic form of \(S\), up to replacing \(u\)
by \(-u\), as
\[
 v^*Sv=\frac{nN}{2\pi}\int_2^\infty
     \operatorname{arcosh}(s/2)
       \int_{-1/2}^{1/2}
       \left|\sum_a
          \frac{\sigma_a v_a e^{iu\varphi(c_a)}}{s-c_a}
       \right|^2du\,ds .
 \tag{19}
\]
It is nonnegative for \(n>0\). If it is zero, continuity makes
the displayed rational function zero for all \(s>2\) and all
interior \(u\). Its residues at the distinct poles \(c_a\)
are zero. Every \(\sigma_a\ne0\), so \(v=0\).
This proves positive definiteness. Negative \(n\) reverses the
sign in (19), while changing only its unit phase factors.
For \(n=0\), (13) is zero. \(\square\)

Equivalently, \(\exp(i\varphi(z))\) is a Schur function in the
upper half-plane: \(\tau(z)\) has real part in \((0,\pi)\)
and positive imaginary part there. The matrix in (15) is its
boundary Pick kernel, with the explicit original-node weights.
The integral proof above supplies the needed positivity without
assuming a spectral property of a comparison model.

## 4. What this does and does not prove for the coefficient

There is an actual positive observation. Choose the unique
polynomial \(p\) of degree at most \(L\) with values
\[
                       p(c_a)=r_a^{-1}\overline{F_a}.
 \tag{20}
\]
Then at even levels,
\[
                \frac{\phi(R^nlp)}{i\eta}=F^*H_{n,N}F>0
                    \quad(n>0,\ l\ne0).
 \tag{21}
\]
Thus the positive form comes from the original crossing and trace,
with a precisely specified adjoint cap. Its smallest eigenvalue
has not been bounded on the exponential scale in this note.

For the original pair, \(l=\mathcal L_N\) and \(p=e_j\);
the cap in (20) is not inserted. In particular,
\[
 W_{n,j}=i\eta\,e_j(c)^{\,T}R H_{n,N}F,\qquad
 \sum_{j=0}^{L}W_{n,j}W_{p,j}
   =-F^TH_{n,N}^{T}R_n K^{\rm low}_{\rm phys}
                           R_pH_{p,N}F
 \tag{22}
\]
at even levels, where
\(K^{\rm low}_{\rm phys}(a,b)=\sum_{j=0}^{L}e_j(c_a)e_j(c_b)\).
The two phases and the bilinear, rather than Hermitian, pairing
are retained. Positivity of \(H_{n,N}\) does not alone give a
lower bound for (22).

At odd levels use (10), including its rank-one correction, before
forming the pair contraction. At both parities (5) has removed the
artificial boundary \(a=j-1\) from the value support of the trace.
Estimating the resulting normal differences, or their coherent
contraction, remains necessary. No bound for a separately split
normal--normal or mixed region follows by taking absolute values
in this identity.

Reflection supplies a positive norm for a different original word:
the exact reality relations give
\(W_{-n,j}=\overline{W_{n,j}}\), so the reflected pair is
\(\sum_j|W_{n,j}|^2\), whereas the same-sign pair is
\(\sum_jW_{n,j}^2\). This distinction can matter exponentially.
For the full original internal-pair vectors, the
[proved long-power comparison](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_complete_boundary_coefficient_transport.md#7-exponentially-small-coherence-in-an-actual-long-power-family),
Theorem 2, gives
\[
 \frac{|w_n^Tw_n|}{\|w_n\|_2^2}
   =C_ne^{-N\Delta_n}(1+O(N^{-1})),\qquad
 \Delta_n=\frac{16\pi^3}{n^6}+O(n^{-7})>0
\]
for every sufficiently large fixed positive integer \(n\).
This is a result about those full original vectors; it is not
silently transferred to the low-index vector in (22).
It rules out using reflection as a general norm-preserving
substitute for the signed closing observation. The positive form
in this note still requires its specified cap or a separate
estimate of the actual cap's observation.

## 5. A positive weighted subspace at odd levels

The full odd-level formula is (10). There is also an exact
positive form on a smaller, explicitly weighted space; it does
not replace (10).

Let \(N=2m+1\ge3\), and let \(c_0,\ldots,c_{m-1}\) be its
double roots. Write
\[
 P_N(z)=(z+2)Q_N(z)^2,\qquad
 Q_N(z)=\prod_{a=0}^{m-1}(z-c_a).
 \tag{23}
\]
For this section, \(D^+\) is the cardinal differentiation matrix
on these \(m\) nodes only. Define
\[
 A_a^+=(c_a+2)(4-c_a^2),\qquad
 v_a=4-2c_a^2-2c_a,\qquad
 \sigma_a^+=\frac{N}{Q_N'(c_a)}.
 \tag{24}
\]
The original weighted trace is
\[
 \phi_+(f):=\phi((z+2)f)
             =\sum_{a=0}^{m-1}\{A_a^+f'(c_a)+v_af(c_a)\}.
 \tag{25}
\]
The simple endpoint contributes zero because of the actual factor
\(z+2\), not because its trace value has been omitted.

Put
\[
 B^+=A^+D^++\tfrac12\operatorname{diag}(v_a),\qquad
 H_{n,N}^+=A^+\operatorname{diag}(\varphi'(c_a))
                         +\frac{B^+-R^*B^+R}{i},
 \tag{26}
\]
where \(R\) and \(\varphi\) are (8), restricted to the double nodes.

**Theorem 3.** If \(l,p\) have degree at most \(m-1\), and
\(F_a=l(c_a)\), then
\[
 \boxed{\qquad
     \phi((z+2)R^nlp)=i\,p(c)^{T}R H_{n,N}^+F .
     \qquad}
 \tag{27}
\]
For every real \(n>0\), \(H_{n,N}^+\) is positive definite;
for \(n<0\) it is negative definite. In particular, choosing the
unique \(p\) of degree at most \(m-1\) with
\(p(c_a)=r_a^{-1}\overline{F_a}\) gives
\[
              \phi((z+2)R^nlp)/i=F^*H_{n,N}^+F>0
                        \quad(n>0,\ l\ne0).
 \tag{28}
\]

**Proof.** The Chebyshev differential equation, evaluated at
a double root, gives
\((4-c_a^2)P_N''(c_a)=2N^2\). Differentiating (23) twice gives
\(P_N''(c_a)=2(c_a+2)Q_N'(c_a)^2\). Consequently
\[
                      A_a^+=(\sigma_a^+)^2.
 \tag{29}
\]
For any \(l,p\) of degree at most \(m-1\), the polynomial
\((z+2)lp\) has degree at most \(2m-1=N-2\), so its original
trace is zero. Expanding (25) for this product, whose two value
vectors are arbitrary, proves
\[
          A^+D^++(D^+)^TA^++\operatorname{diag}(v_a)=0.
 \tag{30}
\]
It follows that \(B^+\) is skew-symmetric. Its off-diagonal
entry is \(\sigma_a^+\sigma_b^+/(c_a-c_b)\), by the cardinal
derivative formula and (29).

Interpolate \(R^nl\) on the double nodes by a polynomial of degree
at most \(m-1\). Its product with \(p\) has zero weighted trace
by the same degree argument. Subtracting this interpolant gives
the weighted version of (9). Multiplying by \(R^*A^+\) yields
\(iH_{n,N}^+F\), proving (27).

The half-phase gauge of \(H_{n,N}^+\) has exactly the kernel
(16), with \(\sigma_a\) replaced by \(\sigma_a^+\).
All these weights are nonzero. The positive integral (19)
therefore proves strict definiteness with the asserted sign.
Finally (28) is the stated adjoint choice in (27). \(\square\)

The extra factor and the degree restriction in (27) matter.
The unrestricted low complete-end polynomial has degree \(m\)
at odd levels, and the original pair is not replaced here by a
weighted contraction. Its endpoint and top coefficient remain
as in (10).

## 6. Exact transport through ordinary value observations

The positive matrix is an observability Gramian for a specified
unitary evolution. Both its energy and the original signed trace
can be expressed using ordinary value interpolation. This removes
the first normals from the representation without dropping their
contribution.

First let \(N=2m\) and retain the \(m\) even-level nodes. Put
\[
 T_a=\frac{N}{4\pi}\tau(c_a)^2,\qquad
 U_t=\operatorname{diag}(e^{itT_a}),\qquad
 Q(z)=\prod_{a=0}^{m-1}(z-c_a)=2T_m(z/2).
 \tag{31}
\]
Thus the original crossing values are \(R_t=C_{N,t}U_t\).
The scalar \(C_{N,t}\) is kept in the signed trace; it cancels
in unitary conjugations. Define the positive matrix
\[
 G_{ab}=\sigma_a\sigma_b
            \frac{T_a-T_b}{c_a-c_b},\qquad
 G_{aa}=\sigma_a^2 T'(c_a).
 \tag{32}
\]
Its positive integral representation is (17) with \(n=1\).

For a physical value vector \(F\), let \(I_tF\) be the polynomial
of degree at most \(m-1\) whose values are
\[
                         (I_tF)(c_a)=e^{itT_a}F_a.
 \tag{33}
\]
When \(F=p(c)\), write \(I_t(p)\) for this same polynomial.
This specifies its exact representative. The interpolation does
not assume that the crossing phase is a polynomial off the grid.
For real \(s>2\) define the observation
\[
 (\mathcal O_tF)(s)=\sum_a
          \frac{\sigma_a e^{itT_a}F_a}{s-c_a}
                 =N\,\frac{(I_tF)(s)}{Q(s)}.
 \tag{34}
\]
The equality follows from the Lagrange partial fractions and
\(\sigma_a=N/Q'(c_a)\).

**Theorem 4.** For every real \(n\ge0\),
\[
 \boxed{\quad
 H_{n,N}=\int_0^n U_t^*G U_t\,dt,\qquad
 H_{n+p,N}=H_{n,N}+U_n^*H_{p,N}U_n\quad(p\ge0).
 \quad}
 \tag{35}
\]
Consequently
\[
 F^*H_{n,N}F
   =\frac{N}{2\pi}\int_0^n\int_2^\infty
        \operatorname{arcosh}(s/2)
               |(\mathcal O_tF)(s)|^2\,ds\,dt
 \tag{36}
\]
is strictly increasing in \(n\) for \(F\ne0\). For the specified
complete-end source \(F_a=\mathcal L_N(c_a)\), this is the
fully determined positive integral
\[
 F^*H_{n,N}F
   =\frac{N^3}{2\pi}\int_0^n\int_2^\infty
      \operatorname{arcosh}(s/2)
       \left|\frac{I_t(\mathcal L_N)(s)}{Q(s)}\right|^2
           ds\,dt .
 \tag{37}
\]
No source amplitude or overlap is inserted as a hypothesis.

For the original signed trace, for any \(l,p\) of degree at most
\(m-1\), one has instead the bilinear identity
\[
 \boxed{\quad
 \phi(R^nlp)=
   \frac{i\eta C_{N,n}N^3}{2\pi}
       \int_0^n\int_2^\infty
        \operatorname{arcosh}(s/2)
        \frac{I_{n-t}(p)(s)\,I_t(l)(s)}{Q(s)^2}\,ds\,dt .
 \quad}
 \tag{38}
\]
This includes \(l=\mathcal L_N\) and every original low
Newton coefficient \(p=e_j\). There is no remaining first-normal
term or separately omitted row below \(a=j\) in (38).

**Proof.** Differentiating (15), with \(\varphi(c_a)=nT_a\),
gives
\[
                   \frac{d}{dn}H_{n,N}=U_n^*G U_n,
                         \qquad H_{0,N}=0.
 \tag{39}
\]
The diagonal follows by the same differentiation. Integration
proves the first equality in (35). Split its integral at \(n\)
and use \(U_{n+t}=U_nU_t\) to obtain the second. The positive
integral for \(G\) then proves (36); (34) gives (37).
For each \(t\), \(I_tF\) is nonzero when \(F\ne0\), so its
positive weighted squared integral on \(s>2\) is strictly positive.
All integrals converge: the rational observation is \(O(s^{-1})\)
at infinity and has no pole on \([2,\infty)\).

For the signed observation, multiply the first equality in (35)
by \(U_n\), obtaining
\[
                    U_nH_{n,N}
                      =\int_0^n U_{n-t}G U_t\,dt .
 \tag{40}
\]
Substitute this in (14), with \(R_n=C_{N,n}U_n\).
The Gram representation of \(G\) turns the two vectors into
their Cauchy sums (34). In this bilinear product no complex
conjugation is introduced. This proves (38). \(\square\)

There is an exact odd-level counterpart on the weighted space of
Theorem 3. Use its \(m\) double nodes, \(Q=Q_N\) from (23),
and \(\sigma^+=N/Q'\). Equations (31)--(37) then hold for
\(H^+_{n,N}\), with inputs of degree at most \(m-1\).
Equation (38) has \(\phi((z+2)R^nlp)\) on its left and
\(\eta=1\) on its right. The proof is identical, including the
factor \(N^3/(2\pi)\). The unrestricted odd source still uses
(10).

The two formulas (37) and (38) distinguish the remaining issue.
The first integrates nonnegative quantities and has a monotone
transport law. The second is the actual trace, and multiplies
observations at the complementary times \(t\) and \(n-t\)
without conjugation. A lower bound for that integral needs
control of those observations together. Neither a lower bound
for the positive energy alone nor the invertibility of the
finite crossing form supplies it.

There is a useful exact timescale for observing every channel.
It is proportional to the level, not a fixed crossing power.

**Corollary 5.** At even levels,
\[
 H_{N,N}=N\operatorname{diag}(G)\ \ge 2I,\qquad
 H_{n+N,N}=H_{n,N}+N\operatorname{diag}(G)\quad(n\ge0).
 \tag{41}
\]
On the odd weighted space of Theorem 3,
\[
 H^+_{2N,N}=2N\operatorname{diag}(G^+)
                  \ \ge\frac{128}{N^2}I,\qquad
 H^+_{n+2N,N}=H^+_{n,N}+2N\operatorname{diag}(G^+).
 \tag{42}
\]
Here \(G^+\) is (32) with the odd double nodes and weights
\(\sigma^+\).

**Proof.** At even levels, reverse the node order and write
\[
 \tau_b=(2b+1)\pi/N,\qquad
 T_b=\frac{\pi(2b+1)^2}{4N},\qquad 0\le b<N/2.
 \tag{43}
\]
The distinct differences \(T_b-T_c\) are nonzero integer
multiples of \(2\pi/N\): the integer \((b-c)(b+c+1)\)
is even. Thus integration over \(0\le t\le N\) in (35)
kills every off-diagonal entry. The diagonal of \(G\) is
\[
                  G_{aa}=\frac{N}{\pi}\tau_a\sin\tau_a.
 \tag{44}
\]
Both \(\tau_a\) and \(\pi-\tau_a\) are at least \(\pi/N\).
The inequality \(\sin x\ge2\min(x,\pi-x)/\pi\) gives
\(NG_{aa}\ge2\). The second equality in (41) follows from
the cocycle because the resulting diagonal commutes with \(U_n\).

At odd levels the double-node angles are
\(\tau_b=2\pi b/N\), \(1\le b\le(N-1)/2\).
Their frequencies are \(T_b=\pi b^2/N\), so their distinct
differences integrate to zero over \(0\le t\le2N\).
Now
\(G^+_{aa}=N(c_a+2)\tau_a\sin\tau_a/\pi\).
The bounds
\(c_a+2=4\sin^2(\tau_a/2)\ge16/N^2\),
\(\tau_a\ge2\pi/N\), and \(\sin\tau_a\ge2/N\)
give \(2NG^+_{aa}\ge128/N^2\).
The cocycle again proves the translated identity. \(\square\)

This supplies a polynomially coercive observation of the original
value space over the full crossing period, with its appropriate
odd weighted interpretation. It does not supply the corresponding
bound on a fixed time interval: the
[small-eigenvalue theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_pick_form_small_eigenvalues.md)
gives exponentially small directions for every fixed positive
power as \(N\) grows. Taking \(n=N\) or \(n=2N\) changes the
crossing power with the quantum level and therefore is not a
volume-conjecture statement for a fixed knot. Nor does a
positive energy replace the bilinear observation in (38).
The averaging in (41) is the continuous crossing flow (35).
At even levels \(R^N\) has scalar physical values, but its first
normals need not vanish: after dividing by that scalar, it is
\(1+r\) with \(r\) in the radical of the full double-root algebra
and \(r^2=0\). The nonzero matrix \(H_{N,N}\) retains precisely
this normal contribution. Finite-level nilpotence therefore
coexists with the observation problem at fixed crossing power.

## 7. Reproduction

Run
\[
 \texttt{python3 experiments/check\_trace\_normal\_defect\_positive\_form.py}.
\]
The checker compares the original value-and-normal trace with
(5), (9), (10), and (14) at both parities, including the top odd
Newton index. It also checks the even cardinal identities and
the normalized Gram kernel, the weighted odd trace (27), and
the exact transport and interpolation identities (34)--(40), and
the frequency and diagonal identities in (41)--(44). Its
[saved record](../repro/results/research-trace-normal-defect-positive-form.json)
records the source hashes. These finite checks supplement the
proofs above; no numerical eigenvalue test is used as a proof of
positivity.
