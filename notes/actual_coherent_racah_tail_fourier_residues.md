# A finite Fourier identity for coherent Racah normal tails

29 October 2026. This is an own finite algebraic identity for the actual
retained `[2N]` current. It gives a uniform logarithmic relative bound
when the largest face sum occurs at least twice, including genuinely
nonempty high-partner tails. For arbitrary partner labels the identity
retains a second alternating sum. No general bound on that residual,
higher normal jets, or completed physical transport is asserted.

## 1. The actual tail and its positive core

Use the symmetric quantum-factorial convention and the exact generic
sum of [the supported normal theorem](actual_supported_racah_common_phase_and_normal_metric.md).
Put `D=N-1`, `theta=pi/N`, `q=exp(i theta)`, `Q=q^2`, and

    s_r=product_(u=1)^r 2 sin(u theta),  s_0=1.

For any partner of a supported folded sextuple let `F_i` be its four
face sums and `Q_k` its three opposite sums. Assume the tail is live:
`min Q_k>2D`. Define

    a_i=2D-F_i,  b_k=Q_k-2D,  c_k=D-b_k=3D-Q_k.

The exact face-deficit inequalities give

    0<=a_i<=c_k<=D-1 for EVERY i,k,
    sum_k c_k-sum_i a_i=D.                       (1)

Indeed `c_k-a_i=D-(Q_k-F_i)>=0`; the equality follows from
`sum F_i=sum Q_k`. Order the four `a_i` as

    A=a_1<=B=a_2<=a_3<=a_4.

The true positive core, indexed by `z=2D-v`, is

    C=sum_(v=0)^A C_v,
    C_v=(1/N) product_k s_(c_k-v)
                     /[s_v product_i s_(a_i-v)] >0.              (2)

This is the same `C(q)` appearing in the ACTUAL generic identity

    (-1)^D S/[N]=C(zeta)+[2N] T(zeta).             (3)

The true root current is

    T(q)=-2 sin(theta) N^2 sum_(k=0)^(D-c_max-1)
       (-1)^k s_k /
       [product_i s_(a_i+1+k) product_j s_(D-c_j-1-k)].            (4)

All displayed factorial arguments are between zero and `D`. No
invalid factorial has been assigned a value or silently removed.

## 2. Exact coherent Fourier reduction

Write

    H_r=sum_(u=1)^r cot(u theta), H_0=0,
    J_v=H_v+sum_k H_(c_k-v)-sum_i H_(a_i-v).

Then the following identity is exact at every level, of either parity:

    T(q)=-sin(theta) sum_(v=0)^A C_v J_v
          +(2 sin(theta)/N) sum_(v=A+1)^B (-1)^(A+v) E_v,          (5)

where

    E_v=s_(v-A-1) product_k s_(c_k-v)
                    /[s_v product_(i=2)^4 s_(a_i-v)] >0.         (6)

An empty last sum is zero. In particular it is absent when `A=B`,
equivalently when the largest face sum occurs at least twice.

The second sum is essential. For `N=5` and partner labels
`(a,b,c,d,e,f)=(2,2,3,3,2,2)`, one has the ordered arrays
`a_i=(0,1,1,2)`, `c_k=(2,3,3)`. The first sum in (5) is zero,
whereas the retained residual gives `T(q)=-1`. Dropping it would
incorrectly assert zero current.

## 3. Own finite algebraic proof

This proof only uses polynomial division, finite sums of roots of
unity, and the elementary sine-factorial reflection
`s_r s_(D-r)=N`.

Let

    R(x)=product_k product_(u=1)^(c_k)(1-Q^u x)
                      / product_i product_(u=1)^(a_i)(1-Q^u x),
    f(x)=x R(x)/(1-x),
    K=sum_k c_k(c_k+1)/2-sum_i a_i(a_i+1)/2,
    beta=(2 sin(theta)/N) i^(N-2) q^(-K).

In (4) put `j=k+1` and use the sine-factorial reflection on its
three descending denominators. Converting every remaining sine by
`2 sin(u theta)=i q^(-u)(1-Q^u)` gives exactly

    T(q)=beta sum_(j=1)^(D-c_max) f(Q^j).          (7)

The phase is important: the alternating sign and the degree difference
in (1) leave `q^(2j)=Q^j`, the numerator `x` in `f`.

After cancellation, `f` has SIMPLE poles precisely at

    r_v=Q^(-v),  0<=v<=A.

For `1<=u<=A` the numerator has three factors `1-Q^u x` and the
denominator has four. Above `A` there are no poles because every
`c_k` is at least every `a_i`. Its polynomial part has degree at
most `D=N-1`: the numerator degree minus denominator degree is `D`.

Let

    B_v=[(1-x/r_v) f(x)]_(x=r_v),
    L_v(x)=(1-x/r_v) f(x).

Ordinary partial fractions give a polynomial `P` of degree at most
`N-1` with

    f(x)=P(x)+sum_v B_v/(1-x/r_v).

Since `f(0)=0`, one has `P(0)=-sum_v B_v`. Sum this identity over
all `N`th roots except its pole set. For a nonconstant monomial
of degree less than `N` the full root sum is zero, and

    sum_(x^N=1,x!=r_v) 1/(1-x/r_v)=(N-1)/2.

The finite regular parts at the other omitted roots cancel the
corresponding partial-fraction corrections. Thus

    sum_(x^N=1,x not a pole) f(x)
       =sum_(v=0)^A [r_v L_v'(r_v)-(N+1)B_v/2].                 (8)

For example, the finite regular part of `f` at `r_v` is
`-r_v L_v'(r_v)`. This also checks the constant `(N+1)/2` in (8).

Direct conversion of the unit factors gives, for EVERY `v`,

    B_v=i^(-D) q^K N C_v,
    r_v L_v'(r_v)/B_v=(N+1)/2-(i/2)J_v.         (9)

Here is an explicit verification rather than an assumed residue sign.
For `v>=1`, set `(Q;Q)_r=product_(u=1)^r(1-Q^u)`. Cancelling the
three numerator and four denominator zero factors gives

    B_v=(-1)^v Q^[v(v-1)/2]
           product_k (Q;Q)_(c_k-v)
              /[(Q;Q)_v product_i (Q;Q)_(a_i-v)].

Converting these factorials to sines leaves the phase
`i^(-D) q^(K-vN)(-1)^v=i^(-D)q^K`, proving the first part of (9).
For `v=0` it is immediate from `R(1)`. The logarithmic derivative
of a unit factor is

    -Q^w/(1-Q^w)=1/2-(i/2)cot(w theta).

After removing the pole, the signed number of unit factors is
`N-1`, and the leading factor `x` contributes one. The real part
is therefore `(N+1)/2`. The negative indices `1-v,...,-1` and the
factor `1-x` contribute `H_v`, while the remaining positive indices
contribute the other seven sums in `J_v`. This proves the second
part of (9). Since `beta B_v=-2i sin(theta) C_v`, (8) contributes
exactly the first term of (5).

It remains to compare (8)'s root set with (7)'s ACTUAL finite range.
For roots `x=Q^(-v)` outside the range in (7), cancellation shows:

* `0<=v<=A`: these are precisely the omitted poles;
* `A<v<=B`: the regular value can be nonzero;
* `B<v<=c_max`: the regular value is zero.

The last assertion follows by counting factors: above `B`, at most
two denominator factors remain while at least three numerator factors
remain up to `a_4`; beyond `a_4`, no denominator factors remain, and
at least one numerator factor remains up to `c_max`.
For the middle range the exact unit-factor conversion gives

    beta f(Q^(-v))=(2 sin(theta)/N)(-1)^(A+v+1) E_v.              (10)

One can verify (10) before conversion using

    f(Q^(-v))=(-1)^(A+1) Q^[vA-A(A+1)/2]
       (Q;Q)_(v-A-1) product_k (Q;Q)_(c_k-v)
        /[(Q;Q)_v product_(i=2)^4 (Q;Q)_(a_i-v)].

Subtracting these extra regular nodes from (8) proves (5), including
its residual sign. This is a finite proof for all arrays satisfying
(1), not an inference from finitely many knots or levels.

## 4. A proved nonempty-tail first-normal bound

Suppose `A=B`. Since `H_r=H_(D-r)` and positive cotangents obey
`cot(u theta)<=1/(u theta)` for `u<N/2`,

    0<=H_r<=(N/pi)(1+log N),  0<=r<=D.

Equations (2),(5) therefore give the uniform coherent bound

    |T(q)| <= 8(1+log N) C(q).                  (11)

Unlike an estimate of the absolute summands in (4), this uses the
actual cancellations. The factor 8 is deliberately nonsharp.
Together with the existing positive-core jet estimate and the exact
normal derivative

    dot G(q)=dot C(q)+4N/(q-q^-1) T(q),
    G=(-1)^D S/[N],  dot=D_(log zeta),

it proves, with an absolute constant `C_*`,

    |dot G(q)| <= C_* N^2(1+log N) C(q).         (12)

Indeed the sharper form before `sin(theta)<=pi/N` is applied in
(11) cancels the denominator in `4N/(q-q^-1)` directly. The analytic
face factors have the same unit-factor logarithmic bound. Hence for
this entire repeated-maximal-face class, the ACTUAL normalized squared
scalar and its local positive square root satisfy

    K(q)=W_N^2,
    |dot K(q)| <= C_* N^2(1+log N) W_N^2,
    H(q)=W_N,
    |dot H(q)| <= C_* N^2(1+log N) W_N.           (13)

Their first inverse jets have the corresponding reciprocal bounds.
This conclusion includes live `[2N]` currents; it does not extend to
higher generic normal orders merely by differentiating (5), which is
an identity on the fixed cyclotomic fiber.

## 5. The former all-high diagnostic is now a theorem

Take `N=3m+1` and all six high spins equal to `2m`. Then `a_i=0`,
`c_k=m`, `A=B=0`, and `C=s_m^3/N`. Equation (5) proves EXACTLY

    T(q)/C(q)=-3 sin(theta) sum_(u=1)^m cot(u theta).              (14)

More generally, every live partner array with all four faces equal
`2D` has `a_i=0`; (14) becomes

    T(q)/C(q)=-sin(theta) sum_k sum_(u=1)^(c_k) cot(u theta).

Thus the finite Fourier proof is not confined to the equilateral
sequence. The former numerical observations remain archived as their
historical record; (14) now follows from the own uniform identity.

## 6. The residual is an exact partner involution

For a unique minimum `A<B`, define new arrays

    a*=(A,D-c_1+A,D-c_2+A,D-c_3+A),
    c*=(D-a_2+A,D-a_3+A,D-a_4+A).                (15)

They again satisfy (1), have the SAME unique minimum `A`, and applying
(15) twice returns the original arrays up to permutation. Substitute
`v=A+1+k` in the residual in (5), and apply
`s_r s_(D-r)=N` to its three numerator factorials. The three factors
of `N` cancel its prefactor exactly. The result is the ACTUAL tail
formula (4) for `(a*,c*)`, with no extra factor or sign. Therefore

    T(a,c)-T(a*,c*)=-sin(theta) sum_(v=0)^A C_v J_v.               (16)

Moreover the same factorial reflection proves

    C*_v=C_(A-v),  C*=C,  J*_v=-J_(A-v).          (17)

The last equality also follows directly from `H_(D-r)=H_r`.
Thus the difference in (16) is logarithmically bounded relative to
`C`, whereas this involution alone leaves the average of the two
currents undetermined. Repeated application is not a contraction.

For the actual tetrahedral labels, this is an actual PARTNER move,
not just a transformation of abstract factorial arrays. If the unique
largest face is `F_1=a+b+e`, retain those three edges and replace its
complementary edges by

    (c,d,f) -> (D-c,D-d,D-f).                    (18)

The unchanged face sum is `F_1`; the other new face sums are the
three numbers `2D-Q_k+F_1`, and the new opposite sums are
`2D+F_1-F_i` for `i!=1`. These are exactly (15). They again have the
same unique largest face, because the original tail is live. The
other choices follow by tetrahedral relabeling.

In particular (16) controls a difference of the full ACTUAL first
normals, not merely a difference of bare root tails. Both core germs
have polynomial logarithmic derivatives, their root cores agree by
(17), and the four face factors also have polynomial logarithmic
derivatives. Differentiating (3) for each branch therefore gives

    |dot K_B(q)-dot K_(B*)(q)|
                       <= C_* N^2(1+log N) W_N^2.               (19)

No equality of the two generic normal germs is asserted. Combining
these controlled three-edge differences with other exact source
relations is a possible next step; (16) by itself does not fix the
common first-normal component.

## 7. What the general residual still requires

For a unique largest face, the last sum in (5) is still alternating.
No polynomial relative bound on its absolute envelope has been proved
here. Positivity of the residues does not authorize replacing this
residual by its absolute sum. The exact formula exposes the partner
involution and proves the repeated-maximal-face class, but it does
not close the general first-normal transport problem. The transformed
summation interval need not be shorter than the original one.

The identity holds for abstract arrays (1) as well as actual partner
branches. Applying it to a source retains all original generic
normalization, peripheral factors and marked exterior data through
the already proved coefficient theorem. It does not alone supply a
positive completed recoupling metric or identify a global complement.

Audit: [exact finite-field Fourier and tail checks](../experiments/audit_actual_coherent_racah_tail_fourier_residues.py)
and [recorded results](../experiments/actual_coherent_racah_tail_fourier_residues_results.json).

Independent full analytical review of the Fourier residue identity,
phase conversion, retained residual and first-normal scope passed.
The exact audit freshly replayed 13,132 balanced arrays and 32 all-high
identities. The uniform proof is the algebraic argument above; these
finite checks are supplementary.
