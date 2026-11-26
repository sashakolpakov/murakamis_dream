# The actual pure source need not be real stable or Lee–Yang zero-free

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The filling argument uses an even Fourier polynomial on a finite color
window. Here that Fourier operation is applied to the exact full
physical source samples, and separately to its pure wire corridor.
Positivity of the pure core does not give a general real-stable or
Lee–Yang class preserved by Conway composition. A strict construction
with two crossing circles already shows the failure. The proof retains
the complete physical source, including its signed aliases and Casimir
normals. It does not replace that source by a positive majorant.

The conclusion concerns the stated finite color window. It says nothing
about a smaller zero-free neighborhood of the complete geometric point,
which is already available in the long-filling proof, or about a
different geometric domain adapted to a short filling.

## 1. A strict construction and its exact physical source

Fix \(N\ge5\), and put
\[
 d=N-1,\qquad M=\lfloor d/2\rfloor,\qquad
 q=e^{\pi i/N},\qquad \theta=\pi/N,\qquad
 S_j=\prod_{k=1}^j2\sin(k\theta),\quad S_0=1.
 \tag{1}
\]
Write \(e_0,\ldots,e_d\) for the normalized Newton basis of the
**full** pair Casimir algebra. Let \(\mathcal T\) be the genuine
physical quarter-turn and \(\phi\) the original marked Frobenius
closing. The exact source identities are
\[
 \mathcal T e_j=e_{d-j},\qquad
 \phi(e_i e_j)=\delta_{i+j,d},\qquad
 \phi(f\mathcal T g)=\sum_{r=0}^d f_r g_r,
 \tag{2}
\]
where \(f=\sum f_re_r\) and \(g=\sum g_re_r\). The last pairing
is bilinear. It becomes a sum of real squares below because the
specified pure-circle coefficients are real, not because an arbitrary
quantum source has been replaced by a Hermitian norm.

Use two distinct elementary boxes in the construction
\[
                         \tau=C\bigl(h_1\,\mathcal T(h_2)\bigr).
 \tag{3}
\]
The first closing child has strict type \(L\), the second type \(H\).
Assign leaf coordinates \(a_1=a_2=1/4\). The turn changes the
second output to \(3/4\); the closing outputs are complementary.
There is no retained product below the closing root. Thus (3) is
strict in the original sense. With no retained half twists, the
main-strand pairings are \(U\) and \(I\); stacking gives \(U\),
with no internal component, and cylindrical closure gives one main
component. It is therefore an admissible strict construction, not an
independently chosen coefficient array. This observation is not a
claim about the hyperbolicity of any particular short filling.

For an ordinary auxiliary color \(j\), let \(L_j\) be the original
circle operator, with its original pivot, and put
\[
                       \mathsf h_j=\mathcal T(L_j).
\]
There is no extra half twist. For \(0\le a\le M\), write its
complete Newton packet as
\[
            \mathsf h_{N-a}=\sum_{r=0}^d a_{r,N}(a)e_r.
 \tag{4}
\]
The exact pure-leaf theorem states
\[
 \mathsf h_{N-a}
   =\sum_{r=a}^M A_{N,r}(a)e_r+(-1)^N\mathsf h_a,
 \qquad
 A_{N,r}(a)=
       \frac{N^2S_{2r}}{S_r^2S_{r-a}S_{r+a}}>0,
 \tag{5}
\]
with \(\mathsf h_0=0\). Its alias \(\mathsf h_a\), for
\(a>0\), has real coefficients and support in indices at least
\(N-a\). Consequently every coefficient in (4) is real. In
particular, for any integer window satisfying
\[
                              1\le H<M,
 \tag{6}
\]
we have exactly
\[
       a_{r,N}(a)=A_{N,r}(a)
          \quad(0\le a\le H,\ H\le r\le M).
 \tag{7}
\]
The alias cannot reach these indices, because \(N-H>M\).
No alias or repeated-root direction is omitted from (4).

The full original source samples for (3) are
\[
 \mathcal A_N(a,b)
    =\phi\bigl(\mathsf h_{N-a}\,
                         \mathcal T(\mathsf h_{N-b})\bigr)
    =\sum_{r=0}^d a_{r,N}(a)a_{r,N}(b)
       \qquad(0\le a,b\le H).
 \tag{8}
\]
This uses (2) on the complete physical packets. In particular it
retains the signed alias terms in both factors. Any separately
recorded common framing unit leaves the zero statements below
unchanged; (8) itself uses the original source normalization.

## 2. The prescribed finite even Fourier polynomial

Extend these samples by evenness on this finite window, and define
the Laurent polynomial
\[
 \mathscr F_{N,H}(z_1,z_2)
   =\sum_{a,b=-H}^{H}
        \mathcal A_N(|a|,|b|)z_1^a z_2^b.
 \tag{9}
\]
Only the actual colors \(N,N-1,\ldots,N-H\) have been used.
This is the finite even color Fourier operation of the filling
argument, here applied to the complete samples (8). No assertion is made here about an untruncated color
orbit. A cutoff \(H=\lfloor\delta N\rfloor\) with fixed
\(0<\delta<1/2\) satisfies (6) for all sufficiently large levels.

For each complete Newton coordinate put
\[
 \begin{split}
 p_r(u)&=a_{r,N}(0)+2\sum_{a=1}^H
                         a_{r,N}(a)T_a(u/2),\\
 K_{N,H}(u,v)&=\sum_{r=0}^d p_r(u)p_r(v).
 \end{split}
 \tag{10}
\]
Here \(T_a\) is the ordinary Chebyshev polynomial, so
\(2T_a((z+z^{-1})/2)=z^a+z^{-a}\). Every \(p_r\) is real
and has degree at most \(H\). Expanding (8) in (9) gives the
exact identity
\[
 \boxed{\quad
 \mathscr F_{N,H}(z_1,z_2)
       =K_{N,H}(z_1+z_1^{-1},z_2+z_2^{-1}).
 \quad}
 \tag{11}
\]
This equality includes every summand \(0\le r\le d\).

At least two degree-\(H\) features in (10) are not proportional.
Indeed (7) gives a positive leading coefficient for \(p_H\) and
\(p_{H+1}\). Proportionality would imply equality of their first
two Laurent coefficient ratios. But for \(H\le r\le M\),
\[
 \frac{a_{r,N}(1)}{a_{r,N}(0)}
   =\frac{S_r^2}{S_{r-1}S_{r+1}}
   =\frac{\sin(r\theta)}{\sin((r+1)\theta)}.
 \tag{12}
\]
These ratios strictly increase with \(r\): their consecutive
difference is
\[
 \frac{\sin^2\theta}
      {\sin((r+1)\theta)\sin((r+2)\theta)}>0.
 \tag{13}
\]
All denominators used for \(r=H\) are positive in (6).

The complete samples and the pure wire corridor are different finite
functions. For (3), a pure corridor obtained by restricting the actual
wire to \(\mathcal W\subseteq\{H,\ldots,M\}\) is exactly
\[
 C_N^{\mathcal W}(a/N,b/N)
       =\sum_{r\in\mathcal W}A_{N,r}(a)A_{N,r}(b).
 \tag{13a}
\]
Its Fourier polynomial therefore has the same representation with
only these low-index features. Whenever \(\mathcal W\) contains two
distinct indices, (12)--(13) again prove nonproportionality. In
particular this applies, at all sufficiently large levels, to a
fixed strict wire window about the complete point and a sufficiently
small color cutoff \(H=\lfloor\delta N\rfloor\). The arguments below
apply separately to (8) and (13a); no estimate of their difference is
used to transfer a statement about zeros.

## 3. A sum-of-squares test for stability

We use an elementary fact about real polynomials.

**Lemma.** Let \(p_1,\ldots,p_m\in\mathbb R[u]\), let
\(H=\max\deg p_j\ge1\), and suppose at least two nonzero
features are not proportional. Then \(\sum_jp_j(u)^2\) has
a nonreal zero.

**Proof.** Its degree is \(2H\), since the squares of its real
leading coefficients cannot cancel. Suppose all its zeros were
real. Its nonnegativity on the real line makes every zero even,
so the sum is \(cQ(u)^2\), with \(c>0\) and \(Q\) a real
degree-\(H\) polynomial having only real zeros. At a real zero,
the vanishing order of the sum is twice the smallest vanishing
order of the \(p_j\): after removing that order, its leading
coefficient is a nonzero sum of real squares. Therefore \(Q\)
divides every \(p_j\). Their degrees are at most \(H\), so all
are scalar multiples of \(Q\), a contradiction. \(\square\)

A real polynomial in two variables is called real stable here if
it is nonzero whenever both variables have positive imaginary part.
By (12)--(13), the lemma applies to \(K_{N,H}(u,u)\). Since
its coefficients are real, one nonreal zero \(u_0\) lies in the
upper half-plane. Hence
\[
                         K_{N,H}(u_0,u_0)=0.
 \tag{14}
\]
Thus the actual full-source polynomial \(K_{N,H}\) is **not**
real stable for any \(N,H\) satisfying (6). No stability theorem
about coefficient extraction is needed for this conclusion.

The argument also explains why positivity of a boundary Gram is
different from real stability: a nontrivial Gram sum has several
independent features. Their diagonal is a sum of real squares,
not a real-rooted partition function.

## 4. Zeros in every disk/exterior choice

Clear the Laurent powers in (9):
\[
             P_{N,H}(z_1,z_2)
                =(z_1z_2)^H\mathscr F_{N,H}(z_1,z_2).
 \tag{15}
\]
This is an ordinary polynomial. Solve
\[
                         z^2-u_0z+1=0
\]
at the nonreal zero from (14). Neither solution has modulus one,
since \(z+z^{-1}\) is real on the unit circle. Their product is
one, so they are \(z_-,z_+=z_-^{-1}\), with
\(0<|z_-|<1<|z_+|\). Equation (11) gives
\[
              P_{N,H}(z_\varepsilon,z_\delta)=0
                 \qquad(\varepsilon,\delta\in\{-,+\}).
 \tag{16}
\]
The prefactor in (15) is nonzero at these points. Therefore the
actual finite-window source fails each of the four nonvanishing
conditions obtained by choosing the open unit disk or its exterior
independently for its two fugacities. In particular it does not have
the standard disk/exterior Lee–Yang property. Independent reversal
of fugacity orientations cannot repair this: (9) is separately
reciprocal, and all four choices already occur in (16).

## 5. The literal Gaussian factor is not positive definite

There is a separate elementary limitation on a Fourier-positivity
argument. Define the real angular restriction of the same full source
by
\[
                    A(t)=\mathscr F_{N,H}(e^{2\pi it},1).
\]
It is real and even for real \(t\). Moreover \(A(0)>0\), because
by (11) it is \(\sum_r p_r(2)^2\), and every low feature with
\(H\le r\le M\) has \(p_r(2)>0\) by (7). Thus \(A(t)\)
is nonzero on a real neighborhood of zero.

For any nonzero integer \(n\), the literal Gaussian multiplier
appearing in the filling functional gives
\[
                         g(t)=e^{\pi i nNt^2}A(t).
 \tag{17}
\]
This function is even but nonreal at arbitrarily small nonzero real
\(t\). It is not positive definite, even locally: positivity of the
two-point Gram matrices requires \(g(-t)=\overline{g(t)}\).
No common nonzero scalar phase repairs this, because positivity at
zero would force that phase to be positive real. This is an assertion
about the specified Gaussian-weighted source, not a replacement of
the complete filling functional by a convolution. That functional
also retains its original normal terms, charges and endpoint data.

## 6. What this rules out

The exact finite polynomial used above comes from a strict original
construction, with every wire and alias term retained, on the stated
finite color window. Consequently a proof that puts all such source
polynomials in a real-stable or disk/exterior Lee–Yang class cannot
extend the long-filling theorem. The literal Gaussian factor does not
supply a positive-definite substitute either.

These statements do not locate the zeros relative to an arbitrary
short filling's geometric saddle. They do not exclude a smaller,
construction-dependent geometric zero-free region, a different exact
relative-period representation, or a source-sensitive lower estimate.
In particular they neither disprove a volume identity nor prove a new
one. The existing nonzero small geometric neighborhood and the frozen
long-filling theorem are unchanged.

## Complete proof sources

All three complete proof texts were read at the matching pins below.
The first supplies the full physical turn and Frobenius pairing; the
second supplies the actual core, signed alias and their disjoint
supports; the third fixes the strict construction and component test.
The polynomial arguments above are proved in this note.

| Source | SHA-256 |
|---|---|
| [Original Newton turn and Gram](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Exact pure-circle colors](actual_pure_conway_auxiliary_color_leaf.md) | 2ef360ce60bcaa83969b4900a103573a76290714a59393e17ca25b52f07193c7 |
| [Strict construction definitions](research_strict_conway_family_definitions.md) | 55662159ccd65ae3183bc55b4f17b414d15a18b6970e3d54a725ba16247eeb1a |

The earlier even CROSS stability obstruction concerns a different
face polynomial. It is not used to infer any statement about the pure
source here. Fourier positivity, the definitions of these zero-free
classes, and the algebra of Gram kernels are standard; no general
novelty is claimed for them.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
