# An actual whole Frobenius source is a Fermat-cover trace

Research proof, 27 October 2026. Integral divided powers give a
whole algebraic source polynomial whose root value is the actual
binomial coherent source. Its Kummer-cover trace, norm and first
quantum-normal flag transport are explicit. This supplies a source
object before taking jets, with every power and phase retained.

This is a choice of whole coupons in the original integral color.
An explicit root-identity pair gauge compares it with the previously
specified divided-exponential coupons. Operators and all partial
sources must be transported by that gauge. No equality with a new
state model, controlled growing-level norm, or selected geometric
period is inferred.

## 1. Actual divided powers and the whole polynomial

Fix N>=2, m=N(N+1)-1 and a residue string 0<=s<N in D_m(q).
Use the constant actual sign frame
\[
 w_{k,s}=\beta_{k,s}u_{kN+s},\qquad
 \beta_{k,s}=(-1)^{Nk(k-1)/2+ks},\quad 0\le k\le N.
\]
Symmetric Gaussian coefficients below are integral Laurent
polynomials, with the original divided-power formulas
\[
 F^{(r)}u_j={j+r\brack r}_q u_{j+r},\qquad
 E^{(r)}u_j={m-j+r\brack r}_q u_{j-r}.
\]
Put L_s=m-s and epsilon_s=(-1)^(N-1+s). Define
\[
 A_{k,s}(q)=\epsilon_s^k{L_s\brack kN}_q,\qquad
 P_s(q,t)=\sum_{k=0}^N A_{k,s}(q)t^k.             \tag{1}
\]
Here t is a SOURCE-FLAG coupling. It is not the knot meridian,
the classical longitude, or a quantum-A spectral coordinate.
The literal constant-frame ket psi_s=sum_k w_(k,s) is made from
actual divided powers as
\[
 \psi_s=\sum_k\frac{\beta_{k,s}}{{s+kN\brack kN}_q}
                         F^{(kN)}u_s.             \tag{2}
\]
Every denominator is a unit at q_N: its root value is (-1)^(ks).
The homogeneous dual is also an actual divided-power row:
\[
 \widetilde\lambda_s(q;c,d)=
   \sum_k\epsilon_s^k\beta_{k,s}c^{N-k}d^k
                             u_s^*E^{(kN)}.
\]
Its value on w_(k,s) is A_(k,s)c^(N-k)d^k. Thus its pairing with
the ket is the homogeneous polynomial
\[
 B_s(q;c,d)=\sum_k A_{k,s}(q)c^{N-k}d^k,
       \quad B_s(q;1,t)=P_s(q,t).                 \tag{3}
\]
Normalize by this original pairing unit on its marked chart.
At c=d=1 the normalized dual has coefficients A_k/P_s(q,1).
The root value P_s(q_N,1)=2^N is retained, not set to one before
normalization. Scaling the ket by alpha^N and the dual inversely
retains the unprojectivized source line.

## 2. Exact trace and norm on the root cover

Let zeta_N be the marked N-th root of unity, independent of the
variable q. Work on the Kummer cover x^N=epsilon_s t and set
\[
 \Pi_s(q,x)=\prod_{r=0}^{L_s-1}
                       (1+q^{L_s-1-2r}x).
\]
Multiplication of the factors gives the symmetric Gaussian identity
Pi_s=sum_j {L_s choose j}_q x^j. Averaging the deck transformations
x->zeta_N x kills exactly the degrees not divisible by N. Hence
\[
 \boxed{\ P_s(q,t)=\frac1N\operatorname{Tr}_{x^N=\epsilon_st}
                                      \Pi_s(q,x).\ }            \tag{4}
\]
This is an exact polynomial identity before normal specialization.
It is valid even at t=0 as an identity of coefficients; the cover
is etale on t!=0. The 1/N is part of the source construction.

The full norm is equally explicit. Put Z=Q^N=q^(2N) and
theta_s=(-1)^s q^[N(L_s-1)]. The elementary deck product gives
\[
 \boxed{\ \mathcal N_s(q,t):=\operatorname{Norm}\Pi_s
            =\prod_{r=0}^{L_s-1}(1+\theta_s Z^{-r}t).\ }          \tag{5}
\]
Indeed Norm(1+a x)=1-(-a)^N epsilon_s t, and
(-1)^N epsilon_s=-(-1)^s. No peripheral sign or central power
has been removed in (5). This is a finite factorial in the WHOLE
power coordinate Z, distinct from its value Z=1.

On a marked cover let nu_s^N=mathcal N_s, with nu_s=1 at t=0.
Then c_s=Pi_s/nu_s has norm one and
\[
              P_s=\nu_s\,\frac{\operatorname{Tr}c_s}{N}.        \tag{6}
\]
Thus the source polynomial is a selected trace in a concrete
norm torsor. A norm-one statement about c_s does not by itself
give the trace in (6); both are specified here. Zeros of the
norm or trace remain part of the lattice/domain data.

There is an exact power-parameter law for the SAME source product.
Put q_hat=-q^N, so q_hat^2=Z and q_hat=1 at the marked root.
Since L_s-1 has parity s, (5) becomes
\[
 \operatorname{Norm}\Pi_s(q,x)
        =\prod_{r=0}^{L_s-1}(1+\widehat q^{L_s-1-2r}t)
        =\sum_{j=0}^{L_s}{L_s\brack j}_{\widehat q}t^j.          \tag{6a}
\]
Thus the Kummer norm is the identical finite Gaussian product at
the power parameter -q^N. Its chosen root restriction is a
classical binomial product. This is an algebraic identity; it does
not assert a modular-group action or equate different knot states.

The norm and selected trace also retain different normal data.
Write v=Log Z with v=0 at the marked root. Pairing the symmetric
exponents in (6a) gives
\[
 [\partial_v\log\mathcal N_s]_0=0,\qquad
 [v^2]\log\mathcal N_s
       =\frac{t L_s(L_s^2-1)}{24(1+t)^2}.            \tag{6b}
\]
Indeed their sum is zero and their squared sum is L_s(L_s^2-1)/12.
The source trace in (9) generally has a nonzero FIRST normal on
middle residue strings. That information is in its specified
cyclic trace, even though the norm's first derivative vanishes.

## 3. Its actual root restriction and normalization

Write L_s=N^2+b_s, b_s=N-1-s. At q_N every block of N factors
in Pi_s contributes EXACTLY 1+t: the sign from q_N^N=-1 cancels
epsilon_s as in (1). There are N full blocks. The remaining
polynomial has degree b_s<N, so its deck average is one. Therefore
\[
             P_s(q_N,t)=(1+t)^N,\qquad
       A_{k,s}(q_N)={N\choose k}.                 \tag{7}
\]
One can also verify (7) by cancelling the root zero factors in
the Gaussian product. Its symmetric phase is (-1)^[k(N-1-s)],
which epsilon_s^k cancels for every s and every parity of N.

Equations (5)--(6) keep a useful fractional head correction:
\[
 \mathcal N_s(q_N,t)=(1+t)^{L_s},\quad
 \nu_s(q_N,t)=(1+t)^{N+b_s/N},\quad
          \frac{\operatorname{Tr}c_s(q_N)}N=(1+t)^{-b_s/N}.     \tag{8}
\]
All branches have the same mark at t=0. The product is (7).
Dropping either factor would change the source character.
In particular the original selected dual gives the endpoint
E_(N,0) the value 2^(-N), with the full N-th power still visible.

## 4. First normal equals an explicit flag connection

Use delta=1-Q^N and q=q_N(1-delta)^(1/(2N)). Set
\[
 \ell_s=-\frac12\sum_{a=1}^{s}
             \frac{q_N^a+q_N^{-a}}{q_N^a-q_N^{-a}}.
\]
Then the actual Gaussian polynomial has the exact first derivative
\[
 [\partial_\delta A_{k,s}]_0=k\ell_s{N\choose k},\qquad
 [\partial_\delta P_s]_0=\ell_s N t(1+t)^{N-1}.     \tag{9}
\]
Here is a direct cancellation proof. Split the symmetric Gaussian
product into arguments divisible by N and the remaining residues.
Ratios of the vanishing q-integers have zero first relative
logarithmic derivative: after their simple zeros cancel they are
ratios of odd sinh functions. For each of the k nonzero residue
blocks, cyclic reindexing leaves
N sum_(a<=b_s) cot_q(a) in the q-log derivative. Pairing residues
a and N-a makes that sum equal N sum_(a<=s) cot_q(a).
Finally q partial_q=-2N partial_delta at the root. This gives (9),
including its sign.

At the normalized selected point t=1, the dual's first derivative is
\[
 [\partial_\delta\lambda_s(w_k)]_0
       =2^{-N}{N\choose k}\ell_s(k-N/2).           \tag{10}
\]
More generally it is ell_s t partial_t of the normalized root
dual. Thus the first normal is a concrete source-flag transport.
The same ell_s is the original head connection in
[the whole Jackson current](endpoint_completed_normal_clock_euler_current.md).
It vanishes for s=0,N-1; middle strings retain it.
Higher normals remain those of the WHOLE polynomial (4), with
no assertion that they are all a single flag reparameterization.

## 5. Exact pivotal/moment character and the original coupon gauge

On this residue string J=kN+s. The frozen-pivot adapter Z^J has
the exact source generating function
\[
 \lambda_s(q,t)Z^J\psi_s
              =Z^s\frac{P_s(q,tZ^N)}{P_s(q,t)}.     \tag{11}
\]
This retains all cap/Green moments and both power coordinates.
At the root its value is one, while its normal derivatives must
be taken from (11), including both moving q-Gaussian coefficients.
The frozen root binomial formula cannot be substituted before
those derivatives. No growing-N scaled profile is asserted.

Finally compare this source pair (psi_f,lambda_f) with the
previous actual divided-exponential pair (psi_c,lambda_c), both
normalized to one. They have the SAME root pair by (7).
Let P_i=psi_i lambda_i and put
\[
 G=\psi_f\lambda_c+(I-P_f)(I-P_c).
\]
Its root is I, so it is an invertible regular rational germ, and
\[
          G\psi_c=\psi_f,\qquad\lambda_fG=\lambda_c.              \tag{12}
\]
All arbitrary inserted operators must become G T G^(-1),
connections include their derivative gauge term, and every source,
dual, projector and peripheral adapter is carried along. This is
an actual whole coupon comparison, not an inference from matching
root numbers or a replacement of the source in a partial word.
It supplies neither the missing geometric-current pushforward nor
the selected hyperbolic-volume estimate.

[Exact actual divided-source and cover audit](../experiments/audit_whole_frobenius_source_fermat_trace.py).
