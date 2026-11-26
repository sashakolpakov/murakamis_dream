# An exact Gamma section and affine extension of the original crossing source

22 November 2026. Written research proof.
Earlier author-final notes and public manuscripts remain unchanged.

The original crossing source has an exact canonical Gamma solution of
its homogeneous boundary equation. The physical polynomial period is a
different, explicitly sourced solution: its first-order defect is a
known polynomial in the cyclic boundary characters. Keeping that defect
gives a flat affine extension and its full cyclic monodromy. It does not
identify the physical period with the Gamma section.

The constructions below concern solution and source channels over a
boundary-parameter difference field. They do not replace an original
Conway leg by a two-dimensional vector space.

## 1. The original scalar and canonical factorial

Fix
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\quad Q=q^2,
 \quad \eta=(-1)^d,\quad \kappa=e^{\pi i d^2/(2N)}.
 \tag{1}
\]
Every fractional power of \(q\) means the displayed exponential.
Use the complete Frobenius algebra and centered basis of [B], with
\(U_x=\sum_{j=0}^d x^j f_j\), \(R^+=\sqrt N f_0\), and the
original closing \(\phi\). In particular, all first spectral normals
at repeated Casimir roots are retained. Set
\[
 \Phi(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K})
            =N^{-1/2}\phi(R^+U_{-C}U_{-H}U_{-K}),\qquad r=HK.
 \tag{2}
\]
The level \(N\) is fixed in algebraic identities unless stated
otherwise. The function \(\Phi\) is the original polynomial, of
degree at most \(d\) separately in \(C,H,K\), and is symmetric in
these three variables. No scalar closing is replaced by a norm.

Let \(\mathfrak F=\mathfrak F_N\) be the canonical factorial of
[F]. Its identities needed here are
\[
 \begin{gathered}
 \mathfrak F(j)=(Q;Q)_j\quad(0\le j<N),\qquad
 \mathfrak F(w+1)=(1-Q^{w+1})\mathfrak F(w),\\
 \mathfrak F(w)\mathfrak F(d-w)=Nq^{w(w-d)},\qquad
 \mathfrak F(w+N)=(1-e^{2\pi iw})\mathfrak F(w).
 \end{gathered}
 \tag{3}
\]
The whole meromorphic identities, with their canonical logarithmic
marks, are used; singular factors are canceled before specialization.
Write
\[
 C=e^{-2\pi ic},\qquad H=e^{-2\pi ih},\qquad K=e^{-2\pi ik}
 \tag{4}
\]
on the angle cover, and define
\[
 \boxed{\quad
 G_N(c,h,k)=\frac{\kappa^2}{N^2}
  \frac{\displaystyle\prod_{a\in\{c,h,k\}}
                 \mathfrak F(N(1-a)-\tfrac12)^2}
       {\displaystyle\prod_{\{a,b\}\subset\{c,h,k\}}
                 \mathfrak F(N(1-a-b))}.\quad}
 \tag{5}
\]
The products count labelled singles and pairs, even when numerical
angles coincide. This is an explicit symmetric meromorphic section
on the marked cover, not a prescribed periodic function of \(C,H,K\).

## 2. Its exact shift and homogeneous boundary equation

Let
\[
 \sigma(C,H,K)=(C,H/Q,QK),\qquad
             (\sigma h,\sigma k)=(h+N^{-1},k-N^{-1}).
 \tag{6}
\]
Single steps in (3), with every phase retained, give
\[
 \boxed{\qquad
 \sigma G_N=g\,G_N,\qquad
 g=\frac{(1-qK)^2(1-CH)}{(1-H/q)^2(1-QCK)}.
 \qquad}
 \tag{7}
\]
For example, increasing \(h\) lowers its single factorial argument
by one, producing \((1-H/q)^{-2}\). Decreasing \(k\) produces
\((1-qK)^2\); the two changed pair denominators supply the other
two factors in (7).

The original polynomial equation [B], at its first coherent parameter
zero, is
\[
 D\,\sigma\Phi-(B+D+Q-1)\Phi+B\,\sigma^{-1}\Phi=0,
 \tag{8}
\]
where
\[
 B=\frac{(q-K)^2(1-QCH)}{(H-K)(QH-K)},\qquad
 D=\frac{(q-H)^2(1-QCK)}{(H-QK)(H-K)}.
 \tag{9}
\]
Here \(\sigma\) is the forward shift; it is the inverse of the shift
called \(\sigma\) in [B]. Initially (8)--(9) are read off their
denominator locus, and then as the cleared polynomial identity.

We verify directly that \(G_N\) solves (8). Put
\[
 F_q(X,Y)=2q-X-QY+QC(XY-1).
 \tag{10}
\]
The elementary polynomial factorization
\[
 Q(1-qY)^2(1-CX)-(q-X)^2(1-QCY)
                         =(X-QY)F_q(X,Y)
 \tag{11}
\]
follows by separating its constant and linear terms in \(C\).
The former are \((X-QY)(2q-X-QY)\); the latter are
\(QC(X-QY)(XY-1)\). Direct cancellation using (7) now gives
\[
 \begin{split}
 Dg-D&=\frac{F_q(H,K)}{H-K},\\
 B/(\sigma^{-1}g)-B&=-\frac{F_q(K,H)}{H-K}.
 \end{split}
 \tag{12}
\]
Since \(F_q(H,K)-F_q(K,H)=(Q-1)(H-K)\), their sum is
\(Q-1\). This proves
\[
             Dg+B/(\sigma^{-1}g)=B+D+Q-1,
 \tag{13}
\]
and hence the exact homogeneous equation for the Gamma section.
This proof does not infer an exact equation from a classical symbol
or from an asymptotic expansion.

## 3. The initialized Gamma value and its analytic branch

At \(h=1/(2N)\), put \(R=h+k\), \(p=NR\), \(L=N-p\), and
\[
 B_* =N(1-c)-\tfrac12,\qquad
 D_* =N(1-c-R)+\tfrac12.
\]
The single factorial for \(h\) is \(\mathfrak F(d)=N\), and the
three pair arguments are \(B_*,D_*,L\). Thus (5) gives exactly
\[
 G_N(c,\tfrac1{2N},R-\tfrac1{2N})
            =\frac{\kappa^2\mathfrak F(B_*)\mathfrak F(L)}
                         {\mathfrak F(D_*)}.
 \tag{14}
\]
This is the initialized Gamma term \(\mathcal G_1^0\) of [P]. The
actual source there is
\(\Phi_1^0=\mathcal G_1^0+I_1^0\), with its retained vertical
current \(I_1^0\), not simply \(G_N\). The same source also has the
exact readout
\[
 \Phi_1^0=\kappa\sqrt N\,\mathcal C_N(0,-C,-qr),
                         \qquad r=e^{-2\pi iR}.
 \tag{15}
\]
Consequently (14) retains the original \(\kappa^2\) normalization
and the actual source anchor, while leaving its correction visible.

For completeness, the canonical factorial also specifies the Gamma
section on complex shape charts. Suppose the angles lie in a fixed
complex compact set with
\[
 0<\Re a<1,\qquad 0<\Re(a+b)<1
       \quad(a,b\in\{c,h,k\},\ a\ne b\text{ as labels}).
 \tag{16}
\]
Keep positive margins in these inequalities. All nine arguments in
(5) lie in the full nonzero strips of [F]. Its uniform formula is
\[
 \mathfrak F(Nw+\tau)=\sqrt N\,\mathfrak h(w)
 (1-e^{2\pi iw})^\tau e^{N\mathfrak f(w)}(1+O(N^{-1})),
 \tag{17}
\]
where
\(\mathfrak h(w)^2=i(1-e^{2\pi iw})\) and
\(\mathfrak f(w)=-i\pi/12+i\operatorname{Li}_2(e^{2\pi iw})/(2\pi)\),
on the canonical strip branches. Applying this to (5) proves an
asymptotic for the Gamma section itself:
\[
 \begin{gathered}
 G_N=\kappa^2N^{-1/2}\mathcal B(c,h,k)
                        e^{N\mathcal S(c,h,k)}(1+O(N^{-1})),\\
 \mathcal S=\frac{\sum_{\{a,b\}}\operatorname{Li}_2(e^{-2\pi i(a+b)})
                 -2\sum_a\operatorname{Li}_2(e^{-2\pi ia})
                 +3\operatorname{Li}_2(1)}{2\pi i},\\
 \mathcal B=\frac{-i}{\displaystyle\prod_{\{a,b\}}
                          \mathfrak h(1-a-b)}.
 \end{gathered}
 \tag{18}
\]
Indeed each squared single factorial, including its shift \(-1/2\),
contributes the amplitude \(i\); the denominator contributes its
three \(\mathfrak h\)'s. The net power of \(N\), including
\(N^{-2}\), is \(N^{-1/2}\). The constant in the exponent is
\(+3\operatorname{Li}_2(1)\) in the numerator of (18).

On real positive angles with \(c+h+k<1\), the amplitude is
\[
 \mathcal B=
 \frac{e^{\pi i(c+h+k)}}
  {2\sqrt{2\sin\pi(c+h)\sin\pi(c+k)\sin\pi(h+k)}}.
 \tag{19}
\]
This follows from
\(\mathfrak h(1-u)=i e^{-\pi iu/2}\sqrt{2\sin\pi u}\).
Formula (18) is a holomorphic statement for the specified Gamma
section. It is not, by itself, a holomorphic asymptotic for the
physical scalar \(\Phi\).

## 4. Exact affine forcing of the physical polynomial

The homogeneous solution gives an elementary factorization, but the
inhomogeneous term is fixed by the original source. Define
\[
 F(C,H,K)=\frac{H-QK}{(1-H/q)^2(1-QCK)}.
 \tag{20}
\]
We will prove the following cleared identity of the original polynomial
family:
\[
 \boxed{\quad
 (1-H/q)^2(1-QCK)\,\sigma\Phi
 -(1-qK)^2(1-CH)\Phi
     =\frac\eta N(H-QK)
       [2+H^N+K^N+C^N(1-r^N)].\quad}
 \tag{21}
\]
In particular, on its regular locus,
\[
 \sigma\Phi=g\Phi+JF,\qquad
            J=\frac\eta N[2+H^N+K^N+C^N(1-r^N)].
 \tag{22}
\]
The scalar \(J\) is invariant under \(\sigma\). It is explicit
source data, not a freely chosen forcing or an unknown closed period.

Here is the complete determination of \(J\). Put
\(R_\Phi=\sigma\Phi-g\Phi\). Subtract the homogeneous identity
(13) from (8), without dividing by \(\Phi\). This gives
\[
 DR_\Phi=\frac{B}{\sigma^{-1}g}\,\sigma^{-1}R_\Phi.
 \tag{23}
\]
Direct substitution of (7), (9), and (20) shows
\[
 \frac{B}{D\,\sigma^{-1}g}
 =\frac{(1-qH)^2}{(1-H/q)^2}
   \frac{1-CK}{1-QCK}\frac{H-QK}{QH-K}
 =\frac{F}{\sigma^{-1}F}.
 \tag{24}
\]
Hence \(R_\Phi/F\) is invariant under \(\sigma\).

At fixed \(r\), \(\Phi\) is a symmetric Laurent polynomial in
\(H,K=r/H\) of degree at most \(d\) in either direction. The cleared
numerator of \(R_\Phi/F\) vanishes whenever \(H=QK\): the shift
then exchanges \(H,K\), and its two coefficients coincide. Therefore
division by \(H-Qr/H\) gives a Laurent polynomial. Before that
division its exponent range is contained in
\([-N-1,N+1]\); afterwards it is contained in \([-N,N]\).
Since \(Q\) is primitive, an invariant Laurent polynomial in this
range has the form
\[
                  R_\Phi/F=A_+H^N+A_0+A_-H^{-N}.
 \tag{25}
\]

The extreme coefficient [B, equation (20)] says that the coefficient
of \(H^d\) in \(\Phi(C,H,r/H)\) is \(\eta/N\); by symmetry the
coefficient of \(H^{-d}\) is \(\eta r^d/N\). In the numerator of
\(R_\Phi/F\), the highest term is the \(H^2/q^2\) term multiplying
\(\sigma\Phi\); its coefficient is
\((\eta/N)Q^{-d-1}=\eta/N\). The lowest term is the negative
\(q^2K^2\Phi\) term. Dividing at the two extremes proves
\[
                   A_+=\eta/N,\qquad A_-=\eta r^N/N.
 \tag{26}
\]

The constant coefficient follows from a different original source
readout, rather than a normalization of \(G_N\). Set \(H=q\), so
\(K=r/q\). The socle identity [B, equation (25)] gives
\[
 \Phi(C,q,r/q)=\frac{\kappa^2}{N}F_N(-C)G_N(r).
 \tag{27}
\]
Here \(F_N(-C)=(1+C^N)/(1-qC)\), with its polynomial meaning.
The first coefficient on the left of (21) vanishes at \(H=q\).
Using \(\kappa^2/q=-\eta\) and
\((1-r)G_N(r)=1-r^N\) consequently gives
\[
 (R_\Phi/F)|_{H=q}
       =\frac\eta N(1-r^N)(1+C^N).
 \tag{28}
\]
Since \(H^N=-1\) and \(K^N=-r^N\) there, equations (25)--(28)
give \(A_0=(\eta/N)[2+C^N(1-r^N)]\). This proves (21)--(22).

All divisions in this proof were on a generic locus. Equation (21)
is polynomial in \(C,H,K\), so it continues through its folds and
coefficient-zero loci. At a resonance one keeps that cleared identity
and its family derivatives, not a division by \(J\), \(H-QK\), or
a cyclic norm difference. Internal Hermite normals were already
included in the exact source (2); external parameter derivatives are
obtained by differentiating the whole polynomial identity.

## 5. The full cyclic norm and affine monodromy

The rational multiplier has the exact product
\[
 M:=\prod_{j=0}^{N-1}\sigma^j g
    =\frac{(1+K^N)^2}{(1+H^N)^2}
                         \frac{1-(CH)^N}{1-(CK)^N}.
 \tag{29}
\]
For example \(\prod_{j=0}^{N-1}(1-qQ^jK)=1+K^N\); the other
three products give the remaining factors. Thus \(M\) need not
equal one. On the canonical angle cover the Gamma section obeys
\(\sigma^NG_N=MG_N\). Resetting its marks after \(N\) steps is
not the same operation.

Write \(x=H^N,y=K^N,w=C^N\). A direct factorization gives
\[
 M-1=\frac{(y-x)[2+x+y+w(1-xy)]}
                    {(1+x)^2(1-wy)}
      =\frac{N}{\eta}\frac{(y-x)J}{(1+x)^2(1-wy)}.
 \tag{30}
\]
This is an identity, not a license to cancel \(J\) at its zeros.

The natural affine system is
\[
 \sigma\begin{pmatrix}\Phi\\1\end{pmatrix}
   =\mathcal B_\sigma
                 \begin{pmatrix}\Phi\\1\end{pmatrix},\qquad
 \mathcal B_\sigma=\begin{pmatrix}g&JF\\0&1\end{pmatrix}.
 \tag{31}
\]
Its Gamma subline has section \((G_N,0)^t\). Since the physical
polynomial satisfies \(\sigma^N\Phi=\Phi\), the full product is
\[
 \mathcal B_\sigma^{(N)}
      =\begin{pmatrix}M&(1-M)\Phi\\0&1\end{pmatrix}.
 \tag{32}
\]
The off-diagonal entry can equivalently be computed as the explicit
finite sum
\[
 \sum_{j=0}^{N-1}
  \left(\prod_{\ell=j+1}^{N-1}\sigma^\ell g\right)
                                            \sigma^j(JF).
 \tag{33}
\]
Iteration of (22) proves both descriptions. In particular the
off-diagonal current, not only the determinant \(M\), is retained.
When \(M=1\), the original family (21), (32)--(33) is still the
data; a formula obtained by dividing by \(1-M\) is not a substitute.

There is nevertheless a useful generic selection statement. Two
rational solutions of the forced equation (22), at fixed \(C,r\),
differ by \(u\) satisfying \(\sigma u=gu\). Rational functions of
\(H\) have \(\sigma^Nu=u\), whereas this homogeneous equation gives
\(\sigma^Nu=Mu\). Thus \(u=0\) wherever \(M\ne1\). The physical
polynomial is the unique rational solution on that generic locus.
At a norm resonance it is the continuation of this entire original
family; this uniqueness argument supplies no asymptotic lower bound.

Permuting the three boundary variables gives the same construction
for every balanced shift
\((A,B)\mapsto(A/Q,QB)\), with the third variable fixed. Two
independent such shifts commute and preserve \(CHK\). Their affine
matrices are flat. Indeed symmetry of (5) gives the homogeneous
top-left cocycle. Applying the two orders to the actual polynomial
section \((\Phi,1)^t\) then cancels that top-left term and forces the
off-diagonal cocycle identity, with no division by \(\Phi\).
Equivalently, on a nonzero Gamma chart,
\(\left(\begin{smallmatrix}G_N&\Phi\\0&1\end{smallmatrix}\right)\)
is a common fundamental frame. This is a lattice action with its
displayed cyclic norms; it has not been descended to a finite cyclic
action with identity monodromy.

## 6. Direct summation on real fractional orbits

The first-order equation has an elementary analytic consequence that
does not require second-order tracking. Fix a compact set of pairs
\(c,R>0\), \(c+R<1\), put \(k=R-h\), and let \(0\le h\le R\).
Write
\[
 \begin{split}
 L(x)&=\int_0^x\log|2\sin\pi t|\,dt,\\
 \mathcal A_0(c,h,k)&=L(c+h)+L(c+k)+L(h+k)
                              -2[L(c)+L(h)+L(k)],\\
 M_0(c,R)&=L(c+R)-L(c)-L(R)>0.
 \end{split}
 \tag{33a}
\]
Use the odd one-periodic continuation of \(L\) when needed. Uniformly
on this entire real interval, including its two endpoints,
\[
 \log|G_N(c,h,R-h)|=N\mathcal A_0(c,h,R-h)+O(\log N),
 \qquad \mathcal A_0(c,h,R-h)\ge M_0(c,R).
 \tag{33b}
\]

Here is a factorial proof of the endpoint uniformity, so (18) is not
being used beyond its strict compact shape scope. For real
\(-1/2\le x\le(1-\delta)N\), write \(x=n+\theta\), where
\(n\ge0\) is an integer and \(-1/2\le\theta\le1/2\). The endpoint
formula [F, equation (12)] and exact shifts (3) give
\[
 \mathfrak F(x)=\mathfrak F(\theta)
                   \prod_{j=1}^n(1-Q^{j+\theta}),\qquad
 \mathfrak F(\theta)=(-2\pi i/N)^\theta\Gamma(1+\theta)
                                            (1+O(N^{-1})).
\]
For \(n\ge1\), the product factors have strictly positive sine
moduli. Separate
\(\log(2\sin\pi u)=\log(2\pi u)+
\log(\sin\pi u/(\pi u))\). The second term has a bounded derivative
on \([0,1-\delta]\). Integral comparison for the shifted logarithms
in the first term, or the ordinary Gamma formula for their product,
has an error \(O(\log N)\), uniformly in \(n,\theta\).
For \(n=0\), both the endpoint formula and the corresponding short
integral have this bound directly, including \(x<0\). Consequently
\[
        \log|\mathfrak F(x)|=N L(x/N)+O(\log N)
              \qquad(-1/2\le x\le(1-\delta)N).
\]
For a real single argument in (5), reflect instead:
\[
 \log|\mathfrak F(N(1-a)-1/2)|
       =\log N-\log|\mathfrak F(Na-1/2)|
       =-NL(a)+O(\log N).
\]
The reflection phase has modulus one. The last comparison is uniform
at \(a=0\), because shifting an endpoint by \(1/(2N)\) changes its
log-sine integral by at most \(O((\log N)/N)\). All pair arguments
are in strict strips since \(c+h,c+k,R\) stay uniformly between
zero and one. Substitution in (5) proves the first part of (33b).
These factorials are nonzero on the stated real interval for all
sufficiently large \(N\).

For the second part, write
\(T(a,b)=L(a+b)-L(a)-L(b)\). On \(a,b>0,a+b<1\), its Hessian
divided by \(\pi\) is
\[
 \begin{pmatrix}
 \cot\pi(a+b)-\cot\pi a&\cot\pi(a+b)\\
 \cot\pi(a+b)&\cot\pi(a+b)-\cot\pi b
 \end{pmatrix}.
\]
Its diagonal entries are negative and its determinant is one,
by the cotangent addition formula. It is therefore negative definite.
Since \(\mathcal A_0=T(c,h)+T(c,k)+T(h,k)\), it is concave as a
function of \(h\) at fixed \(c,R\), and continuous at the endpoints.
Its endpoint values are both \(M_0\), which proves the lower bound.
The strict sign of \(M_0\) follows by fixing \(c\): its derivative
in \(R\) is \(\log[\sin\pi(c+R)/\sin\pi R]\), positive before
\(R=(1-c)/2\) and negative afterwards, with zero endpoint values.

Define the source-relative error on this interval by
\(E_N(h)=\Phi(C,H,K)/G_N(c,h,k)-1\). Dividing the exact equation
(22) by \(\sigma G_N=gG_N\), rather than approximating a scalar
ratio, gives
\[
 E_N(h+N^{-1})-E_N(h)
          =\frac{JF}{G_N(c,h+N^{-1},k-N^{-1})}.
 \tag{33c}
\]
This is used only when both endpoints lie in \([0,R]\).
On such real parameters, \(|J|\le6/N\). Also
\(|1-H/q|\ge c/N\) and \(|1-QCK|\ge c\), so \(|F|\le CN^2\).
Equation (33b) now gives the uniform estimate
\[
       |E_N(h+N^{-1})-E_N(h)|
                         \le N^C e^{-NM_0(c,R)}.
 \tag{33d}
\]
There is no division by a fold distance in this formula. The first-order
coefficients are regular for the steps used, even when the interval
crosses the central fold. At a zero of \(H-QK\) the numerator simply
vanishes.

Two points on the same fractional orbit inside \([0,R]\) differ by
at most \(N\) such steps. Summing (33d), with its polynomial factor
enlarged if necessary, proves
\[
 |E_N(h_2)-E_N(h_1)|\le N^C e^{-NM_0(c,R)},\qquad
             N(h_2-h_1)\in\mathbb Z.
 \tag{33e}
\]
This controls variation on every fractional orbit. It does not determine
the orbit-dependent constant.

For the anchored orbit there is also an initialized value. Retain the
additional hypothesis \(L(c+R)-L(R)>0\) from [P], on a compact set.
Equations (14) and [P] give
\(\Phi_1^0-G_N(c,1/(2N),R-1/(2N))=I_1^0\), with
\(|I_1^0|\le N^C\). Thus (33b)--(33e) prove
\[
 \frac{\Phi(C,H,K)}{G_N(c,h,R-h)}
             =1+O\!\left(N^C e^{-NM_0(c,R)}\right),\qquad
 h=(j+1/2)/N\in[0,R].
 \tag{33f}
\]
This is an exponentially accurate agreement on the whole indicated
anchored grid, with the original source current still accounted for.
It is not an exponential estimate at arbitrary fractional offsets;
an additional initializer is needed to fix those constants.

## 7. Integer packets agree exactly with the Gamma section

There is a useful exact check of the initialized residue family, beyond
its leading asymptotic. In the notation of [P], let \(a=m\) be an
integer with \(1\le m<N\), put
\(h=(m-1/2)/N\), \(k=R-h\), and let \(\mathcal G_m^0\) be its
pole-free prefactor from [P, equation (22)]. The arguments of (5) are
\[
 \begin{array}{c|ccc}
 \text{singles}&B_*&N-m&L+m-1\\
 \text{pairs}&B_*-m+1&D_*+m-1&L .
 \end{array}
\]
Using the exact prefactor there and reflection in (3) gives
\[
 \boxed{\quad
 \frac{G_N(c,(m-1/2)/N,R-(m-1/2)/N)}{\mathcal G_m^0}
   =(rQ^m)^{m-1}
       \frac{(q^3CQ^{-m};Q)_{m-1}}{(q^3rC;Q)_{m-1}}.
 \quad}
 \tag{34}
\]
For the scalar phase in this simplification, use
\(\mathfrak F(m-1)\mathfrak F(N-m)
 =Nq^{-(m-1)(N-m)}\). The remaining \(p,L\) factors reduce to
\((-1)^{m+1}r^{m-1}Q^{m(m-1)/2}\); multiplying the reflection
phase gives \((rQ^m)^{m-1}\), including at even levels.

The right side is the elementary terminating sum
\[
 \sum_{j=0}^{m-1}
 \frac{Q^j(Q^{1-m},rQ^m;Q)_j}{(Q,q^3rC;Q)_j}.
 \tag{35}
\]
Here is a finite proof, so no root-of-unity summation or infinite
product limit is assumed. For generic \(Q\), \(n\ge0\), multiply
the proposed identity
\[
 \sum_{j=0}^n\frac{Q^j(Q^{-n},b;Q)_j}{(Q,c;Q)_j}
                         =\frac{b^n(c/b;Q)_n}{(c;Q)_n}
 \tag{36}
\]
by \((c;Q)_n\). The result is the polynomial identity
\[
 \sum_{j=0}^n(-1)^j Q^{j(j-1)/2-(n-1)j}
  {n\brack j}_Q(b;Q)_j(cQ^j;Q)_{n-j}
                      =\prod_{\ell=0}^{n-1}(b-cQ^\ell).
 \tag{37}
\]
It follows by induction using
\(b(b;Q)_j=Q^{-j}[(b;Q)_j-(b;Q)_{j+1}]\) and the two
equivalent \(Q\)-Pascal recurrences. More explicitly, if the
coefficient of \((b;Q)_j\) is \(A_{n,j}\), multiplication by
\(b-cQ^n\) gives
\(A_{n+1,j}=(Q^{-j}-cQ^n)A_{n,j}-Q^{1-j}A_{n,j-1}\);
the coefficients displayed in (37) obey this recurrence, including
its two endpoints. This proves (36). Set \(n=m-1\),
\(b=rQ^m\), \(c=q^3rC\). Since every \((Q;Q)_j\) has \(j<N\),
specialization at the stated primitive root is legal after canceled
continuation. This proves (35).

The actual finite rectangle packet of [P] stops at
\(K_*=\lfloor NR+\zeta\rfloor\). It equals the full terminating
sum (35) only when \(K_*\ge m-1\). This holds for each fixed
finite collection of positive integers and sufficiently large \(N\);
it is not asserted for every \(m<N\) at a fixed \(R\). Even when
the packet equals (35), the actual source still includes its vertical
current. Neither these integer identities nor formal interpolation
alone gives an exponentially accurate generic-offset comparison.

## 8. What can and cannot be sewn from this extension

Affine source extensions and their tensor face and corner terms are
already present in the earlier factorial cut-source treatment. The
new information here is the explicit original-crossing multipliers
\(g,J,F\), their exact norm, and their calibration to the physical
polynomial source. No novelty is claimed for upper-triangular
extensions or variation of constants as general methods.

Tensoring (31) keeps all source terms. For example, the shifted
product of two sourced components contains the two single-source
terms and the double-source term; the latter cannot be omitted before
an actual contraction. Compatible changes of frame cancel on an
internal edge only when the specified dual pairing and the original
boundary vectors and closing row are transported as well.

These are solution/source channels over the boundary difference
field. They do not span the \(N\)-dimensional full Hermite Conway
leg, and no intertwiner for its multiplication or genuine turn has
been constructed here. Flatness at fixed \(CHK\) does not establish
control in the remaining total-center direction, a bounded-rank
replacement of arbitrary components, or a positive sewing cycle.
The coherent parameters and balanced shifts have not been identified
with a knot's marked meridian, longitude, or surgery equations.
All cyclic norms, zeros, and original peripheral factors must remain
until a whole-source pushforward is proved.

The direct-summation corollary controls all fractional-orbit variation
and gives anchored-grid exponential agreement. This note proves no
exponential generic-offset initializer, no exact equality \(\Phi=G_N\),
and no knot-volume or finite-exception theorem. It supplies exact local
data for that separate analytic and geometric comparison.

The complete direct proof sources are:

| Label | Source | SHA-256 |
|---|---|---|
| B | [Original four-input polynomial source](research_four_coherent_boundary_polynomial_source.md) | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| F | [Canonical factorial and full-strip estimates](research_four_coherent_fractional_boundary_source.md) | 8126481cadaa4b1b0ba287495de14cb3263baf8343fbfca9aa4d5b6d962595b1 |
| P | [Original crossing initializer and retained packet](research_four_coherent_zero_radius_boundary_source.md) | f74a6b951936f29f5cf66e4b34cfc84b2c890b1ba5464f472ca023aa70c5c621 |

All three complete matching sources were read at their renewed pins.
Only written mathematics and text operations were used.
